import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator # for time series visualisation


# Import data
#PATH = r"C:\Users\sherv\OneDrive\Documents\GitHub\Python - Projects\Research Project\Data"    
data = {"google":["multiTimeline.csv", "Month"], 
        "RDPI":  ["RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", "DATE"], 
        "CPI":   ["CPI.csv", "DATE"],
        "GDP":   ["GDP.csv", "DATE"], 
        "UE":    ["Unemployment_2004_Present_US(Grab-5-12-18).csv", "DATE"], 
        "SP500": ["S&P500.csv", "Date"], 
        "IR":    ["InterestRate_2004-1-1_Present_US(Grab-5-12-18).csv", "DATE"], 
        "PPI":   ["PPIACO.csv", "DATE"],
        "PMI":   ["ISM-MAN_PMI.csv", "Date"]}
'''
def importdata(key, path ,parseCol):
    key = pd.read_csv("%s" %(path), index_col="%s" %(parseCol), parse_dates=["%s" %(parseCol)])
    key = key.loc["2004-01-01":"2018-09-01"]

for dataset in data.keys():
    importdata(dataset, data[dataset][0], data[dataset][0])  
'''

google = pd.read_csv("multiTimeline.csv", index_col="Month", parse_dates=["Month"])
RDPI = pd.read_csv("RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv", index_col="DATE" ,parse_dates=["DATE"])
CPI = pd.read_csv("CPI.csv", index_col="DATE" , parse_dates=["DATE"])
GDP = pd.read_csv("GDP.csv", index_col="DATE" , parse_dates=["DATE"])
UE = pd.read_csv("Unemployment_2004_Present_US(Grab-5-12-18).csv", index_col="DATE", parse_dates=["DATE"])
SP500 = pd.read_csv("S&P500.csv", index_col="Date", parse_dates=["Date"])
IR = pd.read_csv("InterestRate_2004-1-1_Present_US(Grab-5-12-18).csv", index_col="DATE", parse_dates=["DATE"])
PPI = pd.read_csv("PPIACO.csv", index_col="DATE", parse_dates=["DATE"])
PMI = pd.read_csv("ISM-MAN_PMI.csv", index_col="Date", parse_dates=["Date"])
DJI = pd.read_csv("DJI.csv", index_col="Date", parse_dates=["Date"])

# Check for unit root ADF test
from statsmodels.tsa.stattools import adfuller
def rootTest(dataset):
    result = adfuller(dataset)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
    	print('\t%s: %.3f' % (key, value))
# implement for loop?
print("goolge:")
rootTest(google["Top5"])
print("RDPI:")
rootTest(RDPI["DSPIC96"])
print("CPI:")
rootTest(CPI["CPI"])
print("SP500:")
rootTest(SP500["Close"])


# Autocorrelation?
from statsmodels.graphics.tsaplots import plot_acf
plot_acf(RDPI["DSPIC96"])
plt.grid()
plot_acf(CPI["CPI"])
plt.grid()
print("len(SP500):", len(SP500))
plot_acf(SP500["Close"])
plt.grid()

# for loop?
# adjust data
google = google.loc["2004-01-01":"2018-09-01"]
CPI = CPI.loc["2004-01-01":"2018-09-01"]
GDP = GDP.loc["2004-01-01":"2018-09-01"]
RDPI = RDPI.loc["2004-01-01":"2018-09-01"]
UE = UE.loc["2004-01-01":"2018-09-01"]
SP500 = SP500.loc["2004-01-01":"2018-09-01"]
IR = IR.loc["2004-01-01":"2018-09-01"]
PPI = PPI.loc["2004-01-01":"2018-09-01"]
PMI = PMI.loc["2004-01-01":"2018-09-01"]
DJI = DJI.loc["2004-01-01":"2018-09-01"]



# Visualise
minor_locator = AutoMinorLocator(12)
# Investigating overall trendSS
def google_v_X(Data_col, yName, title):
    if title == False:
        title =yName
    fig, ax1 = plt.subplots()
    google["Top5"].plot(ax=ax1,color='b').xaxis.set_minor_locator(minor_locator)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('google (%)', color='b')
    ax1.tick_params('y', colors='b')
    plt.grid()
    ax2 = ax1.twinx()
    Data_col.plot(ax=ax2,color='r')
    ax2.set_ylabel('%s' %(yName), color='r')
    ax2.tick_params('%s' %(yName), colors='r')
    plt.title("Google vs %s trends" %(title))

# implement for loop
    # Google-CPI
google_v_X(CPI["CPI"], "CPI 1982-1985=100 (%)", "CPI")

    # Google-RDPI
google_v_X(RDPI["DSPIC96"], "RDPI ($)", "RDPI")

    # Google-GDP
google_v_X(GDP["GDP"], "GDP (B$)", "GDP")

    # Google-UE
google_v_X(UE["Value"], "Unemployed persons", "Unemployment")

    # Google-SP500
google_v_X(SP500["Close"], "SP500","")

    # Google-PPI
google_v_X(PPI["PPI"], "PPI","")

    # Google-PMI
#google_v_X(PMI["PMI"], "PMI","")

    # Google-IR
google_v_X(IR["FEDFUNDS"], "Fed Funds Rate (%)", "Interest Rate")

    #Google-DJI
google_v_X(DJI["Close"], "DJI","" )