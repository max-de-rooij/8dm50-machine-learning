# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:00:26 2020

@author: 20169491
"""
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn import linear_model
from sklearn.pipeline import Pipeline

def PolynomialRegression(degree=2): #for degree=1, linear regression is returned
    return Pipeline ([
    ('Poly', PolynomialFeatures(degree)),
 #   ("std_scaler", StandardScaler()), #needed when samples are not scaled
    ('Lin_reg', linear_model.LinearRegression())
    ])
