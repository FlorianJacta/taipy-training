import taipy as tp

from config.config import scenario_cfg

if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_2 = tp.create_scenario(scenario_cfg)
    scenario_1.submit()
    scenario_2.submit()

    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.submit(wait=True)
    scenario_1.submit(wait=True, timeout=5)
