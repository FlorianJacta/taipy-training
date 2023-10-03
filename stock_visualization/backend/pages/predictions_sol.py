import taipy as tp 
from taipy.gui import notify, Markdown
import datetime as dt

tp.Config.load("config/config.toml")


ticker = 'AAPL'
scenario = None
default_data = {"Date":[0], "Predictions":[0]}

predictions = Markdown("""
<|{scenario}|scenario_selector|> 

### **Daily**{: .color-primary} Predictions <|{scenario.ticker.read() if scenario else ticker}|toggle|lov=MSFT;GOOG;AAPL|active={scenario}|on_change=save|>

<|layout|columns=5 2|
<|{scenario}|scenario|> 

<|Refresh|button|on_action={lambda s: s.assign("scenario", scenario)}|>
|>

<|{show_preditions(scenario)}|chart|x=Date|y=Predictions|>

<|{show_preditions(scenario)}|chart|x=Date|y=Predictions|type=bar|>
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