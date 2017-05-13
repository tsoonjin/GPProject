import GPy
import csv
import numpy as np
from datetime import datetime
import plotly.plotly as py
import plotly

# swaps the date and month columns (1,17,18) from the raw data
with open('test_data.csv','rb') as data_file:
    reader = csv.reader(data_file, delimiter=',')
    data = list(reader)
    no_of_data = len(data)
    
    processed_train = open('aggregated_test_data.csv','wb')
    writer = csv.writer(processed_train, delimiter=',')
        
    writer.writerow(["Month", "PSA", "Crime count"])
    
    pattern = '%d/%m/%y %H:%M'
    
    cur_month = 12
    psa_list = []
    crime_counts = []
    for i in range(1,no_of_data):
        target_time = data[i][0]
        psa = data[i][1]
        datetime = datetime.strptime(target_time, pattern)
        
        if datetime.month is not cur_month:
            for j in range(len(psa_list)):
                writer.writerow([cur_month, psa_list[j], crime_counts[j]])
                                 
            psa_list = []
            crime_counts = []
            if cur_month is 1:
                cur_month=12
            else:
                cur_month-=1
        else:
            if psa not in psa_list:
                psa_list.append(psa)
                crime_counts.append(1)
            else:
                crime_counts[psa_list.index(psa)]+=1
    for j in range(len(psa_list)):
        writer.writerow([cur_month, psa_list[j], crime_counts[j]])
