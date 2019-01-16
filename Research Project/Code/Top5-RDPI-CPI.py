import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator # for time series visualisation

# Import data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"
google = pd.read_csv("Top5-aggregate.csv", index_col="Month", parse_dates=["Month"])
RDPI = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", parse_dates=["DATE"])
CPI = pd.read_csv("CPI.csv", parse_dates=["DATE"])

# adjust data
google = google[:-4]
CPI = CPI[:-3]

# Create Moving Average model
    # window 12
RDPI['MA_12'] = RDPI["DSPIC96"].rolling(12).mean()
CPI['MA_12'] = CPI["CPI"].rolling(12).mean()
    # window 6
RDPI['MA_6'] = RDPI["DSPIC96"].rolling(6).mean()
CPI['MA_6'] = CPI["CPI"].rolling(6).mean()
    # window 2
RDPI['MA_2'] = RDPI["DSPIC96"].rolling(2).mean()
CPI['MA_2'] = CPI["CPI"].rolling(2).mean()

# Regressor error
    # Moving average regressors
        # rolling 12
RDPI['e(MA_12)'] = RDPI["DSPIC96"]-RDPI["MA_12"]
CPI['e(MA_12)'] = CPI["CPI"] - CPI['MA_12']
        # rolling 6
RDPI['e(MA_6)'] = RDPI["DSPIC96"]-RDPI["MA_6"]
CPI['e(MA_6)'] = CPI["CPI"] - CPI['MA_6']
        # rolling 2
RDPI['e(MA_2)'] = RDPI["DSPIC96"]-RDPI["MA_2"]
CPI['e(MA_2)'] = CPI["CPI"] - CPI['MA_2']


# Autocorrelation Function






# Visualise
minor_locator = AutoMinorLocator(12)

# google
plt.figure()
google["Top5"].plot(figsize=(12,4)).xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("%")
plt.grid()
plt.legend()
plt.title("Top 5 searches retailers (Google Trend)")

# Real Disposable Personal Incom
plt.figure()
RDPI[["DSPIC96","MA_12", "MA_6", "MA_2"]].plot().xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("$")
plt.grid()
plt.legend()
plt.title("Real Disposable Income")
    # moving average errors
        # rolling 12
plt.figure()
RDPI['e(MA_12)'].plot()
plt.grid()
plt.legend()
plt.title("RDPI Moving average rolling 12 error")
        # rolling 6
plt.figure()
RDPI['e(MA_6)'].plot()
plt.grid()
plt.legend()
plt.title("RDPI Moving average rolling 6 error")

        # rolling 2
plt.figure()
RDPI['e(MA_2)'].plot()
plt.grid()
plt.legend()
plt.title("RDPI Moving average rolling 2 error")


# Consumer Price Index
plt.figure()
CPI[["CPI","MA_12", "MA_6", "MA_2"]].plot().xaxis.set_minor_locator(minor_locator)
plt.xlabel("Year")
plt.ylabel("%")
plt.grid()
plt.legend()
plt.title("Consumer Price Index (1982-1985=100)")
    # moving average errors
        # rolling 12
plt.figure()
CPI['e(MA_12)'].plot()
plt.grid()
plt.legend()
plt.title("CPI Moving average rolling 12 error")
    # moving average errors
        # rolling 6
plt.figure()
CPI['e(MA_6)'].plot()
plt.grid()
plt.legend()
plt.title("CPI Moving average rolling 6 error")
    # moving average errors
        # rolling 2
plt.figure()
CPI['e(MA_2)'].plot()
plt.grid()
plt.legend()
plt.title("CPI Moving average rolling 2 error")