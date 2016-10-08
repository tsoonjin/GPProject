#!/usr/bin/env python
import GPy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import calendar

from config import OUTPUT_TRAIN_PATH, OUTPUT_TEST_PATH


def date_to_day(date):
    """ Converts Panda datetime to day """
    days = calendar.monthrange(date.year, date.month)[1] + date.day
    return date.week


def setup_gp(X, Y, optimizer='scg'):
    kernel = GPy.kern.RBF(input_dim=1, variance=1, lengthscale=0.1)
    m = GPy.models.GPRegression(X, Y, kernel)
    m.optimize(optimizer='lbfgs', max_iters=100)
    print(m)
    m.plot()
    plt.show()
    return m


def main():
    df = pd.read_csv('{}D3_week_count.csv'.format(OUTPUT_TRAIN_PATH), names=['REPORT_DATE', 'COUNT'])
    df_test = pd.read_csv('{}D3_week_count.csv'.format(OUTPUT_TEST_PATH), names=['REPORT_DATE', 'COUNT'])
    df['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
    df_test['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
    T_test = np.array([[date_to_day(t) for t in df_test.as_matrix(columns=df_test.columns[0:1]).ravel()]])
    T_test = np.array([df_test.as_matrix(columns=df_test.columns[0:1]).ravel()])
    Y_test = np.array([df_test.as_matrix(columns=df_test.columns[1:]).ravel()])
    T = np.array([[date_to_day(t) for t in df.as_matrix(columns=df.columns[0:1]).ravel()]])
    T = np.array([df.as_matrix(columns=df.columns[0:1]).ravel()])
    Y = np.array([df.as_matrix(columns=df.columns[1:]).ravel()])
    print(T)
    m = setup_gp(T.T, Y.T)
    predicted_count, predicted_uncertainty = m.predict(T_test.T)
    plt.plot(predicted_count, 'r-')
    plt.plot(Y_test.T, 'b-')
    plt.show()
    # Predict


if __name__ == '__main__':
    main()
