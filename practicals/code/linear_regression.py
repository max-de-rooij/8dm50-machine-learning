import numpy as np

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

    return beta

def mse(X, y_true, beta):
    '''
    measures the average squared difference between
    the predicted values and true values
    '''
    # add column of ones to X
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)
 
    y_pred = np.dot(X,beta)
 
    MSE = np.square(np.subtract(y_true,y_pred)).mean() 
    return MSE

