import taipy as tp 
from taipy.gui import notify, Markdown
import datetime as dt

tp.Config.load("config/config.toml")

scenario = None
default_data = {"Date":[0], "Predictions":[0]}

predictions = Markdown("""
<|{scenario}|scenario_selector|>

### **Daily** Predictions
<|{ticker}|toggle|lov=MSFT;GOOG;AAPL|on_change=save|>

<|layout|columns=5 2|
<|{scenario}|scenario|>

<|Refresh|button|on_action={lambda s: s.assign("scenario", scenario)}|>
|>

<|{show_preditions(scenario)}|chart|x=Date|y=Predictions|>
""")

def show_preditions(scenario):
    if scenario is not None and scenario.predictions.read() is not None:
        return scenario.predictions.read()
    else:
        return default_data

def save(state, var_name, var_value):
    state.scenario.ticker.write(state.ticker)
    state.scenario.date.write(dt.date.today())
    state.scenario.predictions.write(None)
    state.scenario = state.scenario
    notify(state, "success", 'Parameters saved: ready for submission!')