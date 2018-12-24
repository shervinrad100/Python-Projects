import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as mdates


#1/1/07 till now monthly (per gram?)

gold = pd.read_csv("Gold.csv")
brent = pd.read_csv("brent-month_csv.csv")
dollar = pd.read_csv("USDX.csv")
dates = mdates.num2date(mdates.datestr2num(gold['date']))
Gold = gold['price']
Brent = brent['Brent Spot Price']
Dollar = dollar['Price']

fig, ax1 = plt.subplots()
ax1.plot(dates, Gold, 'y')
ax1.set_ylabel('Gold (yellow)')
ax2 = ax1.twinx()
ax2.plot(dates, Brent, 'k')
ax2.set_ylabel('Brent (Black)')
fig.autofmt_xdate()
plt.grid(True)

fig, ax1 = plt.subplots()
ax1.plot(dates, Dollar, 'r')
ax1.set_ylabel('Dollar (red)')
ax2 = ax1.twinx()
ax2.plot(dates, Brent, 'k')
ax2.set_ylabel('Brent (Black)')
fig.autofmt_xdate()
plt.grid(True)

fig, ax1 = plt.subplots()
ax1.plot(dates, Dollar, 'r')
ax1.set_ylabel('Dollar (red)')
ax2 = ax1.twinx()
ax2.plot(dates, Gold, 'y')
ax2.set_ylabel('Gold (yellow)')
fig.autofmt_xdate()
plt.grid(True)

GoldBrent07_12 = np.corrcoef(Gold[0:84],Brent[0:84]) #From 07 to 12
GoldBrent15_18 = np.corrcoef(Gold[96:],Brent[96:]) #From 15 to 18

print('GoldBrent07_12', GoldBrent07_12[0][1])
print('GoldBrent15_18', GoldBrent15_18[0][1])
print('overall GoldBrent', np.corrcoef(Gold,Brent)[0][1])

DollarBrent09_15 = np.corrcoef(Dollar[43:115],Brent[24:96])
DollarBrent15_18 = np.corrcoef(Dollar[0:43],Brent[96:-1]) 
# Dollar has one month less than Brent (dimension error) so use -1
print('DollarBrent09_15', DollarBrent09_15[0][1])
print('DollarBrent15_18', DollarBrent15_18[0][1])
print('overall GoldBrent', np.corrcoef(Dollar,Brent)[0][1])