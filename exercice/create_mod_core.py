import pandas as pd
from prophet import Prophet
from taipy import Config

def clean_data(initial_dataset: pd.DataFrame):
    print("Cleaning Data")
    initial_dataset = initial_dataset.rename(columns={"Date": "ds", "Close": "y"})
    initial_dataset['ds'] = pd.to_datetime(initial_dataset['ds']).dt.tz_localize(None)
    cleaned_dataset = initial_dataset.copy()
    return cleaned_dataset

def retrained_model(cleaned_dataset: pd.DataFrame):
    print("Model Retraining")
    model = Prophet()
    model.fit(cleaned_dataset)
    return model


def predict(model):
    periods = 365
    return model.predict(model.make_future_dataframe(periods=periods)[-periods:])[['ds', 'yhat']].rename(columns = {'ds':'Date', 'yhat':'Close_Prediction'})


## Input Data Nodes
initial_dataset_cfg = Config.configure_data_node(id="initial_dataset",
                                                 storage_type="csv",
                                                 default_path='df.csv')

cleaned_dataset_cfg = Config.configure_data_node(id="cleaned_dataset")                                                  

clean_data_task_cfg = Config.configure_task(id="clean_data_task",
                                            function=clean_data,
                                            input=initial_dataset_cfg,
                                            output=cleaned_dataset_cfg,
                                            skippable=True)


model_training_cfg = Config.configure_data_node(id="model_output")                                                  

predictions_cfg = Config.configure_data_node(id="predictions")                                                  

model_training_task_cfg = Config.configure_task(id="model_retraining_task",
                                                function=retrained_model,
                                                input=cleaned_dataset_cfg,
                                                output=model_training_cfg,
                                                skippable=True)

predict_task_cfg = Config.configure_task(id="predict_task",
                                         function=predict,
                                         input=model_training_cfg,
                                         output=predictions_cfg,  
                                         skippable=True)

# Create our scenario configuration from our tasks
scenario_cfg = Config.configure_scenario_from_tasks(id="stock",
                                                    task_configs=[clean_data_task_cfg,
                                                    model_training_task_cfg,
                                                    predict_task_cfg])


"""
import taipy as tp
import yfinance as yf

# Run of the Taipy Core service
tp.Core().run()

def get_stock_data(ticker, start):
    ticker_data = yf.download(ticker, start, dt.datetime.now()).reset_index()  # downloading the stock data from START to TODAY
    ticker_data['Date'] = ticker_data['Date'].dt.tz_localize(None)
    return ticker_data


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

stocks = tp.get_scenarios()

for stock in stocks:
    print(stock.name)
    print(stock.predictions.read())
"""