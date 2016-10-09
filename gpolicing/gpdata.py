#!/usr/bin/env python
import os
import pandas as pd

from config import (HEADERS, OUTPUT_TRAIN_PATH, OUTPUT_TEST_PATH, TRAIN_PATH, TEST_PATH, CRIMES,
                    INFO_PATH)


def write_csv(outpath, df):
    df.to_csv(outpath, sep=',')


def read_csv(filepath):
    """ Read csv and format data to ensure consistency """
    df = pd.read_csv(filepath, names=HEADERS)[1:]
    df['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
    df.set_index(['REPORT_DATE'], inplace='True')
    df.sort_index(inplace=True)
    return df


def groupby_weekonly(df, attr='OFFENSE', val='THEFT/OTHER'):
    filtered = df[df[attr] == val]
    return filtered.groupby(filtered.index.week)[attr].count()


def groupby_week(df, space='PSA', attr='OFFENSE', val='THEFT/OTHER'):
    filtered = df[df[attr] == val]
    return filtered.groupby([filtered.index.week, space])[attr].count()


def concat_read_csv(dirpath):
    filenames = os.listdir(dirpath)
    ls = []
    for f in filenames:
        if f.endswith('txt'):
            df = read_csv('{}{}'.format(dirpath, f))
            df['DISTRICT'] = int(f.split('.')[0][-1])
            ls.append(df)
    final_df = pd.concat(ls)
    return final_df


def process_psa():
    df = pd.read_csv('{}PSA.csv'.format(INFO_PATH))
    sum = df['TOTALPOP'].sum()
    df['TOTALPOP'] = df['TOTALPOP'] / sum
    df = df.ix[:, ['PSA', 'TOTALPOP']]
    df.sort_values(['PSA'], inplace=True)
    df.to_csv('{}PSA_processed.csv'.format(INFO_PATH), index=False, header=False)


def process_crime():
    # Reading 7 districts from 3 months of training data
    df_train = concat_read_csv(TRAIN_PATH)
    df_test = concat_read_csv(TEST_PATH)
    for k, v in CRIMES.items():
        write_csv('{}week_{}.csv'.format(OUTPUT_TRAIN_PATH, k), groupby_week(df_train, val=v))
        write_csv('{}weekonly_{}.csv'.format(OUTPUT_TRAIN_PATH, k), groupby_weekonly(df_train, val=v))
        write_csv('{}week_{}.csv'.format(OUTPUT_TEST_PATH, k), groupby_week(df_test, val=v))
        write_csv('{}weekonly_{}.csv'.format(OUTPUT_TEST_PATH, k), groupby_weekonly(df_test, val=v))


if __name__ == '__main__':
    process_psa()
