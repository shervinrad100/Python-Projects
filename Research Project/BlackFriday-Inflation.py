# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:34:10 2018

@author: sherv
"""

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

# Import data and construct moving average 
# Disposable income from: https://fred.stlouisfed.org/series/DSPIC96

disp_income = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv")
trends_amazon = pd.read_csv("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv")

# are the datasets of the same length?
"""
equal = len(disp_income)==len(trends_amazon)
if equal == False:
    print(disp_income)
    print(trends_amazon)
else:
    pass
"""
# investigate the sets and parse accordingly
trends_amazon = trends_amazon[:-2]
dates = mdates.num2date(mdates.datestr2num(trends_amazon['Month']))

# Check to see if the are the same
"""
time = mdates.num2date(mdates.datestr2num(disp_income['DATE']))
time == dates
"""
amazon = trends_amazon['amazon: (United States)']
RDPI = disp_income['DSPIC96']

def MA(series, n): # https://www.youtube.com/watch?v=5-SV_xXQ_wE
    weights = np.repeat(1.0, n)/n
    MA = np.convolve(series,weights,'valid')
    return MA
n =12
RDPI_MA = MA(RDPI,n)

plt.figure()
plt.plot(dates,amazon)
plt.figure()
plt.plot(dates,RDPI)
plt.plot(dates,RDPI_MA)
