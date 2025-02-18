from taipy.gui import notify, Markdown
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

historical = Markdown("""
## Stock Price **Analysis**{: .color-primary} <|{ticker}|toggle|lov=MSFT;GOOG;AAPL|on_change=update_ticker|>

<|{data}|chart|x=Date|y=Volume|>
""")