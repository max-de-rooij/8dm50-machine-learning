from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def Poly_Regression(degree=4, **arg):
    return make_pipeline(PolynomialFeatures(degree),
                         LinearRegression(**arg))