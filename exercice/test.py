from taipy.gui import Gui, notify
import pandas as pd
import yfinance as yf
from taipy.config import Config
import taipy as tp 
import datetime as dt

Config.load('config_model_train.toml')
scenario_cfg = Config.scenarios['stock']

def get_stock_data(ticker, start):
    ticker_data = yf.download(ticker, start, dt.datetime.now()).reset_index()  # downloading the stock data from START to TODAY
    ticker_data['Date'] = ticker_data['Date'].dt.tz_localize(None)
    return ticker_data

start_date = '2015-01-01'

property_chart = {"type":"lines",
                  "x":"Date",
                  "y[1]":"Open",
                  "y[2]":"Close",
                  "y[3]":"High",
                  "y[4]":"Low",
                  "color[1]":"green",
                  "color[2]":"grey",
                  "color[3]":"red",
                  "color[4]":"yellow"
                 }


df = pd.DataFrame([], columns = ['Date', 'High', 'Low', 'Open', 'Close'])
df_pred = pd.DataFrame([], columns = ['Date','Close_Prediction'])

stock_text = "No Stock to Show"
chart_text = 'No Chart to Show'
pred_text = 'No Prediction to Show'

stock = ""
stocks = []

page = """
<|toggle|theme|>
# Stock Portfolio

### Choose the stock to show

<|layout|columns=1 1|
<|{f'The stock is {stock.name}' if stock else 'No Stock to Show'}|>
<|{stock}|selector|lov={stocks}|dropdown|adapter={lambda s: s.name}|>
<|Reset|button|on_action=reset|>
<|Press for Stock|button|on_action=update_ticker_history|active={stock}|>
<|Update Model|button|on_action=update_model|active={stock}|>


<|{f'Monthly history of stock {stock.name}' if stock else 'No Chart to Show'}|>
<|{df}|chart|properties={property_chart}|>
|>

<|{f'1 Year Close Prediction of Stock {stock.name}' if stock else 'No Prediction to Show'}|>
<|{df_pred}|chart|x=Date|y=Close_Prediction|>
"""

def reset(state):
    state.stock = ""
    state.df = pd.DataFrame([], columns = ['Date', 'High', 'Low', 'Open', 'Close'])
    state.df_pred = pd.DataFrame([], columns = ['Date','Close_Prediction'])
    notify(state, 'success', 'Reset done!')



def update_ticker_history(state):
    state.stock.initial_dataset.write(get_stock_data(state.stock.name, start_date))
    on_change(state, "stock", state.stock)
    notify(state, 'success', 'History up-to-date! You should retrain the model')

def on_change(state, var_name, var_value):
    if var_name == "stock" and var_value:
        state.df = state.stock.initial_dataset.read()
        state.df_pred = state.stock.predictions.read()      

def update_model(state):
    print("Update Model Clicked")
    tp.submit(state.stock)
    on_change(state, "stock", state.stock)
    notify(state, 'success', 'Model trained and charts up-to-date!')


def on_init(state):
    tickers = {'MSFT':get_stock_data('MSFT', start_date),
               'AAPL':get_stock_data('AAPL', start_date),
               'GOOG':get_stock_data('GOOG', start_date)}

    def create_and_submit_scenario(stock_name):
        scenario_stock = tp.create_scenario(scenario_cfg, name=stock_name)
        scenario_stock.initial_dataset.path = f"{stock_name}.csv"
        scenario_stock.initial_dataset.write(tickers[stock_name])
        tp.submit(scenario_stock)

    for stock_name in tickers.keys():
        create_and_submit_scenario(stock_name)

    state.stocks = tp.get_scenarios()
    state.stock = state.stocks[0]

tp.Core().run()
Gui(page).run()
