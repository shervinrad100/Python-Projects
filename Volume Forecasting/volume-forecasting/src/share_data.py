# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 23:02:19 2021

@author: JamesOrwell
"""
import pandas as pd
import yfinance as yf
from datetime import timedelta, date, datetime
import os
import datetime as dt

def get_path():
    if not os.path.exists('dataset'):
        os.makedirs('dataset')
    cwd = os.getcwd()
    print('cwd:', cwd)
    return os.path.join(cwd,'dataset')

path = get_path()
print(path)

os.chdir(path)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(len(files))

def update_local_dataset(t, dataset_filename): 
    df = pd.read_csv(dataset_filename, index_col =0, header = 0)
    df.index = pd.to_datetime(df.index)
    #check latest date and pull new data
    latest_date = df.index[-1].date()
    start_date = max(latest_date + timedelta(days=1), date.today()- timedelta(days=7))
    start_date_str = start_date.strftime('%Y-%m-%d')
    today = date.today()
    ticker_obj = yf.Ticker(t)
    temp_df = ticker_obj.history(start = start_date_str, end = today, interval = '1m')
#    temp_df['ticker'] = t
    temp_df.to_csv(dataset_filename, mode = 'a', header = False)


def create_local_dataset(t, dataset_filename): 
    start_date = (date.today() - timedelta(7)).strftime('%Y-%m-%d')
    end_date = date.today().strftime('%Y-%m-%d')
    ticker_obj = yf.Ticker(t)
    t_df = ticker_obj.history(start = start_date, end = end_date, interval = '1m')
 #   t_df['ticker'] = t
    t_df.to_csv(dataset_filename)


def update_local_datasets(tickers,path):
    #go to current working directory and get file names
    cwd = os.getcwd()
    os.chdir(path)
    #files = [f for f in os.listdir('.') if os.path.isfile(f)]
    #open csv files and scan for symbols
    for t in tickers:
        print('working on ', t)
            # if file does not exist create new file with ticker:
        dataset_filename = ('{}.csv'.format(t))
        if os.path.isfile(dataset_filename ):
            update_local_dataset(t, dataset_filename)
        else:
            create_local_dataset(t, dataset_filename)
    os.chdir(cwd)
            
tickers = ['PSE', 'JNJ', 'NVS', 'MRK', 'AZN', 'SNP', 'PTR', 'BP', 'XOM', 'AMZN', 'TSLA', 'MSFT',
          'AAPL', 'ZOM', 'GS', 'JPM', 'WFC', 'FRC', 'HDB', 'RDS']

update_local_datasets(tickers,path)
