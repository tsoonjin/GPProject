#!/usr/bin/env python
import os
import pandas as pd

from config import TRAIN_PATH, HEADERS, OUTPUT_TRAIN_PATH, TEST_PATH, OUTPUT_TEST_PATH


def write_csv(outpath, df):
    df.to_csv(outpath, sep=',')


def read_csv(filepath):
    """ Read csv and format data to ensure consistency """
    df = pd.read_csv(filepath, names=HEADERS)[1:]
    df['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
    df.set_index(['REPORT_DATE'], inplace='True')
    df.sort_index(inplace=True)
    return df


def get_month_count(df):
    return df.groupby(pd.TimeGrouper("M"))['METHOD'].count()


def get_week_count(df):
    return df.groupby(df.index.week)['METHOD'].count()


def get_day_count(df):
    return df.groupby(df.index.date)['METHOD'].count()


def get_shiftday_count(df):
    return df.groupby([df.index.date, 'SHIFT'])['METHOD'].count()


def get_psaday_count(df):
    return df.groupby([df.index.date, 'PSA'])['METHOD'].count()


def get_censusday_count(df):
    return df.groupby([df.index.date, 'CENSUS_TRACT'])['METHOD'].count()


def get_districtday_count(df):
    return df.groupby([df.index.date, 'DISTRICT'])['METHOD'].count()


def get_censustract_count(df):
    return df.groupby(df['CENSUS_TRACT'])['METHOD'].count()


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


if __name__ == '__main__':
    # Reading 7 districts from 3 months of training data
    concat_df = concat_read_csv(TRAIN_PATH)
    dfs = {'D{}'.format(i): read_csv('{}D{}.txt'.format(TEST_PATH, i)) for i in range(1, 8)}
    # Write processed dataframe to desired output
    for k, df in dfs.items():
        write_csv('{}{}_week_count.csv'.format(OUTPUT_TEST_PATH, k), get_week_count(df))
    write_csv('{}DALL_processed.csv'.format(OUTPUT_TEST_PATH), concat_df)
    write_csv('{}DALL_districtday_count.csv'.format(OUTPUT_TEST_PATH), get_districtday_count(concat_df))
