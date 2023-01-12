import statsmodels.api as sm 
import statsmodels.formula.api as smf 

def linear_regression(X, y):
    X = sm.add_constant(X)
    model = sm.OLS(y,X)
    results = model.fit()
    return results