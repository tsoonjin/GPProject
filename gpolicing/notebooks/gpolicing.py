#!/usr/bin/env python
# coding: utf-8
import math
import numpy as np
import scipy as sp
import GPy

from config import PATH


psa_pop = {str(i[0]): i[1] for i in np.genfromtxt('../data/info/PSA_processed.csv', delimiter=',')}
weekly_theft_count = {str(i[0]): i[1] for i in np.genfromtxt('../data/train/week_theft_count_3m.csv', delimiter=',')}
avg_weekly_count = np.mean(list(weekly_theft_count.values()))
train_theft = np.genfromtxt('../data/train/week_theft_in_3m.csv', delimiter=',')
train_theft_dict = {str(i[1])+str(i[0]): i[2] for i in train_theft}
# Training input
time_train = train_theft[:, 0].ravel()
space_train = train_theft[:, 1].ravel()
space_grid, time_grid = np.meshgrid(np.unique(space_train), np.unique(time_train))
X_train = np.vstack([space_grid.ravel(), time_grid.ravel()]).T
# Training output
intensity_train = np.array([[math.log(train_theft_dict.get('{}{}'.format(*i), 0.000001)) for i in X_train]]).T
log_es = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_train]]).T
truth_lamda = np.exp(intensity_train + log_es)
truth_lamda_grid = truth_lamda.reshape(len(weekly_theft_count.keys()), len(psa_pop.keys()))
Y_train = np.array([[sp.stats.poisson.rvs(i) for i in truth_lamda]]).T


# Make a kernel for the spatial only effect (which is in log space)
kern_s = GPy.kern.Matern32(1, active_dims=[0], name='space_effect')
kern_t = GPy.kern.RBF(1, active_dims=[1], name='time_effect')
kern_p = GPy.kern.PeriodicExponential(1, active_dims=[1], period=52.0, name='periodic_effect')
# Make a kernel for the space_time effect, f
kern_st = kern_s * kern_t
full_kern = kern_s + kern_t + kern_st


likelihood_func = GPy.likelihoods.Poisson()
laplace_inf = GPy.inference.latent_function_inference.Laplace()
m = GPy.core.GP(X=X_train, Y=Y_train, kernel=full_kern, likelihood=likelihood_func, inference_method=laplace_inf)
m.optimize()


# Testing
test_theft = np.genfromtxt('../data/test/week_theft_in_test1m.csv', delimiter=',')
test_theft_dict = {str(i[1])+str(i[0]): i[2] for i in test_theft}
# Training input
time_test = test_theft[:, 0].ravel()
space_test = test_theft[:, 1].ravel()
space_grid_test, time_grid_test = np.meshgrid(np.unique(space_test), np.unique(time_test))
X_test = np.vstack([space_grid_test.ravel(), time_grid_test.ravel()]).T
intensity_test = np.array([[train_theft_dict.get('{}{}'.format(*i), 0.000001) for i in X_test]]).T
pred_mean, pred_variance = m._raw_predict(X_test)
log_es_test = np.array([[math.log(avg_weekly_count * psa_pop[str(i[0])]) for i in X_test]]).T
