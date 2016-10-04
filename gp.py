import GPy
import csv
import numpy as np
import time
import plotly.plotly as py
import plotly

# pip install GPy
# Roughly following GPy tutorial at http://nbviewer.jupyter.org/github/SheffieldML/notebook/blob/master/GPy/basic_gp.ipynb

# Requires `pip install plotly` and sign up at plot.ly for api key
# Need to execute the following once to set the credentials file locally; can be commented out after that
# plotly.tools.set_credentials_file(username='username', api_key='api_key')
with open('data/subset_train.csv','rb') as data_file:
    reader = csv.reader(data_file)
    data = np.matrix(list(reader))[1:,:]
    
    features = data[:,1:].astype(np.int).astype(np.float)
    targets = data[:,0]
    
    
    print features

    m = GPy.models.GPRegression(features, targets)