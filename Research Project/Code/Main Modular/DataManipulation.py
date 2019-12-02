import pandas as pd 
import numpy as np
import random

def importdata(key, path ,parseCol, From="2004-01-01", To="2019-09-01"):
    ''' 
    make sure the end date of the parse is shared between all datasets
    '''
    dataset = pd.read_csv("%s" %(path), index_col="%s" %(parseCol), parse_dates=["%s" %(parseCol)])
    if From!=None and To!=None:
        dataset = dataset.loc[From:To]
    return dataset

