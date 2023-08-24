from taipy.gui import Gui, notify
import datetime as dt
import yfinance as yf

def get_stock_data(ticker):
    now = dt.date.today()
    past = now - dt.timedelta(days=365*2)
    return yf.download(ticker, past, now).reset_index()

ticker = 'AAPL'
data = get_stock_data(ticker)

historical = """
"""

Gui(historical).run()