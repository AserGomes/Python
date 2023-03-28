import pandas as pd
import numpy as np
import datetime
import requests
import io
import time
import mplfinance as mpl

def getdata(papel,start=None,end=None):

    e = pd.to_datetime(end)
    s = pd.to_datetime(start)
    now = datetime.datetime.today()

    if(end==None):
        enddate = int(datetime.datetime.timestamp(datetime.datetime(now.year, now.month, now.day - 1, now.hour, now.minute,now.second))) - time.timezone
    else:
        enddate = int(datetime.datetime.timestamp(datetime.datetime(e.year, e.month, e.day - 1, e.hour, e.minute,e.second))) - time.timezone

    if(start==None):
        startdate = int(datetime.datetime.timestamp(datetime.datetime(now.year - 1, now.month, now.day - 1, now.hour, now.minute,now.second))) - time.timezone
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

getcandle('PETR4.SA')



