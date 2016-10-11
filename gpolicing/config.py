#!/usr/bin/env python
""" Stores settings and constants used for processing in main code """


# Paths
ROOT = 'data/'
PATH = {'info': '{}{}'.format(ROOT, 'info/'),
        'train': '{}{}'.format(ROOT, 'train/'),
        'raw': '{}{}'.format(ROOT, 'raw/'),
        'test': '{}{}'.format(ROOT, 'test/'),
        'models': '{}{}'.format(ROOT, 'models/')}
TRAIN_PATH = '{}week_robbery_in_3m.csv'.format(PATH['train'])
TEST_PATH = '{}week_robbery_in_test1m.csv'.format(PATH['test'])

# Data Format
HEADERS = ["REPORT_DATE", "SHIFT", "OFFENSE", "METHOD", "BLOCK", "DISTRICT", "PSA", "WARD", "ANC",
           "NEIGHBORHOOD_CLUSTER", "BLOCK_GROUP", "CENSUS_TRACT", "VOTING_PRECINCT", "CCN",
           "XBLOCK", "YBLOCK", "START_DATE", "END_DATE"]

CRIMES = {'theft': 'THEFT/OTHER', 'burglary': 'BURGLARY',
          'robbery': 'ROBBERY', 'assault': 'ASSAULT W/DANGEROUS WEAPON', 'homicide': 'HOMICIDE'}
