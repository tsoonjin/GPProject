#!/usr/bin/env python
""" Stores settings and constants used for processing in main code """


# Paths
ROOT = 'data/'
PATH = {'info': '{}{}'.format(ROOT, 'info/'),
        'train': '{}{}'.format(ROOT, 'train/'),
        'raw': '{}{}'.format(ROOT, 'raw/'),
        'test': '{}{}'.format(ROOT, 'test/'),
        'result': '{}{}'.format(ROOT, 'result/'),
        'figs': '{}{}'.format(ROOT, 'figs/'),
        'models': '{}{}'.format(ROOT, 'models/')}
TRAIN_PATH = '{}week_robbery_in_3m.csv'.format(PATH['train'])
TEST_PATH = '{}week_robbery_in_test1m.csv'.format(PATH['test'])
MAP_PATH = '{}geojsons/police-service-areas-psa.geojson'.format(ROOT)

# Data Format
HEADERS = ["REPORT_DATE", "SHIFT", "OFFENSE", "METHOD", "BLOCK", "DISTRICT", "PSA", "WARD", "ANC",
           "NEIGHBORHOOD_CLUSTER", "BLOCK_GROUP", "CENSUS_TRACT", "VOTING_PRECINCT", "CCN",
           "XBLOCK", "YBLOCK", "START_DATE", "END_DATE"]

CRIMES = {'theft': 'THEFT/OTHER', 'burglary': 'BURGLARY',
          'robbery': 'ROBBERY', 'assault': 'ASSAULT W/DANGEROUS WEAPON', 'homicide': 'HOMICIDE'}


# Map setting
DC_COORDINATES = (38.9072, -77.0639)
