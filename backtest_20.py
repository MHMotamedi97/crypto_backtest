from binance.client import Client
import talib
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
	  print(i)
      if row['Time'] == pd.to_datetime(time, unit='s'):
        newdata.append(row)
      elif row['Time'] != pd.to_datetime(time, unit='s'):
        while(row['Time'] != pd.to_datetime(time, unit='s') and pd.to_datetime(time, unit='s') != end_time):
          r = df.iloc[i-1].values
          r[0] = pd.to_datetime(time, unit='s')
          #r = pd.DataFrame(r)
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
 
 





class MACD():
    def __init__(self, time, interval, data, tick, fastperiod=12, slowperiod=26, signalperiod=9):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.fastperiod = fastperiod
        self.slowperiod = slowperiod
        self.signalperiod = signalperiod
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_macd(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        macd, _, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return macd[len(macd) - 1]
 
    def last_signal(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        _, signal, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return signal[len(signal) - 1]
        
    def last_last_macd(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        macd, _, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return macd[len(macd) - 2]
 
    def last_last_signal(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        _, signal, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return signal[len(signal) - 2]
        
    def last_last_last_macd(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        macd, _, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return macd[len(macd) - 3]
 
    def last_last_last_signal(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        _, signal, _ = talib.MACD(closed_bars, fastperiod=12, slowperiod=26, signalperiod=9)
        return signal[len(signal) - 3]
 
 
class RSI():
    def __init__(self, time, interval, data, tick, timeperiod=7):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_rsi(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        rsi = talib.RSI(closed_bars, timeperiod=self.timeperiod)
        return rsi[len(rsi) - 1]
 
    def last_last_rsi(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        rsi = talib.RSI(closed_bars, timeperiod=self.timeperiod)
        return rsi[len(rsi) - 2]
 
    def last_last_last_rsi(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        rsi = talib.RSI(closed_bars, timeperiod=self.timeperiod)
        return rsi[len(rsi) - 3]
 
 
class PLUS_DI3():
    def __init__(self, time, interval, data, tick, timeperiod=14):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_plus_di(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        PLUS_DI31 = talib.PLUS_DI(high_bars, low_bars, closed_bars, timeperiod=self.timeperiod)
        return PLUS_DI31[len(PLUS_DI31) - 1]
 
 
class MINUS_DI3():
    def __init__(self, time, interval, data, tick, timeperiod=14):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_minus_di(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        MINUS_DI3 = talib.MINUS_DI(high_bars, low_bars, closed_bars, timeperiod=self.timeperiod)
        return MINUS_DI3[len(MINUS_DI3) - 1]
 
    def last_last_minus_di(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        MINUS_DI3 = talib.MINUS_DI(high_bars, low_bars, closed_bars, timeperiod=self.timeperiod)
        return MINUS_DI3[len(MINUS_DI3) - 2]
 
 
class STOCH():
    def __init__(self, time, interval, data, tick, fastk_period=14, slowk_period=5, slowk_matype=0, slowd_period=5,
                 slowd_matype=0):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.fastk_period = fastk_period
        self.slowk_period = slowk_period
        self.slowk_matype = slowk_matype
        self.slowd_period = slowd_period
        self.slowd_matype = slowd_matype
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_slowk(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        slowk, slowd = talib.STOCH(high_bars, low_bars, closed_bars, fastk_period=self.fastk_period,
                                   slowk_period=self.slowk_period, slowk_matype=self.slowk_matype,
                                   slowd_period=self.slowd_period, slowd_matype=self.slowd_matype)
        return slowk[len(slowk) - 1]
 
    def last_last_slowk(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        slowk, slowd = talib.STOCH(high_bars, low_bars, closed_bars, fastk_period=self.fastk_period,
                                   slowk_period=self.slowk_period, slowk_matype=self.slowk_matype,
                                   slowd_period=self.slowd_period, slowd_matype=self.slowd_matype)
        return slowk[len(slowk) - 2]
 
    def last_slowd(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        slowk, slowd = talib.STOCH(high_bars, low_bars, closed_bars, fastk_period=self.fastk_period,
                                   slowk_period=self.slowk_period, slowk_matype=self.slowk_matype,
                                   slowd_period=self.slowd_period, slowd_matype=self.slowd_matype)
        return slowd[len(slowd) - 1]
 
    def last_last_slowd(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        slowk, slowd = talib.STOCH(high_bars, low_bars, closed_bars, fastk_period=self.fastk_period,
                                   slowk_period=self.slowk_period, slowk_matype=self.slowk_matype,
                                   slowd_period=self.slowd_period, slowd_matype=self.slowd_matype)
        return slowd[len(slowd) - 2]
 
 
class PMA():
    def __init__(self, time, interval, data, tick, timeperiod=50):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_pma(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        pma = talib.MA((high_bars + low_bars + closed_bars) / 3, timeperiod=self.timeperiod)
        return pma[len(pma) - 1]
 
    def last_last_pma(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        high_bars = self.data['High'].values[0:self.timestamp]
        low_bars = self.data['Low'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        # np.append(high_bars, candle[1])
        # np.append(low_bars, candle[2])
        pma = talib.MA((high_bars + low_bars + closed_bars) / 3, timeperiod=self.timeperiod)
        return pma[len(pma) - 2]
 
 
class MA():
    def __init__(self, time, interval, data, tick, timeperiod=12):
        self.time = time
        self.timestamp = int(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_ma(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        ma = talib.MA(closed_bars, timeperiod=self.timeperiod)
        return ma[len(ma) - 1]
 
    def last_last_ma(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        # np.append(closed_bars, candle[3])
        ma = talib.MA(closed_bars, timeperiod=self.timeperiod)
        return ma[len(ma) - 2]
 
 
class EMA():
    def __init__(self, time, interval, data, tick, timeperiod=3):
        self.time = time
        self.timestamp = np.int64(time / Period[interval.name]) + 1
        self.interval = interval.value
        self.data = data.dictionary[interval.name]
        self.tick = tick
        self.current_candle = np.zeros(4)
        self.period = Period[interval.name]
        self.timeperiod = timeperiod
 
    def make_candle(self, current_candle, tick, period, time):
        x = current_candle
        if (self.time % self.period == 0):
            x = np.array([tick, tick, tick, tick])
            self.current_candel = x
            return x
 
        elif (self.time % self.period == self.period - 1):
            x[3] = tick
            self.current_candel = x
            return x
        else:
            if tick > x[1]:
                x[1] = tick
                self.current_candel = x
                return x
            elif tick < x[2]:
                x[2] = tick
                self.current_candel = x
                return x
        self.current_candel = x
        return x
 
    def last_ema(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        Open_bars = self.data['Open'].values[0:self.timestamp]
        High_bars = self.data['High'].values[0:self.timestamp]
        Low_bars = self.data['Low'].values[0:self.timestamp]
        close_ha=(closed_bars+Open_bars+High_bars+Low_bars)/4
        # np.append(closed_bars, candle[3])
        ema = talib.EMA(closed_bars, timeperiod=self.timeperiod)
        # print("time", self.time, "timestamp", self.timestamp)
        return ema[len(ema) - 1]


    def last_last_ema(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        
        closed_bars = self.data['Close'].values[0:self.timestamp]
        Open_bars = self.data['Open'].values[0:self.timestamp]
        High_bars = self.data['High'].values[0:self.timestamp]
        Low_bars = self.data['Low'].values[0:self.timestamp]
        close_ha=(closed_bars+Open_bars+High_bars+Low_bars)/4
        # np.append(closed_bars, candle[3])
        ema = talib.EMA(closed_bars, timeperiod=self.timeperiod)
        return ema[len(ema) - 2]
        
    def last_last_last_ema(self):
        # candle = self.make_candle(self.current_candle, self.tick, self.period, self.time)
        closed_bars = self.data['Close'].values[0:self.timestamp]
        Open_bars = self.data['Open'].values[0:self.timestamp]
        High_bars = self.data['High'].values[0:self.timestamp]
        Low_bars = self.data['Low'].values[0:self.timestamp]
        close_ha=(closed_bars+Open_bars+High_bars+Low_bars)/4
        # np.append(closed_bars, candle[3])
        ema = talib.EMA(closed_bars, timeperiod=self.timeperiod)
        return ema[len(ema) - 3]
 
 
def tick_gen(low, high, size):
  if low < high:
    x = np.random.uniform(low, high, size)
  else:
    x = np.random.uniform(high, low, size)
  return x
 
 
start_time = "7 jul, 2019"
end_time = "20 jul, 2021"
crypto = 'DOGEUSDT'

balance = 10000
price = 0
buy_price = 0
sale_order = 0
stoploss = 0
buy_trigger = 0
percent = 1
commission = 0.002

orders = []
history = []

data_base = database()
for i in data_base.dictionary:
  data_base.dictionary[i].to_csv(i+'.csv', index=None)

# data_base = local_database()

one_min = data_base.dictionary[Interval.in_1_minute.name].values

for timestamp in range (one_min.shape[0]):
    # ticks = tick_gen(one_min[timestamp][4], one_min[timestamp][1], 1)  # 24 ro kardam 1
    # for tick in ticks:
    tick = one_min[timestamp][4]
    size = round((balance * percent) / tick, ndigits=3)
    # signal_1d = MACD(timestamp, Interval.in_1_day, data=data_base, tick=tick)
    # macd_1d = MACD(timestamp, Interval.in_1_day, data=data_base, tick=tick)
    # rsi_1d = RSI(timestamp, Interval.in_1_day, data=data_base, tick=tick)
    # ma3_1d = MA(timestamp, Interval.in_1_day, data=data_base, tick=tick, timeperiod=3)
    # 1h
    # macd_1h = MACD(timestamp, Interval.in_1_hour, data=data_base, tick=tick)
    # signal_1h = MACD(timestamp, Interval.in_1_hour, data=data_base, tick=tick)
    # rsi_1h = RSI(timestamp, Interval.in_1_hour, data=data_base, tick=tick)
    # 5m
    # ema3_5m = EMA(timestamp, Interval.in_5_minute, data=data_base, tick=tick, timeperiod=3)
    # ema25_5m = EMA(timestamp, Interval.in_5_minute, data=data_base, tick=tick, timeperiod=25)
    # ema50_5m = EMA(timestamp, Interval.in_5_minute, data=data_base, tick=tick, timeperiod=50)
    # ema100_5m = EMA(timestamp, Interval.in_5_minute, data=data_base, tick=tick, timeperiod=100)
    # rsi_5m = RSI(timestamp, Interval.in_5_minute, data=data_base, tick=tick)
    # 15m
    ema3_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=3)
    # ema4_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=4)
    # ema8_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=8)
    # ema12_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=12)
    ema13_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=13)
    # ema20_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=20)
    # ema50_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=50)
    # ema100_15m = EMA(timestamp, Interval.in_15_minute, data=data_base, tick=tick, timeperiod=100)
    # rsi_15m = RSI(timestamp, Interval.in_15_minute, data=data_base, tick=tick)
    # plus_di_15m = PLUS_DI3(timestamp, Interval.in_15_minute, data=data_base, tick=tick)
    # minus_di_15m = MINUS_DI3(timestamp, Interval.in_15_minute, data=data_base, tick=tick)
    # 30m
    # ema3_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=3)
    # ema4_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=4)
    # ema8_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=8)
    # ema12_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=12)
    # ema13_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=13)
    # ema20_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=20)
    # ema50_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=50)
    # ema100_30m = EMA(timestamp, Interval.in_30_minute, data=data_base, tick=tick, timeperiod=100)
    # rsi_30m = RSI(timestamp, Interval.in_30_minute, data=data_base, tick=tick)
    # plus_di_30m = PLUS_DI3(timestamp, Interval.in_30_minute, data=data_base, tick=tick)
    # print(one_min[timestamp][0])
    # print(ema3_15m.last_ema())
    try:
      if len(orders) == 0:  
        # print(ema3_15m.last_ema(), ema13_15m.last_ema())
        # print(len(orders))
        # if timestamp > 59200 and timestamp < 60000:
          # print(ema3_15m.last_ema(), '\t', ema13_15m.last_ema())
          # print(one_min[timestamp][0])
        if ema3_15m.last_ema() > ema13_15m.last_ema(): 
          # print(ema3_15m.last_ema(), '\t', ema13_15m.last_ema())
          # print(one_min[timestamp][0])
          # print(timestamp)
          buy_trigger = 2
          orders.append(buy(tick, time=one_min[timestamp][0], size=size))
          price = orders[0].size * tick
          # print("2", size)
          balance = balance - (tick * orders[0].size)
          stoploss = tick - (tick * 0.002)
          #stoploss = ema100_5m.last_ema()
          sale_order = ((tick - stoploss) * 3) + tick   
          # print("opening time =", orders[0].time, "\t", "price =", tick , "Stoploss =", stoploss, "sale_order = ", sale_order) #, "ema25 =", ema25_5m.last_ema(), "ema50 =", ema50_5m.last_ema(), "ema100 =", ema100_5m.last_ema(), "ema3 =", ema3_5m.last_ema())  
      elif len(orders) == 1: 
        # print(ema3_15m.last_ema(), ema13_15m.last_ema()) 
        # print(len(orders))
        if ema3_15m.last_ema() < ema13_15m.last_ema():
          buy_trigger = 0
          profit = ((orders[0].close(tick) * orders[0].size))
          com = price*commission
          pure  = profit - com
          balance = balance + pure + price
          price = 0
          qoute = np.array([orders[0].time, orders[0].price, one_min[timestamp][0], tick, orders[0].size, (orders[0].close(tick) * orders[0].size), balance])
          print("opening time =", orders[0].time, "\t", "close Price =", tick, "\t", "closing time =",
          one_min[timestamp][0], "\t", "size =", orders[0].size, "\t","profit(Dallar) =",
          pure, "\t","profit(percent) =" , (pure*100)/(balance-pure) , "\t", "Balance =", balance)
          history.append(qoute)
          orders = []
    except Exception as e:
        print(e)
        pass

if (len(orders) == 1):
    history.append(np.array([orders[0].time, orders[0].price, one_min[timestamp][0], tick, orders[0].size, (orders[0].close(tick) * orders[0].size), balance]))
    orders = []
if (len(history) > 0):
    history = pd.DataFrame(history)
    history.columns = ["Opening Time", "Open Price", "Closing Time", "Close Price", "Size", "Profit", "Balance"]
    history.to_excel(excel_writer="./history_abbas_ema3_13_2years_newnew.xlsx")



