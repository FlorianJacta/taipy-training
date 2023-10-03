import taipy as tp
from config.config import scenario_cfg



if __name__=="__main__":
    tp.Core().run()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)

    scenario_1.input.write(10)
    scenario_2.input.write(8)

    scenario_1.submit()
    scenario_2.submit()
    
    print(tp.compare_scenarios(scenario_1, scenario_2))
