#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"
Google_amazon_US = pd.read_csv("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv", index_col="Month", parse_dates=["Month"])
DSPIC = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", index_col="DATE", parse_dates=["DATE"])

# Adjust datasets
Google_amazon_US = Google_amazon_US[:-2]

# Create Moving Average
DSPIC['MA_12'] = DSPIC["DSPIC96"].rolling(12).mean()

# Google trends: amazon: (United States)
plt.figure(1)
Google_amazon_US["amazon: (United States)"].plot()
plt.xlabel("Year")
plt.ylabel("%")
plt.grid()
plt.legend()

# Real Disposable Personal Incom
plt.figure(2)
DSPIC["DSPIC96"].plot()
DSPIC["MA_12"].plot()
plt.xlabel("Year")
plt.ylabel("$")
plt.grid()
plt.legend()
