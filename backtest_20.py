# !pip install python-binance
from binance.client import Client
import numpy as np
import pandas as pd
from datetime import datetime
import enum
 
class buy:
    def __init__(self, price, time, size, tp=0, sl=0):
        self.price = price
        self.size = size
        self.tp = tp
        self.sl = sl
        self.time = time
 
    def close(self, price_now):
        return (price_now - self.price)
 
    def change(tp, sl):
        self.tp = tp
        self.sl = sl
 
def get_bars(symbol, timeframe, start_time, end_time):
    # api_key = 'XkA9wEWiO3HEuy8iSXg74S9dR9gBUtqsaa7QiZc5qire8iod1N8YKxTN2jGlzI2s'
    # api_secret = 'H0JWKsG9DM1k8kitOkAqajvmg9k8e073zy0dQ7HABIVrkdPj9YcbAwuqxYTOLJQP'

    api_key = 'mKudn88izK1eyiUHMena8sJ9dn2kpcwLgHG2KmVgGDIHsBiaOMyTTkcTRwLWvs0g'
    api_secret = 'SyAMegwr1J7UhTlIKBV6dMov4gk2xyUgvop9jLB7dvx0YZQgXUzCooLcnef2QOlD'

    client = Client(api_key, api_secret)
    candlesticks = client.get_historical_klines(symbol, timeframe.value, start_time, end_time)
    # df = np.asarray(candlesticks, dtype=np.float64)
    # df = pd.DataFrame(df).filter(items=[0, 1, 2, 3, 4, 5])
    # df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    # df['Time'] = [datetime.fromtimestamp(float(time) / 1000) for time in df['Time']]
    df = pd.DataFrame(candlesticks, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume','a','b','c','d','e','f'])
    df['Time'] = pd.to_datetime(df['Time'],unit='ms')
    df['Open'] = df['Open'].astype(np.float64)
    df['High'] = df['High'].astype(np.float64)
    df['Low'] = df['Low'].astype(np.float64)
    df['Close'] = df['Close'].astype(np.float64)
    df['Volume'] = df['Volume'].astype(np.float64)
    newdata = []
    delta_seconds = 60*Period[timeframe.name]
    time = np.float64(df['Time'].iloc[0].timestamp())
    end_time = df['Time'].iloc[-1]
    for i, row in df.iterrows():
      if row['Time'] == pd.to_datetime(time, unit='s'):
        newdata.append(row)
      elif row['Time'] != pd.to_datetime(time, unit='s'):
        while(row['Time'] != pd.to_datetime(time, unit='s') and pd.to_datetime(time, unit='s') != end_time):
          r = df.iloc[i-1].values
          r[0] = pd.to_datetime(time, unit='s')
          newdata.append(r)
          time = time + delta_seconds
        newdata.append(row)
      time = time + delta_seconds
    newdata = pd.DataFrame(newdata)
    return newdata
 
 
class database():
    def __init__(self):
        self.dictionary = {
            'in_1_minute': get_bars(crypto, Interval.in_1_minute, start_time, end_time),
            'in_3_minute': get_bars(crypto, Interval.in_3_minute, start_time, end_time),
            'in_5_minute': get_bars(crypto, Interval.in_5_minute, start_time, end_time),
            'in_15_minute': get_bars(crypto, Interval.in_15_minute, start_time, end_time),
            'in_30_minute': get_bars(crypto, Interval.in_30_minute, start_time, end_time),
            'in_1_hour': get_bars(crypto, Interval.in_1_hour, start_time, end_time),
            'in_2_hour': get_bars(crypto, Interval.in_2_hour, start_time, end_time),
            'in_4_hour': get_bars(crypto, Interval.in_4_hour, start_time, end_time),
            'in_6_hour': get_bars(crypto, Interval.in_6_hour, start_time, end_time),
            'in_8_hour': get_bars(crypto, Interval.in_8_hour, start_time, end_time),
            'in_12_hour': get_bars(crypto, Interval.in_12_hour, start_time, end_time),
            'in_1_day': get_bars(crypto, Interval.in_1_day, start_time, end_time),
        }
 
class local_database():
    def __init__(self):
        self.dictionary = {
            'in_1_minute': pd.read_csv('in_1_minute.csv'),
            'in_3_minute': pd.read_csv('in_3_minute.csv'),
            'in_5_minute': pd.read_csv('in_5_minute.csv'),
            'in_15_minute': pd.read_csv('in_15_minute.csv'),
            'in_30_minute': pd.read_csv('in_30_minute.csv'),
            'in_1_hour': pd.read_csv('in_1_hour.csv'),
            'in_2_hour': pd.read_csv('in_2_hour.csv'),
            'in_4_hour': pd.read_csv('in_4_hour.csv'),
            'in_6_hour': pd.read_csv('in_6_hour.csv'),
            'in_8_hour': pd.read_csv('in_8_hour.csv'),
            'in_12_hour': pd.read_csv('in_12_hour.csv'),
            'in_1_day': pd.read_csv('in_1_day.csv'),
        }
 
Period = {
    'in_1_minute': 1,
    'in_3_minute': 3,
    'in_5_minute': 5,
    'in_15_minute': 15,
    'in_30_minute': 30,
    'in_1_hour': 60,
    'in_2_hour': 120,
    'in_4_hour': 240,
    'in_6_hour': 360,
    'in_8_hour': 480,
    'in_12_hour': 720,
    'in_1_day': 1440
}
 
 
class Interval(enum.Enum):
    in_1_minute = Client.KLINE_INTERVAL_1MINUTE
    in_3_minute = Client.KLINE_INTERVAL_3MINUTE
    in_5_minute = Client.KLINE_INTERVAL_5MINUTE
    in_15_minute = Client.KLINE_INTERVAL_15MINUTE
    in_30_minute = Client.KLINE_INTERVAL_30MINUTE
    in_1_hour = Client.KLINE_INTERVAL_1HOUR
    in_2_hour = Client.KLINE_INTERVAL_2HOUR
    in_4_hour = Client.KLINE_INTERVAL_4HOUR
    in_6_hour = Client.KLINE_INTERVAL_6HOUR
    in_8_hour = Client.KLINE_INTERVAL_8HOUR
    in_12_hour = Client.KLINE_INTERVAL_12HOUR
    in_1_day = Client.KLINE_INTERVAL_1DAY
 
 
 
start_time = "7 jul, 2019"
end_time = "20 jul, 2021"
crypto = 'DOGEUSDT'


data_base = database()
for i in data_base.dictionary:
  data_base.dictionary[i].to_csv(i+'.csv', index=None)

# data_base = local_database()



