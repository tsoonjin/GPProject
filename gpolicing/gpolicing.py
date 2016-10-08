#!/usr/bin/env python
import GPy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

from config import OUTPUT_TRAIN_PATH, OUTPUT_TEST_PATH


def setup_gp(X, Y, optimizer='scg'):
    kernel = GPy.kern.RBF(input_dim=1, variance=1, lengthscale=0.1)
    m = GPy.models.GPRegression(X, Y, kernel)
    m.optimize(optimizer='lbfgs', max_iters=100)
    print(m)
    m.plot()
    plt.show()
    return m


def process_data():
    pass


if __name__ == '__main__':
    process_data()
