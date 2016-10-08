#!/usr/bin/env python
""" Stores configuration such as data path and date format """


TRAIN_PATH = '../data/train/3month/'
TEST_PATH = '../data/test/3month/'
OUTPUT_TRAIN_PATH = '../data/processed/train/'
OUTPUT_TEST_PATH = '../data/processed/test/'

# Dataframe headers
HEADERS = ["REPORT_DATE", "SHIFT", "OFFENSE", "METHOD", "BLOCK", "DISTRICT", "PSA", "WARD", "ANC",
           "NEIGHBORHOOD_CLUSTER", "BLOCK_GROUP", "CENSUS_TRACT", "VOTING_PRECINCT", "CCN",
           "XBLOCK", "YBLOCK", "START_DATE", "END_DATE"]
