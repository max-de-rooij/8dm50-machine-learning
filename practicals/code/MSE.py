# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:45:30 2020

@author: 20169491
"""
import numpy as np

def MSE(y_true,y_pred):
    MSE = np.square(np.subtract(y_true,y_pred)).mean() 
    return MSE
