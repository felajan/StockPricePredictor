#! /usr/bin/env python3
import matplotlib
import requests
import asyncio
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import sys
import dearpygui.dearpygui as dpg
import stock_charting


# load necessary information such as api key from .env file
load_dotenv()
api_key = os.getenv('ALPHA_KEY')
query_url = os.getenv('ALPHA_QUERY')
ts = TimeSeries(api_key, output_format='pandas')

# set backend for matplotlib
# set to PyQt6 for now while exploring charting options with dearpygui vs pyqt5
print("Getting current backend for matplotlib: {}\n".format(matplotlib.get_backend()))
print("Setting backend to PyQt5\n")
matplotlib.rcParams['backend'] = 'Qt5Agg'
print("Getting new backend for matplotlib: {}\n".format(matplotlib.get_backend()))
# will use to get SMA later
# ti = TechIndicators(api_key)

# we are going to be using AAPL stock for the purpose of working on our code
# will have the option for user input for stock symbol in further iterations
# get daily ['1. open', '2. high', '3. low', '4. close', '5. volume']
aapl_data, aapl_meta_data = ts.get_daily(symbol='AAPL')
stock_charting.chart_daily(aapl_data, aapl_meta_data)

# code for creating GUI will be worked on here for now
