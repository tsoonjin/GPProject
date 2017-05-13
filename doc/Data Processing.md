1. Downloaded raw data from 2 Jun 10 to 2 Oct 16 (arbitrary start/end dates)
2. Processed/Fixed date orders from MDY to DMY (`process_dates.py`)
3. Sort by date and get data from May 16 to Jul 16 as TRAINING data and Aug 16 as TESTING data
4. Remove any strings found in the fields, and put 0 as value for missing data (`remove_strings.py`)
5. Name the resulting training file as `subset_train.csv` and testing file as `subset_test.csv`