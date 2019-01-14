# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 01:25:41 2019

@author: sherv
"""

from pandas import Series
from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf
series = Series.from_csv('RealDisposableIncome-2004-1_Present-Mon-US(Grab-30-11-18).csv', header=0)
plot_acf(series)
pyplot.show()