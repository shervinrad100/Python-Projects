import ref_data as rd
import edgar_sentiment_wordcount as esw
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd
import scipy.stats as ss


prices = rd.get_yahoo_data('2000-01-01', '2000-01-12', 'MMM')
dates = prices.index
close = prices['adjclose']

fig = plt.plot(dates,close)
plt.xlim(datetime.strptime('2000-01-01','%Y-%m-%d'), datetime.strptime('2000-01-13','%Y-%m-%d'))
plt.show()

