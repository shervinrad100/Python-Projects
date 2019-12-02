# " plotting functions "
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator 
from Statisticalz import *

minor_locator = AutoMinorLocator(12)

# for key in data.keys():
#     fig, ax1 = plt.subplots()
#     data[key][meta[key][2]].plot(ax=ax1,color='k').xaxis.set_minor_locator(minor_locator)
#     ax1.set_xlabel('Date')
#     ax1.set_ylabel(f"{key} index", color='k')
#     plt.grid()
#     Title = f"{key}"
#     plt.title(Title)
# #    plt.savefig("%s\%s.png" %(save_PATH, Title))

def boxcox(data, Title=""):
    fig, ax = plt.subplots(2,2, figsize=[15,12])
    fig.suptitle(Title, fontsize=20)
    np.log(data).diff(1).hist(ax=ax[0,0])
    ax[0,0].set(ylabel="Frequency", xlabel="Returns")
    probplot(np.log(data).diff(1).dropna(),plot=ax[0,1], rvalue=True);
    fig.text(0.5,0.5,"No Transform", ha="center", va="center", fontsize=16)
    fig.text(0.5,0.9,"Log Transformed", ha="center", va="center", fontsize=16)
    data.diff(1).hist(ax=ax[1,0])
    ax[1,0].set(ylabel="Frequency", xlabel="Returns")
    probplot(data.diff(1).dropna(),plot=ax[1,1], rvalue=True);
    
    
    
