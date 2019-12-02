import pandas as pd

from keras.layers import LSTM


def importdata(key, path ,parseCol, From="2004-01-01", To="2019-09-01"):
    ''' 
    make sure the end date of the parse is shared between all datasets
    '''
    dataset = pd.read_csv("%s" %(path), index_col="%s" %(parseCol), parse_dates=["%s" %(parseCol)])
    if From!=None and To!=None:
        dataset = dataset.loc[From:To]
    return dataset

import_PATH = r"E:\GitHub\Python-Projects\Research Project\Data"

meta = {# dataset: [path, Date_col, Value_col]
        "Google":[f"{import_PATH}\multiTimeline.csv", "Month", "Top5"], 
        "SP500": [f"{import_PATH}\S&P500.csv", "Date", "Close"]
}

data ={}
for key in meta.keys():
    data[key] = importdata(key, meta[key][0], meta[key][1])
    
SP = data["SP500"][meta["SP500"][2]].loc[:"2019-01-01"]
GGL = data["Google"][meta["Google"][2]].loc[:"2019-01-01"]
