## TODO: check MSE bias
## TODO: find break points
## TODO: merge garch-var 

from DataManipulation import * 
from Plotters import *
from Statisticalz import *

# from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.statespace.varmax import VARMAX, VARMAXResults
from arch import arch_model


import_PATH = r"E:\GitHub\Python-Projects\Research Project\Data"

meta = {# dataset: [path, Date_col, Value_col]
        "Google":[f"{import_PATH}\multiTimeline.csv", "Month", "Top5"], 
        "SP500": [f"{import_PATH}\S&P500.csv", "Date", "Close"]
}

data ={}
for key in meta.keys():
    data[key] = importdata(key, meta[key][0], meta[key][1])
    
SP = data["SP500"]["Close"].loc["2009-01-01":"2018-12-01"]
GGL = data["Google"][meta["Google"][2]].loc["2009-01-01":"2018-12-01"]


# VAR data vector
VAR_GGL_SP = pd.DataFrame()
VAR_GGL_SP["SP"] = np.log(SP[:round(len(SP)*0.95)])
VAR_GGL_SP["GGL"] = np.log(GGL[:round(len(SP)*0.95)]) 

var_model6_12 = VARMAX(VAR_GGL_SP.loc["2009-06-01":], order=(6,12)).fit()
forc = var_model6_12.get_forecast(12)
pred = var_model6_12.get_prediction(start="2015-01-01")

fig, ax = plt.subplots()
plt.title("SP500-GGL")

pred_low_conf_int, pred_up_conf_int = pred.conf_int().iloc[:,0], pred.conf_int().iloc[:,2]
forc_low_conf_int, forc_up_conf_int = forc.conf_int().iloc[:,0], forc.conf_int().iloc[:,2]

lower = pd.concat([pred_low_conf_int, forc_low_conf_int])
upper = pd.concat([pred_up_conf_int, forc_up_conf_int])

xs = lower.keys()
np.exp(forc.predicted_mean)["SP"].plot(label="VAR(6,12)", color="r", ax=ax)
ax.fill_between(xs,np.exp(lower),np.exp(upper), color="0.85", label="95% confidence interval")
np.exp(pred.predicted_mean["SP"]).plot(ax=ax,label="VAR(6,12) (In sample)", color="y")
SP.loc["2015-01-01":].plot(label="Observations", color="k",ax=ax)
plt.grid()
plt.legend()



fig, ax = plt.subplots()
arch_model(SP, vol="GARCH", p=1, q=1).fit().conditional_volatility.loc["2015-01-01":].plot(ax=ax,title="Conditional variance SP500")
ax.set(xlabel="Date",ylabel="Variance")
plt.grid()



