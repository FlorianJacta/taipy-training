import datetime as dt
import pandas as pd


def clean_data(initial_dataset: pd.DataFrame):
    print("     Cleaning data")
    initial_dataset["Date"] = pd.to_datetime(initial_dataset["Date"])
    cleaned_dataset = initial_dataset[["Date", "Value"]]
    return cleaned_dataset


def predict(cleaned_dataset: pd.DataFrame, day: dt.datetime):
    print("     Predicting")
    train_dataset = cleaned_dataset[cleaned_dataset["Date"] < pd.Timestamp(day.date())]
    predictions = train_dataset["Value"][-30:].reset_index(drop=True)
    date_range = pd.date_range(start=pd.Timestamp(day.date()), periods=30, freq="D")
    smooth_predictions = predictions.rolling(window=3).mean()
    smooth_predictions = smooth_predictions.round(2)
    return pd.DataFrame(
        {
            "Date": date_range,
            "Prediction": predictions,
            "Smooth Prediction": smooth_predictions,
        }
    )


def evaluate(predictions, cleaned_dataset, day):
    print("     Evaluating")
    expected = cleaned_dataset.loc[
        cleaned_dataset["Date"] >= pd.Timestamp(day.date()), "Value"
    ][:30].reset_index(drop=True)
    mae = ((predictions["Prediction"] - expected) ** 2).mean()
    return int(mae)
