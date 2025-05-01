#%pip install -r requirements.txt

#Importing
import pandas as pd
import numpy as np
import eep153_tools
import cfe
from cfe import Regression
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")

from Acquiring_Dataframes import ugd8_p, ugd8_x, ugd8_c, ugd8_z, ugd_fct, ugd_rdi

#Get saved result
ugd8_result = cfe.read_pickle('RGSN Files/Uganda19-20.rgsn')

#Reference prices
pbar = ugd8_p.mean(axis=1)
pbar = pbar.reset_index(level="u", drop=True) 
pbar = pbar.reindex(ugd8_result.beta.index) 
pbar = pbar.replace(np.nan,1)
def my_prices(j,p0,p=pbar):
    """
    Change price of jth good to p0, holding other prices fixed.
    """
    p = p.copy()
    p.loc[j] = p0
    return p

#Budgets
xhat = ugd8_result.predicted_expenditures()
xbar = xhat.groupby(['i','t','m']).sum()
xref = xbar.quantile(0.5) 

#Food Quantities
qhat = (xhat.unstack('j')/ugd8_p.reset_index(drop=True, level="u").transpose()).dropna(how='all')
qhat = qhat.loc[:,qhat.count()>0]

#Mapping Nutrients

# Create a new FCT and vector of consumption that only share rows in common:
fct0,c0 = ugd_fct.align(qhat.T,axis=0,join='inner')

# The @ operator means matrix multiply
N = fct0.T@c0

N  #NB: Uganda quantities are for previous 7 days

def nutrient_demand(x,p):
    c = ugd8_result.demands(x,p)
    fct0,c0 = ugd_fct.align(c,axis=0,join='inner')
    N = fct0.T@c0

    N = N.loc[~N.index.duplicated()]
    
    return N

# In first round, averaged over households and villages
dbar = ugd8_result.d[ugd_rdi.columns].mean()

# This matrix product gives minimum nutrient requirements for
# the average household
hh_rdi = ugd_rdi@dbar

hh_rdi

def nutrient_adequacy_ratio(x,p,d,rdi=ugd_rdi,days=7):
    hh_rdi = ugd_rdi.replace('',0)@d*days

    return nutrient_demand(x,p)/hh_rdi




