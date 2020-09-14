from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

def poly_estimator(degree=1):
    model = Pipeline([
                 ("poly_features", PolynomialFeatures(degree)),
                 ("regression", LinearRegression())
                ])
    
    return model