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

def Compare(df_1, yName1, df_2, yName2, Title):
    r_squared = data[key][meta[key][2]].corr(data["google"]["Top5"])
    fig, ax1 = plt.subplots()
    df_1.plot(ax=ax1,color='b').xaxis.set_minor_locator(minor_locator)
    ax1.set_xlabel('Date')
    ax1.set_ylabel(yName1, color='b')
    ax1.tick_params('y', colors='b')
    plt.grid()
    plt.text("2005-01-01", 100, r"$r^2=$ "+"%.2f" %(r_squared))
    ax2 = ax1.twinx()
    df_2.plot(ax=ax2,color='r')
    ax2.set_ylabel(yName2, color='r')
    ax2.tick_params('y', colors='r')
    plt.title(Title)
    plt.savefig("%s\%s.png" %(PATH, Title))

def plot_regressors(key, lag, Title, central="true"):
    fig, axes = plt.subplots()
    data[key][meta[key][2]].plot(ax=axes).xaxis.set_minor_locator(minor_locator)
    if central == "both":
        for i in lag:
            data[key][["MA_%s" %(i), "MAc_%s" %(i)]].plot(ax = axes)
    elif central == "false":
        for i in lag:
            data[key][["MA_%s" %(i)]].plot(ax = axes)
    elif central == "true":
        for i in lag:
            data[key][["MAc_%s" %(i)]].plot(ax = axes)
    plt.xlabel("Year")
    plt.ylabel(meta[key][2])
    plt.grid()
    plt.legend()
    plt.title(Title)
    plt.savefig("%s\%s.png" %(PATH, Title))
    
    
def plot_residuals(key, lag, Title, central="both"):
    std={}
    mu ={}
    for i in lag:
        if central == "both":
            std["ec%s" %(i)] = "%.2f" %(data[key]["ec(%s)" %(i)].std())
            std["e%s" %(i)] = "%.2f" %(data[key]["e(%s)" %(i)].std())
            mu["ec%s" %(i)] = "%.2f" %(data[key]["ec(%s)" %(i)].mean())
            mu["e%s" %(i)] = "%.2f" %(data[key]["e(%s)" %(i)].mean())
        elif central == "true":
            std["ec%s" %(i)] = "%.2f" %(data[key]["ec(%s)" %(i)].std())
            mu["ec%s" %(i)] = "%.2f" %(data[key]["ec(%s)" %(i)].mean())
        elif central == "false":
            std["e%s" %(i)] = "%.2f" %(data[key]["e(%s)" %(i)].std())
            mu["e%s" %(i)] = "%.2f" %(data[key]["e(%s)" %(i)].mean())
    fig, axes = plt.subplots()
    if central == "both":
        for i in lag:
            data[key][["e(%s)" %(i), "ec(%s)" %(i)]].plot(ax = axes).xaxis.set_minor_locator(minor_locator)
            yax = data[key][["e(%s)" %(i), "ec(%s)" %(i)]].max() 
            scale = yax //6
            plt.text("2019-02-01",yax - scale,r"$\sigma_{c}^2=$ "+std["ec%s" %(i)])
            plt.text("2019-02-01",yax - 2*scale,r"$\mu_{c}^2=$ "+mu["ec%s" %(i)])
            plt.text("2019-02-01",yax - 3*scale,r"$\sigma^2=$ "+std["e%s" %(i)])
            plt.text("2019-02-01",yax - 4*scale,r"$\mu^2=$ "+mu["e%s" %(i)])
    elif central == "false":
        for i in lag:
            data[key][["e(%s)" %(i)]].plot(ax = axes).xaxis.set_minor_locator(minor_locator)
    elif central == "true":
        for i in lag:
            data[key][["ec(%s)" %(i)]].plot(ax = axes).xaxis.set_minor_locator(minor_locator)    
    plt.xlabel("Year")
    plt.grid()
    plt.legend()
    plt.title(Title)
    plt.savefig("%s\%s.png" %(PATH, Title))
    
def plot_ACF(key, array, Title):
    plt.figure()
    autocorrelation_plot(data[key][array].dropna())
    plt.title(Title)
    plt.savefig("%s\%s.png" %(PATH, Title))

def distribution(key, array, Title):
    for arrayName in array:
        plt.figure()
        data[key][arrayName].hist()   
        plt.title(Title)
        plt.savefig("%s\%s.png" %(PATH, Title))
    
def IID_test(key, array):
    Data = data[key][array].dropna()
    alpha = 0.05
    stat, p = shapiro(Data)
    plt.figure()
    probplot(Data, plot=plt, rvalue=True)
    plt.grid()
    Title = key+" "+array+" QQ-plot"
    plt.title(Title)
    plt.savefig("%s\%s.png" %(PATH, Title))
    print(key, "'%s'" %(array), "\n \t Test Statistics=%.3f, p=%.3f" %(stat, p))
    if p >= alpha:
        print(" \t %s Normally distributed" %(key+" "+"'%s'" %(array)))
    else:
        print(" \t %s Not normally distributed" %(key+" "+"'%s'" %(array)))


# Data
PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Plots"    
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

# Visualise
    # Overal trends
    Compare(data["google"][meta["google"][2]], "Google Trends (%)", data[key][meta[key][2]], key, "Google Trends v %s" %(key))
    # Index and regressor
    plot_regressors(key, [12,3], "12 and 3 forward rolling window MA- %s" %(key), central="false")
    plot_regressors(key, [3], "central and forward 3 rolling window MA- %s" %(key), central="both")
    # Autocorrelation
    plot_ACF(key, meta[key][2], "%s ACF" %(key))
    plot_ACF(key, "ec(3)", "ec(3) residual ACF- %s" %(key))
    plot_ACF(key, "R", "Return ACF- %s" %(key))
    # residual plots
#    plot_residuals(key, [3],  "%s residuals e(3), ec(3)" %(key), central="both")
#    plot_residuals(key, [12,3],  "%s residuals (central window) ec(3),ec(12)" %(key), central="true")
    distribution(key, ["ec(3)"], "ec(%i) Residual distribution: %s" %(3,key))
    distribution(key, ["R"], "Returns destribution: %s" %(key))
    # normality test
    print(key)
    print("\t ec(3) skew %.3f" %(data[key]["ec(3)"].skew()))
    print("\t ec(3) kurtosis %.3f" %(data[key]["ec(3)"].kurtosis()))
    IID_test(key, "ec(3)")
    IID_test(key, "R")


