import requests,json,csv,os,glob,re,string, csv
from yahoofinancials import YahooFinancials
from pandas_datareader import data
from datetime import timedelta,datetime
import pandas as pd
from bs4 import BeautifulSoup

def get_sp100():
    data = []
    r = requests.get('https://en.wikipedia.org/wiki/S%26P_100')
    soup = BeautifulSoup(r.content,'html.parser')
    table = soup.find('table', attrs={'id':'constituents'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols!=[]:
            cols = cols[0]
            data.append(cols)
        else:
            pass
    return data

def get_yahoo_data(start_date, end_date, ticker):
    extended_date = datetime.strptime(end_date,'%Y-%m-%d')+timedelta(days=20)
    extended_date = extended_date.strftime('%Y-%m-%d')
    ticker_data = YahooFinancials(ticker).get_historical_price_data(start_date, extended_date, 'daily')
    prices = pd.DataFrame(ticker_data[ticker]['prices'])
    prices['formatted_date'] = pd.to_datetime(prices['formatted_date'])
    prices.set_index('formatted_date', inplace=True)
    prices = prices.drop(columns='date')
    prices['1d returns'] = prices['close'].pct_change().shift(-1)
    prices['2d returns'] = prices['close'].pct_change(periods=2).shift(-2)
    prices['3d returns'] = prices['close'].pct_change(periods=3).shift(-3)
    prices['5d returns'] = prices['close'].pct_change(periods=5).shift(-5)
    prices['10d returns'] = prices['close'].pct_change(periods=10).shift(-10)
    prices['Symbol'] = ticker
    prices = prices[prices.index <= end_date]
    return prices

def get_sentiment_word_dict(file_path):
    master_dictionary = {}
    sentiment_categories = ['negative', 'positive', 'uncertainty', 'litigious', 'constraining',
                             'superfluous', 'interesting','modal']
    
    with open(file_path) as f:
        md_header = f.readline()
        for line in f:
            cols = line.split(',')
            master_dictionary[cols[0]] = MasterDictionary(cols)
    
    sentiment_dictionary = {}
    for category in sentiment_categories:
        sentiment_dictionary[category] = {}

    # Create dictionary of sentiment dictionaries with count set = 0
    for word in master_dictionary.keys():
        for category in sentiment_categories:
            if master_dictionary[word].sentiment[category]:
                sentiment_dictionary[category][word] = 0

    return sentiment_dictionary,master_dictionary

class MasterDictionary:
    def __init__(self, cols):

        self.negative = int(cols[7])
        self.positive = int(cols[8])
        self.uncertainty = int(cols[9])
        self.litigious = int(cols[10])
        self.constraining = int(cols[11])
        self.superfluous = int(cols[12])
        self.interesting = int(cols[13])
        self.modal = int(cols[14])

        self.sentiment = {}
        self.sentiment['negative'] = bool(self.negative)
        self.sentiment['positive'] = bool(self.positive)
        self.sentiment['uncertainty'] = bool(self.uncertainty)
        self.sentiment['litigious'] = bool(self.litigious)
        self.sentiment['constraining'] = bool(self.constraining)
        self.sentiment['superfluous'] = bool(self.superfluous)
        self.sentiment['interesting'] = bool(self.interesting)
        self.sentiment['modal'] = bool(self.modal)    