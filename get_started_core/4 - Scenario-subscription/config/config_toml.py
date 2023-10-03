from taipy import Config


Config.load('config/config_09.toml')
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

# my_scenario is the id of the scenario configured
scenario_cfg = Config.scenarios['my_scenario']