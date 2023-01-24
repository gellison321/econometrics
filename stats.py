import numpy as np 
import pandas as pd 
import os
import statsmodels.api as sm 
import statsmodels.formula.api as smf
from  statsmodels.stats.weightstats import CompareMeans, DescrStatsW

def linear_regression(x, y):
    return sm.OLS(y.astype(int), np.asarray(sm.add_constant(x.astype(int)))).fit()


def test_means(x1, x2):
    return CompareMeans(DescrStatsW(x1),  DescrStatsW(x2))