def seasonality_check(DF, Title, key=None, array=None, ):
    """
    data must not include incomplete years. 
    """
    if key and array: #check this line later
        df = data[key][array]
    else:
        df = DF
    mm = [M for M in range(1,13)]
    df_by_month = {}
    for M in mm:
        val = []
        for year in range(len(df)//12):
            val.append(df.iloc[year*12+M-1])
        df_by_month[M] = val
    df_by_month = pd.DataFrame.from_dict(df_by_month)    
    
    fig, axes = plt.subplots(1,2, figsize=(15,5))   
    fig.suptitle("Concatenated Data per Month")
    df_by_month.plot(ax=axes[0], kind="box" , color="k")
    (df_by_month.var()/df_by_month.var().max()).plot(ax=axes[1], kind="bar", grid=True, color="k") # is this normalisation correct?
    axes[0].set(ylabel=f"{Title}", xlabel="Month index")
    axes[1].set(xlabel="Month index", ylabel="Variance % of var().max()")
    return df_by_month



def diff_plots(diff1, diff2, Title="", Title1="Log Seasonally differenced:  D_12=1, d=0", Title2="Log differenced trend:   D_12=1, d=1", lag=40, txt=True, savefig=False):
    fig, axes = plt.subplots(3,2, figsize=[15,10])
    fig.suptitle(Title)
    diff1.plot(ax=axes[0,0], grid=True, title=Title1)
    plot_acf(diff1, ax=axes[1,0], title="", lags=lag);
    axes[1,0].set(ylabel="ACF")
    temp = pacf(GGL_log_diff, nlags=100).max()
    
    # following block doesnt work
    if temp <= 1 and txt==False:
        plot_pacf(diff1, method="ywunbiased", ax=axes[2,0], title="", lags=lag);
        axes[2,0].set(ylabel="PACF", xlabel="Lag")
    elif txt==True:
        axes[2,0].text(.5,.5,"Non-stationary",horizontalalignment='center', verticalalignment='center', fontsize=20)
        axes[2, 0].xaxis.set_ticklabels([])
        axes[2, 0].yaxis.set_ticklabels([])
    else:
        pass
    
    diff2.plot(ax=axes[0,1], grid=True, title=Title2)
    plot_acf(diff2, ax=axes[1,1], title="", lags=lag);
    axes[1,1].set(ylabel="ACF")
    plot_pacf(diff2, method="ywunbiased", ax=axes[2,1], title="", lags=lag);
    axes[2,1].set(ylabel="PACF", xlabel="Lag")
    
    if savefig==True:
        fig.savefig("%s\%s.png" %(save_PATH, Title))
    else: pass



def coolplot(data, supTitle, Title="", pacfmethod="ywunbiased", savefig=False):
    fig = plt.figure(figsize=[15,10])
    fig.suptitle(supTitle)
    grid = plt.GridSpec(3,2,wspace=0.3, hspace=0.4)
    
    ax1 = plt.subplot(grid[0,0])
    data.plot(ax=ax1, grid=True)
    ax1.set(title=Title)
    plt.hlines(y=data.mean(), xmin="2009-01-01", xmax="2018-12-01", color="r")
    
    ax2 = plt.subplot(grid[1,0])
    plot_acf(data, ax=ax2, lags=40)
    ax2.set(ylabel="ACF", xlabel="Lag")
    
    ax3 = plt.subplot(grid[1,1])
    plot_pacf(data, ax=ax3, method=pacfmethod, lags=39)
    ax3.set(ylabel="PACF", xlabel="Lag")
    
    ax4 = plt.subplot(grid[0,1])
    (data**2).plot(title=f"{Title} squared returns", grid=True, ax=ax4)
    
    ax5 = plt.subplot(grid[2,0])
    data.plot(kind="hist", ax=ax5)
    ax5.set(xlabel="returns")
#     x = np.linspace(data.min(), data.max(),num=100)
#     plt.plot(x, norm.pdf(x, 1, np.sqrt(1)),color="r")

    
    ax6 = plt.subplot(grid[2,1])
    probplot(data, plot=ax6, rvalue=True)
    ax6.set(title="QQ plot")
    ax6.grid()
    
    stat, p = shapiro(data)
    if p >= 0.05:
        print(" \t %s Normally distributed" %(supTitle))
    else:
        print(" \t %s Not normally distributed" %(supTitle))
        
    print("\n \t Shapiro t-Statistics: %.3f \n \t p-value: %.3f" %(stat, p))

    
    if savefig==True:
        fig.savefig("%s\%s.png" %(save_PATH, Title))
    else: pass
    

def forcplot(modelfit, data=None, horizon=12, Start="2015-01-01", Label=""):
    forc = modelfit.get_forecast(horizon)
    pred = modelfit.get_prediction(start=Start)
    
    pred_low_conf_int,pred_up_conf_int = pred.conf_int().iloc[:,0],pred.conf_int().iloc[:,1]
    forc_low_conf_int,forc_up_conf_int = forc.conf_int().iloc[:,0],forc.conf_int().iloc[:,1]

    lower = pd.concat([pred_low_conf_int, forc_low_conf_int])
    upper = pd.concat([pred_up_conf_int, forc_up_conf_int])
    
    fig, ax = plt.subplots()
    data.loc[Start:].plot(ax=ax, label="observation", color="k")
    np.exp(pred.predicted_mean).plot(ax=ax, label=f"{Label} (In Sample)", color="c")
    xs = lower.keys()
    ax.fill_between(xs,np.exp(lower), np.exp(upper), color="0.9", label="95% confidence interval")
    np.exp(forc.predicted_mean).plot(ax=ax, label=f"{Label}", color="r")
    plt.grid()
    plt.ylabel("Index value")
    plt.legend()
    
    
def var_growth_check(df):
    df_years = {}
    mm = [M for M in range(12)]
    for year in range(len(df)//12):
        val = []
        for M in mm:
            val.append(df.iloc[year*12+M])
        df_years[year] = val
    df_years = pd.DataFrame.from_dict(df_years)
    return df_years


def residualplot(model, data, horizon=12, Start="2015-01-01", Label=""):
    pred = model.get_prediction(start=Start).predicted_mean
    
    fig = plt.figure(figsize=[8,6])
    plt.suptitle(Label)
    grid = plt.GridSpec(2,1,wspace=0.3, hspace=0.5)
    ax1 = plt.subplot(grid[0,0])
    ax1.set(ylabel="Residuals")
    ax1.grid()
    xs = pred.keys()
    ax1.scatter(xs,data.loc[Start:]-np.exp(pred))
    ax1.vlines(xs, 0, data.loc[Start:]-np.exp(pred))

    ax2 = plt.subplot(grid[1,0])
    plot_acf(pred, ax=ax2);
    ax2.set(ylabel="ACF")
    
    
def forecastplot(data1,forecasts):
    fig, axes = plt.subplots()
    data1.loc["2016-06-01":].plot(ax=axes, label="SP500")
    forecasts.plot(ax=axes, label="forecast")
    axes.legend()
    axes.grid()
    

