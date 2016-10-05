#!/usr/bin/env python
import GPy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

from config import OUTPUT_PATH


def date_to_day(date):
    """ Converts Panda datetime to day """
    days = calendar.monthrange(date.year, date.month)[1] + date.day
    return days


def setup_gp(X, Y):
    kernel = GPy.kern.RBF(input_dim=1, variance=1., lengthscale=1.)
    m = GPy.models.GPRegression(X, Y, kernel)
    fig = m.plot()
    plt.show()
    m.optimize_restarts(messages=True, num_restarts=10)


def main():
    df = pd.read_csv('{}D3_day_count.csv'.format(OUTPUT_PATH), names=['REPORT_DATE', 'COUNT'])
    df['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
    T = np.array([[date_to_day(t) for t in df.as_matrix(columns=df.columns[0:1]).ravel()]])
    Y = np.array([df.as_matrix(columns=df.columns[1:]).ravel()])
    setup_gp(T.T, Y.T)


if __name__ == '__main__':
    main()
