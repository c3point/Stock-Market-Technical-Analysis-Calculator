# -*- coding: utf-8 -*-
"""
Author: Travis Campos
Date: 03/21/2019

Spyder Editor

Stock Market
"""
#%%

from datetime import datetime
from iexfinance.stocks import get_historical_data

start = datetime(2017, 1, 1)
end = datetime(2018, 1, 1)

df = get_historical_data("TSLA", start, end)

df = get_historical_data("AAPL", start, end, output_format='pandas')

import matplotlib.pyplot as plt

df.plot()
plt.show()

#%%
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web



style.use('ggplot')

start = dt.datetime(2014,1,1)
end = dt.datetime(2019,3,15)

df = web.DataReader('SPY','yahoo',start,end)
df.to_csv('aapl.csv')




df = pd.read_csv('aapl.csv',parse_dates = True, index_col = 0)
df['100ma'] = df['Adj Close'].rolling(window = 100,min_periods = 0).mean()
df['200ma'] = df['Adj Close'].rolling(window = 200,min_periods = 0).mean()


ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1) 

ax1.plot(df.index, df['Adj Close'],color = 'Green')
ax1.plot(df.index, df['100ma'], color = 'Blue')
ax1.plot(df.index, df['200ma'], color = 'Red')
ax2.bar(df.index, df['Volume'])

#%%