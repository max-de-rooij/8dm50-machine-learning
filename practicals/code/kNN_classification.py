import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit
import operator
from sklearn.datasets import load_diabetes, load_breast_cancer

diabetes = load_diabetes()

breast_cancer = load_breast_cancer()
# load the dataset
# same as before, but now we use all features
X_train = diabetes.data[:300, :]
y_train = diabetes.target[:300, np.newaxis]
X_test = diabetes.data[300:, :]
y_test = diabetes.target[300:, np.newaxis]


def euclidian_distance(v1, v2):
    """ Function that will calculate the distance 
    between training data points and the data that we would like to classify
    """
    return np.sqrt(np.sum(np.power(v1-v2, 2)))

def get_neighbours(X_test_i, X_train, k):
    """ Function that get the nearest neighbours 
    of a test datapoint by calculating the ecleudian distance
    between the test point and traindataset
    
    Dependent on the amount of nearest neighbours (k), these
    will be stored in a list: neighbors"""
    dist = []
    neighbours = []
    
    # For a test datapoint we calculate the distance to each datapoint in the traindataset
    # And store this in a new list dist 
    for x in range(0, X_train.shape[0]):
        point_dist = euclidian_distance(X_train[x], X_test_i)
        dist.append((x, point_dist))  # Stores the xtrain index and distance in a new list
    dist.sort(key=operator.itemgetter(1)) # sorts the dist list by smallest distance 
    # For loop that stores the k nearest neighbours index in a list 
    for x in range(k):
        neighbours.append(dist[x][0])
    return neighbours


def predictkNNClass(output, y_train):
    classes = {}
    for i in range(len(output)):
#         print output[i], y_train[output[i]]
        if y_train[output[i]] in classes:
            classes[y_train[output[i]]] += 1
        else:
            classes[y_train[output[i]]] = 1
    sortedVotes = sorted(classes.iteritems(), key=operator.itemgetter(1), reverse=True)
    #print sortedVotes
    return sortedVotes[0][0]

def kNN(X_train, X_test, y_train, y_test, k):
    """ Function that calculates the predicted outcome 
    y_predict by calculating for each test dataset point
    the k nearest neighbours in the traindataset"""
    output_classes = []
    for x in range(0, X_test.shape[0]):
        y_pred = get_neighbours(X_test[x], X_train, k)
        predict_class = predictkNNClass(y_pred, y_train)
        output_classes.append(predict_class)
    return output_classes

kNN_test = kNN(X_train, X_test, y_train, y_test, 2)
