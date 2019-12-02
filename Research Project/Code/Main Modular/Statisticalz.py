# "stats tests"

from scipy.signal import correlate
from statsmodels.tsa.stattools import adfuller, pacf, acf
from scipy.stats import shapiro, probplot, norm # shapiro wilk test for normality sample size thousands or fewer
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def boxcox_optimise(data, Title=""):
    print(Title)
    print("No transform QQ correlation:",round(probplot(data, rvalue=True)[-1][-1],3) )
    for lambd in range(-5,6):
        if lambd != 0:
            transform = data**lambd
        else:
            transform = np.log(data)
        print(f"lambda={lambd} QQ correlation",round(probplot(transform, rvalue=True)[-1][-1],3))
        
        
   
        
def acfpacf(data, Title):
    fig, axes = plt.subplots(1,2, figsize=[15,5])
    plt.suptitle(Title)
    plot_acf(data, ax=axes[0])
    axes[0].set(xlabel="Lag", ylabel="ACF")
    axes[0].text(0.8, -0.3,"95% confidence interval")
    
    plot_pacf(data, ax=axes[1], method="ywmle", lags=44)
    axes[1].set(xlabel="Lag", ylabel="PACF")
    axes[1].text(0.8, -0.2,"95% confidence interval")
    
    
def ADF(array):
    ''' check for unit root errors in dataset'''
    result = adfuller(array)
    print('ADF t-Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))
    if result[1] >= 0.05:
        rej = False
    else:
        rej = True
    print("reject H_0:", rej)
    
    
    
def CF_student_t(data, ACF=False):
    if ACF == False:
        CF = pacf(data, nlags=len(data), method="ywmle")
    else:
        CF = acf(data, nlags=len(data))

    mu = CF.mean()
    std = CF.std()

    t_stat = []
    for i in range(len(CF)):
        rho = CF[i]
        nom = (rho*np.sqrt(len(CF)-2))
        denom = (np.sqrt(1-rho**2))
        
        if denom == 0:
            pass
        else:
            t_stat.append(nom/denom)
    counter = 0
    for t in t_stat:
        if t<4.86:
            counter+=1
        else:
            pass
    print(f"{counter} lags are significant")
    
    


# Levene test (null says equal variance) cant use because data is not normal
# from scipy.stats import levene

# which function to use in the test
# ‘median’ : Recommended for skewed (non-normal) distributions>
# ‘mean’ : Recommended for symmetric, moderate-tailed distributions.
# ‘trimmed’ : Recommended for heavy-tailed distributions.
# def lev(data):
#     Levene = levene(data[len(data)//2:], data[:len(data//2)], center="trimmed")
#     print("Levene Test:")
#     print("\tstatistic=", Levene[0])
#     print("\tp-value=", Levene[1])
#     # with alpha = 0.05, if F>1.9855 regect null (sigma_1=sigma_2=...=sigma_p)
#     if Levene[1] <= 0.5:
#         rej = True
#     else:
#         rej = False
#     print("reject H_0:", rej)
    
# lev(GGL.diff(1).dropna())
# lev(SP.diff(1).dropna())
# lev(DJI.diff(1).dropna())

#Breusch Pagan Test
# from statsmodels.stats.diagnostic import het_breuschpagan
# from statsmodels.formula.api import ols



#Score Test

# F-test

    
