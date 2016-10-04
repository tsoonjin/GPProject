import GPy
import csv
import numpy as np

# pip install GPy
with open('data/subset_train.csv','rb') as train_file:
    reader = csv.reader(train_file)
    data = np.matrix(list(reader))[1:,:]
    
    features = data[:,1:].astype(np.int).astype(np.float)
    targets = data[:,0]
    
    print "Number of features in training data:", data.shape[1]

    m = GPy.models.GPRegression(features, targets)


with open('data/subset_train.csv','rb') as test_file:
    reader = csv.reader(test_file)
    data = np.matrix(list(reader))[1:,:]

    features = data[:,1:].astype(np.int).astype(np.float)
    targets = data[:,0]
    
    print "Number of features in test data:", data.shape[1]

    for i in range(data.shape[0]):
        print "Predicting for:", features[i]
        mu, C, up95, lo95 = m.predict(features[i])
        print "Predicted:", mu
        print "Actual:", targets[i]