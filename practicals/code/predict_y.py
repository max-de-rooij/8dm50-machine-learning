# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:44:59 2020

@author: 20169491
"""
import numpy as np

def predict_y(X,beta):
    """ 
    least squares linear regression
    X       = input data matrix
    beta    = parameter coefficient vector
    Y       = Output predicted vector
    """
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)
    y_pred = X.dot(beta)
    print(y_pred.shape, 'y_pred')
    return y_pred