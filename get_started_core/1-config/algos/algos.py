import datetime as dt
import pandas as pd


def clean_data(initial_dataset: pd.DataFrame):
    print("     Cleaning data")
    initial_dataset['Date'] = pd.to_datetime(initial_dataset['Date'])
    cleaned_dataset = initial_dataset[['Date', 'Value']]
    return cleaned_dataset


def predict(cleaned_dataset: pd.DataFrame, day: dt.datetime):
    print("     Predicting")
    train_dataset = cleaned_dataset[cleaned_dataset['Date'] < pd.Timestamp(day.date())]
    predictions = train_dataset['Value'][-30:].reset_index(drop=True)
    return pd.DataFrame({"Prediction":predictions})


def evaluate(predictions, cleaned_dataset, day):
    print("     Evaluating")
    expected = cleaned_dataset.loc[cleaned_dataset['Date'] >= pd.Timestamp(day.date()), 'Value'][:30].reset_index(drop=True)
    mae = ((predictions['Prediction'] - expected) ** 2).mean()
    return int(mae)
