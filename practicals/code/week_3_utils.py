from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import GridSearchCV

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

import pandas as pd


def lasso_estimator(alpha=1.0):

    model = Pipeline([
        ('normalize', StandardScaler()),
        ('lasso', Lasso(alpha=alpha))
    ])
    return model

def cv_lasso(alpha_range, folds=5):

    param_grid = {'lasso__alpha': alpha_range}
    model = GridSearchCV(lasso_estimator(), param_grid, cv=folds, verbose=0)
    return model
