import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

# Import data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"
Google_amazon_US = pd.read_csv("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv", index_col="Month", parse_dates=["Month"])
DSPIC = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", parse_dates=["DATE"])
# Adjust datasets
Google_amazon_US = Google_amazon_US[:-2]



# Create Moving Average model
DSPIC['MA_12'] = DSPIC["DSPIC96"].rolling(12).mean()
# Create Autoregressive model


# Visualise:
# Google trends: amazon: (United States)
plt.figure()
minor_locator = AutoMinorLocator(12)
Google_amazon_US["amazon: (United States)"].plot(figsize=(12,4)).xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("%")
plt.grid()
plt.legend()

# Real Disposable Personal Incom
plt.figure()
DSPIC[["DSPIC96","MA_12"]].plot(figsize=(12,4)).xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("$")
plt.grid()
plt.legend()

# Calculate error
DSPIC['e_MA'] = DSPIC["DSPIC96"]-DSPIC["MA_12"]
#DSPIC['e_AR'] = DSPIC["DSPIC96"]-DSPIC["AR_12"]


# Check for stationarity in errors
plt.figure()
DSPIC['e_MA'].hist()
plt.grid()
plt.title("Error point Histogram")
#DSPIC['e_mu'] = DSPIC['e_MA'].mean()*np.ones(len(DSPIC))
split = len(DSPIC)/2
half1, half2 = DSPIC.iloc[:split] , DSPIC.iloc[split:]
mu1, mu2 = half1.loc["e_MA"].mean(), half2.loc["e_MA"].mean() # gettign errors here



plt.figure()
DSPIC["e_MA"].plot()
DSPIC["<e_MA>"] = np.ones(len(DSPIC))*DSPIC["e_MA"].mean()
DSPIC["<e_MA>"].plot().xaxis.set_minor_locator(minor_locator)
plt.ylim([-550,550])
plt.xlabel("Year")
plt.grid()
plt.legend()
plt.text(0.1, -500, r'$\mu =121.06$')

DSPIC["(e_MA)-<e_MA>"]=DSPIC["e_MA"]-DSPIC["<e_MA>"]
DSPIC["(e_MA)-<e_MA>"].mean()

