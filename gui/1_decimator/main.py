import yfinance as yf
from taipy.gui import Gui
from taipy.gui.data.decimator import MinMaxDecimator, RDP, LTTB


df_AAPL = yf.Ticker("AAPL").history(interval="1d", period = "100Y")
df_AAPL["DATE"] = df_AAPL.index.astype(int).astype(float)

n_out = 500
decimator_instance = MinMaxDecimator(n_out=n_out)

decimate_data_count = len(df_AAPL)

page = """
# Decimator

From a data length of <|{len(df_AAPL)}|> to <|{n_out}|>

## Without decimator

<|{df_AAPL}|chart|x=DATE|y=Open|>

## With decimator

<|{df_AAPL}|chart|x=DATE|y=Open|decimator=decimator_instance|>
"""

gui = Gui(page)
gui.run(port=5025)
