import taipy as tp
from taipy.config import Config

import datetime as dt
import pandas as pd

#from config.config import scenario_cfg

def create_scenario(date: dt.datetime):
    scenario = tp.create_scenario(config=scenario_cfg, name="scenario_" + str(date.date()))
    scenario.day.write(date)
    tp.submit(scenario)
    return scenario



Config.load('config/config.toml')
scenario_cfg = Config.scenarios['scenario']

if __name__ == "__main__":
    tp.Core().run()
    print(tp.get_scenarios())
    
    my_first_scenario = create_scenario(dt.datetime(2021, 1, 25))
    
    predictions = my_first_scenario.predictions.read()
    print("Predictions\n",predictions)  
    
    for i in range(10):
        date = dt.datetime(2021, 1, 25) + dt.timedelta(days=i)
        create_scenario(date)

        
    maes = []
    names = []
    
    for scenario in tp.get_scenarios():
        evaluation = scenario.evaluation.read()
        print(f"\nscenario : {scenario.name}")
        print(f"Metric: {evaluation}")
    
        maes.append(evaluation)
        names.append(scenario.name)


    from taipy.gui import Gui
    df_metrics = pd.DataFrame({"Names": names, "MAE": maes})
    Gui("<|{df_metrics}|chart|x=Names|y=MAE|type=bar|>").run(port=4999)
