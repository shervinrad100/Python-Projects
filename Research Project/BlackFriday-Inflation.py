# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:34:10 2018

@author: sherv
"""

import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np

# Disposable income from: https://fred.stlouisfed.org/series/DSPIC96

DSPIC96 = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv")
Google_amazon_US = pd.read_csv("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv")

Google_amazon_US = Google_amazon_US[:-2] # Google has more data so we delete it
dates = mdates.num2date(mdates.datestr2num(DSPIC96['DATE']))

MA_time = mdates.num2date(mdates.datestr2num(Google_amazon_US['Month']))


amazon = Google_amazon_US['amazon: (United States)']
RDPI = DSPIC96['DSPIC96']

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
plt.plot(RDPI_MA)

