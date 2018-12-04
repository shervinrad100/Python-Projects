#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Import data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"
Google_amazon_US = pd.read_csv("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv", index_col="Month", parse_dates=["Month"])
DSPIC = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", index_col="DATE", parse_dates=["DATE"])
# time = pd.to_datetime(DSPIC["DATE"], infer_datetime=True)


# Adjust datasets
Google_amazon_US = Google_amazon_US[:-2]
# Create Moving Average model
DSPIC['MA_12'] = DSPIC["DSPIC96"].rolling(12).mean()
# Create Autoregressive model


# Visualise:
# Google trends: amazon: (United States)
plt.figure(1)
minor_locator = AutoMinorLocator(12)
Google_amazon_US["amazon: (United States)"].plot(figsize=(12,4)).xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("%")
plt.grid()
plt.legend()

# Real Disposable Personal Incom
plt.figure(2)
DSPIC[["DSPIC96","MA_12"]].plot(figsize=(12,4)).xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("$")
plt.grid()
plt.legend()

# Calculate error
DSPIC['P-P_MA'] = DSPIC["DSPIC96"]-DSPIC["MA_12"]
#DSPIC['P-P_AR'] = DSPIC["DSPIC96"]-DSPIC["AR_12"]
