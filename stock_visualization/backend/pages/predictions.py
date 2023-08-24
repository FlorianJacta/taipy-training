import taipy as tp 
from taipy.gui import notify, Markdown
import datetime as dt

tp.Config.load("config/config.toml")

scenario = None
default_data = {"Date":[0], "Predictions":[0]}

predictions = Markdown("""
[put scenario selector]

### **Daily**{: .color-primary} Predictions
[put toggle to choose from MSFT;GOOG;AAPL]

<|layout|columns=5 2|
[put scenario]

<|Refresh|button|on_action={lambda s: s.assign("scenario", scenario)}|>
|>

<|{show_preditions(scenario)}|chart|x=Date|y=Predictions|>
""")

def show_preditions(scenario):
    return default_data

def save(state, var_name, var_value):
    # write ticker
    # write date
    # write predictions to None
    # refresh scenario
    notify(state, "success", 'Parameters saved: ready for submission!')