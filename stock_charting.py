#! /usr/bin/env python3

from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

def chart_daily(data, meta_data, option):
    # data is a pandas dataframe, meta_data is a dict
    # use option variable to choose between ['1. open', '2. high', '3. low', '4. close', '5. volume']
    figure(num=None, figsize=(15, 6), dpi=80, facecolor='w', edgecolor='k')
    # plot closing prices
    data["4. close"].plot()
    plt.tight_layout()
    plt.grid()
    plt.show()

