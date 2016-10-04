import GPy
import csv
import numpy as np
import time
import plotly.plotly as py
import plotly

with open('processed_train.csv','rb') as data_file:
    reader = csv.reader(data_file, delimiter=',')
    data = list(reader)
    no_of_data = len(data)
    
    for i in range(no_of_data - 1):
        target_time = data[i + 1][0]
        time_obj = time.strptime(target_time, '%d/%m/%y %H:%M')
        day = int(time.strftime('%d', time_obj))
        hour = int(time.strftime('%H', time_obj))
        minute = int(time.strftime('%M', time_obj))
        second = int(time.strftime('%S', time_obj))
        data[i + 1][0] = ((day * 24 + hour) * 60 + minute) * 60 + second

        cluster = data[i + 1][3]
        if cluster is "":
            data[i + 1][3] = "0"
        else:
            data[i + 1][3] = cluster.replace("Cluster ", "")
        
        precinct = data[i + 1][5]
        data[i + 1][5] = precinct.replace("Precinct","")

        target_time = data[i + 1][9]
        time_obj = time.strptime(target_time, '%d/%m/%y %H:%M')
        day = int(time.strftime('%d', time_obj))
        hour = int(time.strftime('%H', time_obj))
        minute = int(time.strftime('%M', time_obj))
        second = int(time.strftime('%S', time_obj))
        data[i + 1][9] = ((day * 24 + hour) * 60 + minute) * 60 + second

        target_time = data[i + 1][10]
        if target_time is not "":
            time_obj = time.strptime(target_time, '%d/%m/%y %H:%M')
            day = int(time.strftime('%d', time_obj))
            hour = int(time.strftime('%H', time_obj))
            minute = int(time.strftime('%M', time_obj))
            second = int(time.strftime('%S', time_obj))
            data[i + 1][10] = ((day * 24 + hour) * 60 + minute) * 60 + second


with open('undiscreted_train.csv','wb') as undiscreted_test:
    writer = csv.writer(undiscreted_test, delimiter=',')
    writer.writerows(data)