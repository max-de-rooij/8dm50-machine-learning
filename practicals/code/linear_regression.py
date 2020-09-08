import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


def lsq(X, y):
    """
    Least squares linear regression
    :param X: Input data matrix
    :param y: Target vector
    :return: Estimated coefficient vector for the linear regression
    """

    # add column of ones for the intercept
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)

    # calculate the coefficients
    beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))
    y_hat = X.dot(beta)
    return beta

def knn_classify(X_train, y_train, k, X_test):

    # Initialize predicted classes
    predicted_class = []
    
    # Normalize features in X_test and X_train
    X_test = (X_test - np.ones(X_test.shape) * np.mean(X_test, axis=0))/(np.std(X_test, axis=0))
    X_train = (X_train - np.ones(X_train.shape) * np.mean(X_train, axis=0))/(np.std(X_train, axis=0))

    # for every point in the test set
    for i in range(len(X_test)):
        # Calculate the difference between the point in the test set and every point in the training set
        diff = X_train - np.ones(X_train.shape) * X_test[i,:]
        # the distances are then diag(diff*diff^T) (sum of squared differences = tr(diff*diff^T)) 
        dist = np.diagonal(diff.dot(np.transpose(diff)))

        # get the indices of a sorted list of distances
        dist_sorted_idx = np.argsort(dist)

        # get the k shortest distances
        idx_k = dist_sorted_idx[:k]

        # obtain the classes of those points
        classes = y_train[idx_k]

        # count the amount of class 0 and class 1
        unique,counts = np.unique(classes, return_counts=True)

        # predicted class is the most frequent class in the k closest points
        predicted_class.append(unique[np.argmax(counts)])
    return predicted_class

def knn_regression(X_train, y_train, k, X_test):

    # Initialize output y values
    y_hat = []
    # Normalize features in X_test and X_train
    X_test = (X_test - np.ones(X_test.shape) * np.mean(X_test, axis=0))/(np.std(X_test, axis=0))
    X_train = (X_train - np.ones(X_train.shape) * np.mean(X_train, axis=0))/(np.std(X_train, axis=0))

    # for every point in the test set
    for i in range(len(X_test)):
        # Calculate the difference between the point in the test set and every point in the training set
        diff = X_train - np.ones(X_train.shape) * X_test[i,:]
        # the distances are then diag(diff*diff^T) (sum of squared differences = tr(diff*diff^T)) 
        dist = np.diagonal(diff.dot(np.transpose(diff)))

        # get the indices of a sorted list of distances
        dist_sorted_idx = np.argsort(dist)

        # get the k shortest distances
        idx_k = dist_sorted_idx[:k]

        # obtain the mean of the output-values of those points
        output = np.mean(y_train[idx_k])
       
        y_hat.append(output)

    return y_hat

def class_conditional_probability(X,y):
    fig,ax = plt.subplots(int(X.shape[1]/5),5)
    fig.set_figheight(25)
    fig.set_figwidth(20)
    for i in range(X.shape[1]):
        c0 = np.sort(X[y==0,i])
        #c0 = (c0-np.mean(c0))/np.std(c0)
        c1 = np.sort(X[y==1,i])
        #c1 = (c1-np.mean(c1))/np.std(c1)
        curax = ax[i//5, i%5]
        curax.plot(c0,norm.pdf(c0, np.mean(c0), np.std(c0)), c1, norm.pdf(c1, np.mean(c1), np.std(c1)))
        curax.set_title(f'feature number {i+1}')
    plt.show()

        