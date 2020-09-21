from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

def PolynomialRegression(degree=2):
    return make_pipeline(PolynomialFeatures(degree),
                         LinearRegression())