import GPy
import csv
import numpy as np

# pip install GPy
with open('data/train.csv','rb') as train_file:
    reader = csv.reader(train_file)
    data = np.matrix(list(reader))[1:,:]
    
    features = data[:,:-1].astype(np.float)
    targets = data[:,-1]
    
    print "Features:", features

    m = GPy.models.GPRegression(features, targets)

print "Model:", m

with open('data/test.csv','rb') as test_file:
    reader = csv.reader(test_file)
    data = np.array(list(reader))[1:,:]

    features = data[:,:-1].astype(np.float)
    targets = data[:,-1]
    
    print "Number of features in test data:", data.shape[1]

    for i in range(data.shape[0]):
        mu, C = m.predict(np.array([features[i]]))
        print "Predicted:", mu, C
        print "Actual:", targets[i]

GPy.plotting.change_plotting_library('plotly')
fig = m.plot()
GPy.plotting.show(fig,  filename='basic_gp_regression_notebook')