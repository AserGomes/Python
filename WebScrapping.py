import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import datetime
import yfinance as yf
import pandas_datareader as web
import requests
import time
import io
import mplfinance as mpl

ontem=datetime.datetime.today()

title='PETR4.SA'
enddate = int(datetime.datetime.timestamp(datetime.datetime(ontem.year,ontem.month,ontem.day-1,ontem.hour,ontem.minute,ontem.second))) - time.timezone
startdate= int(datetime.datetime.timestamp(datetime.datetime(ontem.year-1,ontem.month,ontem.day-1,ontem.hour,ontem.minute,ontem.second))) - time.timezone
#https://query1.finance.yahoo.com/v7/finance/download/BBDC4.SA?period1=1647975607&period2=1679511607&interval=1d&events=history&includeAdjustedClose=true
urlyahoo=f'https://query1.finance.yahoo.com/v7/finance/download/{title}?period1={startdate}&period2={enddate}&interval=1d&events=history&includeAdjustedClose=true'

def getdata(papel,start=None,end=None):

    e = pd.to_datetime(end)
    s = pd.to_datetime(start)
    ontem = datetime.datetime.today()

    if(end==None):
        enddate = int(datetime.datetime.timestamp(datetime.datetime(ontem.year, ontem.month, ontem.day - 1, ontem.hour, ontem.minute,ontem.second))) - time.timezone
    else:
        enddate = int(datetime.datetime.timestamp(datetime.datetime(e.year, e.month, e.day - 1, e.hour, e.minute,e.second))) - time.timezone

    if(start==None):
        startdate = int(datetime.datetime.timestamp(datetime.datetime(ontem.year - 1, ontem.month, ontem.day - 1, ontem.hour, ontem.minute,ontem.second))) - time.timezone
    else:
        startdate = int(datetime.datetime.timestamp(datetime.datetime(s.year - 1, s.month, s.day - 1, s.hour, s.minute,s.second))) - time.timezone

    url = f'https://query1.finance.yahoo.com/v7/finance/download/{papel}?period1={startdate}&period2={enddate}&interval=1d&events=history&includeAdjustedClose=true'
    r = requests.get(url,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
    data = pd.read_csv(io.StringIO(r.content.decode('utf=8')),index_col=0,parse_dates=True)
    df = pd.DataFrame({
                     'data':data.index,
                     'open': data.Open,
                     'close':data.Close,
                     'high':data.High,
                     'low':data.Low,
                     'volume':data.Volume
                      })
    return df

def getcandle(papel, start=None, end=None):
    jp = getdata(papel, start, end)
    mpl.plot(jp,type='candle',style='yahoo',figsize=(15,7),title=papel)
    x = mpl.show()
    return x

carteira=['PETR4.SA','EGIE3.SA','CPLE6.SA','TRPL4.SA']
figures=['PETR4.SA','EGIE3.SA','CPLE6.SA','TRPL4.SA']

getcandle('BBDC4.SA')
mpl.show()



