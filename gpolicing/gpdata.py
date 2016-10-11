#!/usr/bin/env python
import os
import pandas as pd

from config import HEADERS, PATH, CRIMES


# I/O operations

def write_csv(outpath, df):
    df.to_csv(outpath, sep=',')


def read_csv(filepath, index_by_date=True):
    """ Read csv and format data to ensure consistency """
    # Ignores headers
    df = pd.read_csv(filepath, names=HEADERS)[1:]
    if index_by_date:
        df['REPORT_DATE'] = pd.to_datetime(df['REPORT_DATE'])
        df.set_index(['REPORT_DATE'], inplace='True')
        df.sort_index(inplace=True)
    return df


def concat_read_csv(dirpath, extension='txt'):
    '''' Read all files that matches given extension as a single data frame '''
    filenames = os.listdir(dirpath)
    concat_df = pd.concat([read_csv('{}{}'.format(dirpath, f))
                           for f in filenames if f.endswith(extension)])
    return concat_df


# Sorting data

def groupby_week_count(df, attr='OFFENSE', val='THEFT/OTHER'):
    ''' Returns count of crime for a given offense for each week '''
    filtered = df[df[attr] == val]
    return filtered.groupby(filtered.index.week)[attr].count()


def groupby_week_space(df, space='PSA', attr='OFFENSE', val='THEFT/OTHER'):
    ''' Returns count of crime for a given space for each week '''
    filtered = df[df[attr] == val]
    return filtered.groupby([filtered.index.week, space])[attr].count()


def get_psa_population():
    ''' Generates population of a PSA divided by total population '''
    df = pd.read_csv('{}PSA_raw.csv'.format(PATH['info']))
    sum = df['TOTALPOP'].sum()
    df['TOTALPOP'] = df['TOTALPOP'] / sum
    df = df.ix[:, ['PSA', 'TOTALPOP']]
    df.sort_values(['PSA'], inplace=True)
    df.to_csv('{}PSA_processed.csv'.format(PATH['info']), index=False, header=False)


def process_training(filepath, outpath):
    concat_df = concat_read_csv('{}{}/'.format(PATH['raw'], filepath))
    for k, v in CRIMES.items():
        write_csv('{}week_{}_in_{}.csv'.format(PATH[outpath], k, filepath),
                  groupby_week_space(concat_df, val=v))
        write_csv('{}week_{}_count_{}.csv'.format(PATH[outpath], k, filepath),
                  groupby_week_count(concat_df, val=v))


if __name__ == '__main__':
    process_training('test1m', 'test')
