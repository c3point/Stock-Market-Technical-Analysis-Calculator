# -*- coding: utf-8 -*-
"""
Author: Travis Campos
Date: 03/21/2019

Spyder Editor

Stock Market
"""
#%%
from PyQt4 import QtCore, QtGui

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import dateutil.relativedelta
import re

from yahoo_finance import Share
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock

now = dt.datetime.now()


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

start_date = find_date(3)
start = dt.datetime(start_date[0],start_date[1],start_date[2])

msft = Stock("MSFT")
print msft.get_market_cap()


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.zacks.com/stock/quote/AAPL")
soup = BeautifulSoup(r.content, "html.parser")
for tr in soup.findAll("table", class_="abut_bottom"):
    for td in tr.find_all("td"):
        if td.text == "Market Cap":
            print td.text, td.find_next_sibling("td").text







def fill_table_NYSE():
    for i in range(1,4):
        for j in range(1,7):
            pass
            
            

def fill_table_Nasdaq():
    pass
    


#%%