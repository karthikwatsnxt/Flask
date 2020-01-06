from alpha_vantage.timeseries import TimeSeries
# Your key here
key = 'PTI5V1H8HF25R6O6'
ts = TimeSeries(key)
tsla, meta = ts.get_daily(symbol='AMZN')
print(tsla['2020-01-02'])

##########################################################################

from yahoo_fin.stock_info import *
tickers = tickers_nasdaq()
print (tickers)
get_options_chain('amzn', '03/15/2019')
get_stats('aapl')

###############################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2019,12,1)
end=datetime.datetime.now()
stock='TSLA'
df=web.DataReader(stock,'yahoo',start,end)
app=dash.Dash()

app.layout= html.Div(children=[
        html.H1(children='TSLA Stock Dashboard'),        
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df.Close , 'type': 'bar', 'name': stock}
            ],
            'layout': {
                'title': 'Stock Price'
            }
        }
    )
        ])

if __name__ == '__main__':
    app.run_server()
	
	
########################################################################################


# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si

# get live price of Apple
si.get_live_price("aapl")
 
# or Amazon
si.get_live_price("amzn")
 
# or any other ticker
si.get_live_price(ticker)

# get quote table back as a data frame
si.get_quote_table("aapl", dict_result = False)
 
# or get it back as a dictionary (default)
si.get_quote_table("aapl")

# get most active stocks on the day
si.get_day_most_active()
 
# get biggest gainers
si.get_day_gainers()
 
# get worst performers
si.get_day_losers()

############################################################################################