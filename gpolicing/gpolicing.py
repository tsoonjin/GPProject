#!/usr/bin/env python
# coding: utf-8
import os
import GPy
import sys
import numpy as np

from config import PATH, TRAIN_PATH, TEST_PATH
from gp_utils import (load_as_dict, load_training, load_test, load_model, save_model,
                      count_from_prediction, in_sample_prediction, out_sample_forecast,
                      get_predicted_stats, stats_to_csv, get_truth_stats)


def init_params(offense):
    """ Returns psa_population and week_count """
    psa_pop = load_as_dict('{}{}'.format(PATH['info'], 'PSA_processed.csv'))
    week_count = load_as_dict('{}week_{}_count_3m.csv'.format(PATH['train'], offense))
    return psa_pop, week_count


def generate_kernel():
    # Make a kernel for the spatial only effect (which is in log space)
    kern_s = GPy.kern.Matern32(1, active_dims=[0], name='space_effect')
    kern_t = GPy.kern.RBF(1, active_dims=[1], name='time_effect')
    kern_p = GPy.kern.PeriodicExponential(1, active_dims=[1], period=52.0, name='periodic_effect')
    # Make a kernel for the space_time effect, f
    kern_st = kern_s * kern_t
    full_kern = kern_s + kern_t + kern_st
    return full_kern


def generate_model(train_path, psa_pop, week_count, full_kern, mname):
    X_train, Y_train, _, _, _ = load_training(train_path, psa_pop, week_count)
    filepath = '{}{}.npy'.format(PATH['models'], mname)
    if os.path.isfile(filepath):
        return load_model(X_train, Y_train, full_kern, filepath)
    likelihood_func = GPy.likelihoods.Poisson()
    laplace_inf = GPy.inference.latent_function_inference.Laplace()
    m = GPy.core.GP(X=X_train, Y=Y_train, kernel=full_kern, likelihood=likelihood_func,
                    inference_method=laplace_inf)
    m.optimize(messages=True)
    save_model(m, filepath)
    return m


def predict(m, X_test):
    predict_mean, predict_variance = m._raw_predict(X_test)
    return predict_mean, predict_variance


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python gpolicing.py [model_name] [offense]")
        exit()
    mname, offense = sys.argv[1:]
    psa_pop, week_count = init_params(offense)
    m = generate_model(TRAIN_PATH, psa_pop, week_count, generate_kernel(), mname)
    (predict_mean, _, X_test, truth_f, log_es_test, _) = out_sample_forecast(TEST_PATH, psa_pop, week_count,
                                                                             mname, offense, m)
    # psa_counts = get_predicted_stats(X_test, predict_mean, log_es_test, psa_pop.keys())
    psa_counts = get_truth_stats(X_test, truth_f, psa_pop.keys())
    stats_to_csv(psa_counts, '{}{}_truth.csv'.format(PATH['result'], mname))
