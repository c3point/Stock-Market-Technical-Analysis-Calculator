# -*- coding: utf-8 -*-
"""
Author: Travis Campos
Date: 03/21/2019

Spyder Editor

Stock Market
"""
#%%

import datetime as dt
from datetime import datetime
from iexfinance.stocks import get_historical_data

import re


from iexfinance.stocks import Stock

def get_share_price(stock):
    price = Stock(stock).get_price()
    string = "$" + price
    return string

def find_company_name(stock):
    info = str(Stock(stock).get_company())
    lst = []
    lst = re.findall('companyName\': u\'([^\']+)',info)
    return lst[0]


now = dt.datetime.now()
start = dt.datetime(2010,9,25)
end = dt.datetime(now.year,now.month,now.day)

    
def test_plot():
    start = datetime(2017, 1, 1)
    end = datetime(2018, 1, 1)
    
    df = get_historical_data("TSLA", start, end)
    
    df = get_historical_data("AAPL", start, end, output_format='pandas')
    
    
    df.plot()
    plt.show()
    
    return


#df = get_historical_data("AAPL", start, end, output_format='pandas')
#print df





#%%
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import dateutil.relativedelta
import re


#from stock_market_technical_chart import *


now = dt.datetime.now()

style.use('ggplot')

start = dt.datetime(2010,9,25)
end = dt.datetime(now.year,now.month,now.day)


def find_date(month_count):
    d = dt.datetime.strptime(str(now.year)+"-"+str(now.month)+"-"+str(now.day), "%Y-%m-%d")
    d2 = d - dateutil.relativedelta.relativedelta(months=month_count)
    lst = []
    lst = re.split('-',str(d2))
    new_lst = []
    new_lst.append(int(lst[0]))
    new_lst.append(int(lst[1]))
    info = re.split("\s",lst[2])
    new_lst.append(int(info[0]))
    return new_lst


global_df = web.DataReader('AAPL','yahoo',start,end)
global_df.to_csv('stock.csv')




global_df = pd.read_csv('stock.csv',parse_dates = True, index_col = 0)
global_df['100ma'] = global_df['Adj Close'].rolling(window = 100,min_periods = 0).mean()
global_df['200ma'] = global_df['Adj Close'].rolling(window = 200,min_periods = 0).mean()


ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1) 




def three_month_chart():
    global start
    global global_df
    
    date = find_date(3)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('3month.csv')
    df = pd.read_csv('3month.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('three_m.png')
    
    plt.cla()
    
    

def six_month_chart():
    global start
    global global_df
    
    date = find_date(6)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('6month.csv')
    df = pd.read_csv('6month.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('six_m.png')
    
    plt.cla()

def nine_month_chart():
    global start
    global global_df
    
    date = find_date(9)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('9month.csv')
    df = pd.read_csv('9month.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('nine_m.png')
    
    plt.cla()

def one_year_chart():
    global start
    global global_df
    
    date = find_date(12)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('1year.csv')
    df = pd.read_csv('1year.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('one_y.png')
    
    plt.cla()

def three_year_chart():
    global start
    global global_df
    
    date = find_date(36)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('3year.csv')
    df = pd.read_csv('3year.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('three_y.png')
    
    plt.cla()
    
def five_year_chart():
    global start
    global global_df
    
    date = find_date(60)
    start = dt.datetime(date[0],date[1],date[2])
    
    df = web.DataReader('AAPL','yahoo',start,end)
    df.to_csv('5year.csv')
    df = pd.read_csv('5year.csv',parse_dates = True, index_col = 0)
    
    plt.rcParams["figure.figsize"] = (10,5)
    size = global_df.shape[0]
    
    ax1.plot(df.index, df['Adj Close'],color = 'Green')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['100ma'][range(size-df.shape[0],size)], color = 'Blue')
    ax1.plot(global_df.index[range(size-df.shape[0],size)], global_df['200ma'][range(size-df.shape[0],size)], color = 'Red')
    ax2.bar(global_df.index[range(size-df.shape[0],size)], global_df['Volume'][range(size-df.shape[0],size)])
    plt.savefig('five_y.png')
    
    plt.cla()

def save_charts():
    three_month_chart()
    six_month_chart()
    nine_month_chart()
    one_year_chart()
    three_year_chart()
    five_year_chart()
    return
    

save_charts()






#%%