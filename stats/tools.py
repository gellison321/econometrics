import numpy as np 
import pandas as pd 
import os
import statsmodels.formula.api as sm
from  statsmodels.stats.weightstats import CompareMeans, DescrStatsW
import matplotlib.pyplot as plt ; plt.rcParams["figure.figsize"] = (30,15)
import seaborn as sns
from rdrobust import rdrobust, rdplot, rdbwselect

def test_means(x1, x2):
    return CompareMeans(DescrStatsW(x1),  DescrStatsW(x2))

''' Basic Export to File -- Nothing to see here'''

def export_results_to_csv(summary, filename, directory = './Assignment_4_Files/'):
    for i in np.arange(len(summary.tables)):
        df = pd.DataFrame(summary.tables[i])
        if i == 0:
            type = 'results'
        if i == 1:
            type = 'coefficients'
        if i == 2:
            type = 'info'
        df.to_csv(directory + filename + '_' + type +'.csv')
