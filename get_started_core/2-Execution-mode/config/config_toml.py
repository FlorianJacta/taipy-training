from taipy import Config 
from algos.algos import *

Config.load('config/config_07.toml')
Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)
scenario_cfg = Config.scenarios['my_scenario']

