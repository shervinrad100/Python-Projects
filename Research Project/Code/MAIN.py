import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator # for time series visualisation
from statsmodels.tsa.stattools import adfuller
#from statsmodels.graphics.tsaplots import plot_acf
from pandas.plotting import autocorrelation_plot
from scipy.stats import shapiro # shapiro wilk test for normality sample size thousands or fewer
from scipy.stats import probplot


# Functions 
def importdata(key, path ,parseCol):
    ''' import data, parse and equalise length '''
    dataset = pd.read_csv("%s" %(path), index_col="%s" %(parseCol), parse_dates=["%s" %(parseCol)])
    dataset = dataset.loc["2004-01-01":"2018-09-01"]
    return dataset

def UnitRootTest(array):
    ''' check for unit root errors in dataset'''
    result = adfuller(array)
    print('ADF t-Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))
        
def MA_forward(df_in, window):
    return df_in.rolling(window).mean()

def MA_central(df_in, window):
        return df_in.rolling(window, center=True).mean()

def Compare(df_1, yName1, df_2, yName2, title):
    fig, ax1 = plt.subplots()
    df_1.plot(ax=ax1,color='b').xaxis.set_minor_locator(minor_locator)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(yName1, color='b')
    ax1.tick_params('y', colors='b')
    plt.grid()
    ax2 = ax1.twinx()
    df_2.plot(ax=ax2,color='r')
    ax2.set_ylabel(yName2, color='r')
    ax2.tick_params('y', colors='r')
    plt.title(title)

def plot_regressors(key, yName, Title):
    plt.figure()
    data[key][[meta[key][2], "MA_12", "MA_6", "MA_3"]].plot().xaxis.set_minor_locator(minor_locator)
    plt.xlabel("Year")
    plt.ylabel(yName)
    plt.grid()
    plt.legend()
    plt.title(Title)
    
def plot_residuals(key, Title):
    plt.figure()
    data[key][["e(12)", "ec(12)"]].plot().xaxis.set_minor_locator(minor_locator)
    plt.xlabel("Year")
    plt.grid()
    plt.legend()
    plt.title(Title)
    
def plot_ACF(key, array, Title):
    plt.figure()
    autocorrelation_plot(data[key][array].dropna())
    plt.title(Title)

def distribution(key, arrayName, Title):
    plt.figure()
    data[key][arrayName].hist()   
    plt.title(Title)
    
def IID_test(key, array):
    Data = data[key][array].dropna()
    alpha = 0.05
    stat, p = shapiro(Data)
    plt.figure()
    probplot(data[key][array].dropna(), plot=plt, rvalue=True)
    plt.title(key+" "+array)
    print(key, "'%s'" %(array), '\n \t Test Statistics=%.3f, p=%.3f' % (stat, p))
    if p >= alpha:
        print(" \t %s Normally distributed" %(key+" "+"'%s'" %(array)))
    else:
        print(" \t %s Not normally distributed" %(key+" "+"'%s'" %(array)))


# Data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"    
meta = {# dataset: [path, Date_col, Value_col]
        "google":["multiTimeline.csv", "Month", "Top5"], 
        "RDPI":  ["RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", "DATE", "DSPIC96"], 
        "CPI":   ["CPI.csv", "DATE", "CPI"],
        "GDP":   ["GDP.csv", "DATE", "GDP"], 
        "UE":    ["Unemployment_2004_Present_US(Grab-5-12-18).csv", "DATE", "Value"], 
        "SP500": ["S&P500.csv", "Date", "Close"], 
        "IR":    ["InterestRate_2004-1-1_Present_US(Grab-5-12-18).csv", "DATE", "FEDFUNDS"], 
        "PPI":   ["PPIACO.csv", "DATE", "PPI"],
        "PMI":   ["ISM-MAN_PMI.csv", "Date", "PMI"],
        "DJI":   ["DJI.csv", "Date", "Close"]} 

data ={}

# Visualise
minor_locator = AutoMinorLocator(12)

for key in meta.keys():
# Import data
    data[key] = importdata(key, meta[key][0], meta[key][1])
    
# Calculate Returns
    data[key]["R"] = data[key][meta[key][2]].shift(1) / data[key][meta[key][2]] -1
    
'''
# Check for unit root ADF test
    print("%s: " %(key))
    UnitRootTest(data[key][meta[key][2]])
    print("%s First difference (R):" %(key))
    UnitRootTest(data[key]["R"][1:])
'''

for key in meta.keys():
# Moving averages
    data[key]["MA_12"] = MA_forward(data[key][meta[key][2]], 12)
    data[key]["MA_6"] = MA_forward(data[key][meta[key][2]], 6)
    data[key]["MA_3"] = MA_forward(data[key][meta[key][2]], 3)
    data[key]["MAc_12"] = MA_central(data[key][meta[key][2]], 12)
    data[key]["MAc_6"] = MA_central(data[key][meta[key][2]], 6)
    data[key]["MAc_3"] = MA_central(data[key][meta[key][2]], 3)
    
# residuals
    data[key]["e(12)"] = data[key][meta[key][2]] - data[key]["MA_12"]
    data[key]["e(6)"] = data[key][meta[key][2]] - data[key]["MA_6"]
    data[key]["e(3)"] = data[key][meta[key][2]] - data[key]["MA_3"]
    data[key]["ec(12)"] = data[key][meta[key][2]] - data[key]["MAc_12"]
    data[key]["ec(6)"] = data[key][meta[key][2]] - data[key]["MAc_6"]
    data[key]["ec(3)"] = data[key][meta[key][2]] - data[key]["MAc_3"]
    # normality test
#    print(key)
#    print("\t ec(3) skew %.3f" %(data[key]["ec(3)"].skew()))
#    print("\t ec(3) kurtosis %.3f" %(data[key]["ec(3)"].kurtosis()))
#    IID_test(key, "ec(3)")
#    IID_test(key, "R")

# Visualise
    # Overal trends
#    Compare(data["google"][meta["google"][2]], "Google Trends (%)", data[key][meta[key][2]], "%s" %(key), "Google Trends v %s" %(meta[key][2]))
#    print("Corr(google, %s): " %(key), data[key][meta[key][2]].corr(data["google"]["Top5"]))
    # Index and regressor
#    plot_regressors(key, meta[key][2], key)
    # Autocorrelation
#    plot_ACF(key, meta[key][2], "%s ACF" %(key))
#    plot_ACF(key, "ec(3)", "residual ACF: %s" %(key))
    plot_ACF(key, "R", "residual ACF: %s" %(key))
    # residual plots
#    plot_residuals(key, "%s residuals" %(key))
#    distribution(key, "ec(12)", "ec(12) Residual distribution: %s" %(key))
#    distribution(key, "R", "Returns destribution: %s" %(key))


