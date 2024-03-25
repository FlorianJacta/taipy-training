import taipy as tp

import datetime as dt

from config.config import *

def create_and_run_scenario(date: dt.datetime):
    scenario = tp.create_scenario(config=scenario_cfg,
                                  name=f"scenario_{date.date()}",
                                  creation_date=date)
    scenario.day.write(date)
    tp.submit(scenario)
    return scenario

if __name__ == "__main__":
    tp.Core().run()
    
    my_first_scenario = create_and_run_scenario(dt.datetime(2021, 1, 25))
    
    predictions = my_first_scenario.predictions.read()
    print("Predictions\n", predictions)
    
    