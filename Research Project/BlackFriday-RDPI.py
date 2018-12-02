import numpy as np
import matplotlib.dates as mdates


Google_amazon_US = np.genfromtxt("Amazon-2004-1_Present-mon-US(Grab-30-11-18).csv", delimiter=',')
del(Google_amazon_US[0:])
dates = mdates.num2date(mdates.datestr2num(Google_amazon_US[:][:0]))
