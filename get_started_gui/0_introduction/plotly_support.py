from taipy.gui import Gui, invoke_long_callback

import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

df['SMA 20'] = df['AAPL.Close'].rolling(20).mean()
df['SMA 50'] = df['AAPL.Close'].rolling(50).mean()

df['Buy'] = (df['SMA 20'] > df['SMA 50']) & (df['SMA 20'].shift(1) <= df['SMA 50'].shift(1))


def create_financial_chart(df, i):
    if i < len(df):
        df = df[i-100:i]



    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03, subplot_titles=('', ''), row_heights=[0.7, 0.3])

    fig.add_trace(go.Candlestick(x=df['Date'],
                    name='Candlestick',
                    open=df['AAPL.Open'],
                    high=df['AAPL.High'],
                    low=df['AAPL.Low'],
                    close=df['AAPL.Close']), row=1, col=1)

    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA 20'], mode='lines', name='SMA 20'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA 50'], mode='lines', name='SMA 50'), row=1, col=1)

    fig.add_trace(go.Bar(x=df['Date'], y=df['AAPL.Volume'], name='Volume', marker_color='grey'), row=2, col=1)


    for idx, row in df.iterrows():
        if row['Buy']:
            fig.add_annotation(x=row['Date'], y=row['AAPL.Close'],
                            text="Buy", showarrow=True,
                            arrowhead=1, arrowcolor="green", arrowsize=3, arrowwidth=1,
                            bgcolor="grey", row=1, col=1)

    # Have a cursor
    fig.update_yaxes(spikemode='across', spikesnap='cursor')
    fig.update_layout(hoverdistance=1, hovermode="x unified")
    return fig

i = int(len(df)/2)
fig = create_financial_chart(df, i)


def iddle():
    while True:
        time.sleep(1)

def update_real_time_chart(state):
    state.fig = create_financial_chart(state.df, state.i)
    print(state.i)
    state.i = state.i + 1

def on_init(state):
    invoke_long_callback(state,
                         iddle, [],
                         update_real_time_chart, [],
                         500)

Gui("<|chart|figure={fig}|height=800px|>").run(port=3040)