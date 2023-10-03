from taipy.gui import Gui, notify
import datetime as dt
import yfinance as yf

def get_stock_data(ticker):
    now = dt.date.today()
    past = now - dt.timedelta(days=365*2)
    return yf.download(ticker, past, now).reset_index()

def update_ticker(state):
    state.data = get_stock_data(state.ticker)
    notify(state, "success", "Ticker updated!")

ticker = 'AAPL'
data = get_stock_data(ticker)

historical = """
#### Stock Price **Analysis**{: .color-primary}
<|{ticker}|toggle|lov=MSFT;GOOG;AAPL|on_change=update_ticker|>

Mean Volume: <|{int(data['Volume'].mean())}|>

<|{data}|chart|x=Date|y=Volume|>
"""

Gui(historical).run()