import taipy as tp 
from taipy.gui import notify, Markdown
import datetime as dt

tp.Config.load("config/config.toml")

ticker = 'AAPL'
scenario = None
data_node = None

default_data = {"Date":[0], "Predictions":[0]}

def on_submission_status_change(state, submittable, details):
    submission_status = details.get('submission_status')

    if submission_status == 'COMPLETED':
        print(f"{submittable.name} has completed.")
        notify(state, 'success', 'Completed!')
        state.refresh('scenario')

    elif submission_status == 'FAILED':
        print(f"{submittable.name} has failed.")
        notify(state, 'error', 'Completed!')

predictions = Markdown("""
Put a scenario selector 
                       
### **Daily**{: .color-primary} Predictions <|{scenario.ticker.read() if scenario else ticker}|toggle|lov=MSFT;GOOG;AAPL|active={scenario}|on_change=save|>

Put a scenario viewer
                       
<|{show_preditions(scenario)}|chart|x=Date|y=Predictions|>

<|1 5|layout|
Put a Data Node selector
                       
Put a Data Node
|>
""")

def show_preditions(scenario):
    if scenario and scenario.predictions.read() is not None:
        print(scenario)
        return scenario.predictions.read()
    else:
        return default_data

def save(state, var_name, var_value):
    state.scenario.ticker.write(var_value)
    state.scenario.date.write(dt.date.today())
    notify(state, "success", 'Parameters saved: ready for submission!')
    state.scenario.predictions.write(None)
    state.scenario = state.scenario