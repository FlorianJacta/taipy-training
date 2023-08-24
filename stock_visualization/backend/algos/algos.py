from datetime import timedelta
import yfinance as yf
from prophet import Prophet

def get_data(ticker, date):
    past = date - timedelta(days=365*7)
    return yf.download(ticker, past, date).reset_index()

def predict(preprocessed_dataset):
    df_train = preprocessed_dataset[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})  # This is the format that Prophet accepts

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=365)
    predictions = m.predict(future)[['ds', 'yhat']].rename(columns={'ds': 'Date', 'yhat': 'Predictions'})[-365:]
    return predictions.reset_index()

