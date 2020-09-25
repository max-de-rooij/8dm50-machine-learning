from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso

def Lasso_Pipe(alpha=1):
    return Lasso([('scaler', StandardScaler()), ('Lasso', Lasso(alpha))])