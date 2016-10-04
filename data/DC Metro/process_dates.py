import GPy
import csv
import numpy as np
import time
import plotly.plotly as py
import plotly

# swaps the date and month columns (1,17,18) from the raw data
with open('raw_data.csv','rb') as data_file:
    reader = csv.reader(data_file, delimiter=',')
    data = list(reader)
    no_of_data = len(data)
    
    for i in range(no_of_data - 1):
        target_time = data[i + 1][0]
        data[i + 1][0] = time.strftime('%d/%m/%Y %I:%M %p', time.strptime(target_time, pattern))

        target_time = data[i + 1][16]
        data[i + 1][16] = time.strftime('%d/%m/%Y %I:%M %p', time.strptime(target_time, pattern))
        
        target_time = data[i + 1][17]
        if target_time is not "":
            data[i + 1][17] = time.strftime('%d/%m/%Y %I:%M %p', time.strptime(target_time, pattern))


with open('processed_dates_data.csv','wb') as processed_train:
    writer = csv.writer(processed_train, delimiter=',')
    writer.writerows(data)