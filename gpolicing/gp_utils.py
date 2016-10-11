#!/usr/bin/env python
import numpy as np
import scipy as sp
import GPy
import math
import csv

from collections import OrderedDict


def save_model(m, filepath):
    print('Saving model to: {}\n{}'.format(filepath, m))
    np.save(filepath, m.param_array)


def load_model(X_train, Y_train, full_kern, filepath, likelihood_func=GPy.likelihoods.Poisson(),
               latent_inf=GPy.inference.latent_function_inference.Laplace()):
    print('Loading model from: {}'.format(filepath))
    m = GPy.core.GP(X=X_train, Y=Y_train, kernel=full_kern, likelihood=likelihood_func,
                    inference_method=latent_inf)
    m.update_model(False)
    m.initialize_parameter()
    m[:] = np.load(filepath)
    m.update_model(True)
    print(m)
    return m


def load_as_dict(filepath):
    return {str(i[0]): i[1] for i in np.genfromtxt(filepath, delimiter=',')}


def load_training(filepath, psa_pop, week_count):
    """ Return X, Y training data for model and grids for plotting """
    avg_weekly_count = np.mean(list(week_count.values()))
    train_data = np.genfromtxt(filepath, delimiter=',')
    train_data_dict = {str(i[1])+str(i[0]): i[2] for i in train_data}
    # Training input
    time_train = train_data[:, 0].ravel()
    space_train = train_data[:, 1].ravel()
    space_grid, time_grid = np.meshgrid(np.unique(space_train), np.unique(time_train))
    X_train = np.vstack([space_grid.ravel(), time_grid.ravel()]).T
    # Training output
    truth_f = np.array([[math.log(train_data_dict.get('{}{}'.format(*i), 0.000001))
                        for i in X_train]]).T
    log_es = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_train]]).T
    truth_lamda = np.exp(truth_f + log_es)
    truth_lamda_grid = truth_lamda.reshape(len(week_count.keys()), len(psa_pop.keys()))
    Y_train = np.array([[sp.stats.poisson.rvs(i) for i in truth_lamda]]).T
    return X_train, Y_train, space_grid, time_grid, truth_lamda_grid


def load_test(filepath, psa_pop, week_count):
    """ Return X, Y test data and grids for plotting"""
    avg_weekly_count = np.mean(list(week_count.values()))
    test_data = np.genfromtxt(filepath, delimiter=',')
    test_data_dict = {str(i[1])+str(i[0]): i[2] for i in test_data}
    # Test input
    time_test = test_data[:, 0].ravel()
    space_test = test_data[:, 1].ravel()
    space_grid, time_grid = np.meshgrid(np.unique(space_test), np.unique(time_test))
    X_test = np.vstack([space_grid.ravel(), time_grid.ravel()]).T
    # Test output
    truth_f = np.array([[test_data_dict.get('{}{}'.format(*i), 0) for i in X_test]]).T
    log_es_test = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_test]]).T
    return X_test, truth_f, log_es_test


def count_from_prediction(predictive_mean, log_es_test):
    return np.exp(predictive_mean + log_es_test)


def calc_MSE(truth_f, predictive_f):
    return ((truth_f - predictive_f)**2).mean()


def in_sample_prediction(train_path, psa_pop, week_count, mname, offense, model, test_samples=300):
    avg_weekly_count = np.mean(list(week_count.values()))
    X_train, Y_train, _, _, _ = load_training(train_path, psa_pop, week_count)
    test_indices = np.random.permutation(range(X_train.shape[0]))[:test_samples]
    X_test = X_train[test_indices]
    Y_test = Y_train[test_indices]
    predict_mean, predict_variance = model._raw_predict(X_test)
    log_es_test = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_test]]).T
    mse = calc_MSE(Y_test, count_from_prediction(predict_mean, log_es_test))
    log_result(offense, mname, mse, predict_mean, log_es_test)
    return predict_mean, predict_variance, mse


def out_sample_forecast(test_path, psa_pop, week_count, mname, offense, model):
    avg_weekly_count = np.mean(list(week_count.values()))
    X_test, truth_f, log_es_test = load_test(test_path, psa_pop, week_count)
    predict_mean, predict_variance = model._raw_predict(X_test)
    log_es_test = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_test]]).T
    mse = calc_MSE(truth_f, count_from_prediction(predict_mean, log_es_test))
    log_result(offense, mname, mse, predict_mean, log_es_test)
    return predict_mean, predict_variance, X_test, truth_f, log_es_test, mse


def log_result(offense, mname, mse, predict_mean, log_es_test):
    res = np.c_[predict_mean, count_from_prediction(predict_mean, log_es_test)]
    print('Offense: {}\tModel: {}\tMSE: {}'.format(offense, mname, mse))
    print('Relative risk | Counts\n{}'.format(res))


def get_truth_stats(X_test, Y_test, psa_keys, weeks=[22]):
    """ Returns psa and truth data """
    psa_counts = OrderedDict({p.split('.')[0]: [0, 0] for p in psa_keys})
    for i, test in enumerate(X_test):
        if test[1] not in weeks:
            break
        psa_counts[str(int(test[0]))][0] = psa_counts[str(int(test[0]))][0] + Y_test[i][0]
    return psa_counts


def get_predicted_stats(X_test, predict_mean, log_es_test, psa_keys, weeks=[22]):
    """ Returns psa and crime count as csv """
    counts = count_from_prediction(predict_mean, log_es_test)
    log_relative_risk = predict_mean
    psa_counts = OrderedDict({p.split('.')[0]: [0, 0] for p in psa_keys})
    for i, test in enumerate(X_test):
        if test[1] not in weeks:
            break
        psa_counts[str(int(test[0]))][0] = psa_counts[str(int(test[0]))][0] + counts[i][0]
        psa_counts[str(int(test[0]))][1] = psa_counts[str(int(test[0]))][1] + log_relative_risk[i][0]
    return psa_counts


def stats_to_csv(my_dict, filepath, columns=['PSA', 'COUNT', 'RELATIVE']):
    with open(filepath, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        for key, value in my_dict.items():
            writer.writerow([key, value[0], value[1]])
