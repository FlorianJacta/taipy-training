from taipy import Config
from algos.algos import *

Config.configure_job_executions(mode="standalone", max_nb_of_workers=2)

# Configuration of Data Nodes
input_cfg = Config.configure_data_node("input", default_data=21)
intermediate_cfg = Config.configure_data_node("intermediate", default_data=21)
output_cfg = Config.configure_data_node("output")

# Configuration of tasks
first_task_cfg = Config.configure_task("double",
                                       double,
                                       input_cfg,
                                       intermediate_cfg)

second_task_cfg = Config.configure_task("add",
                                        add,
                                        intermediate_cfg,
                                        output_cfg)

# Configuration of the pipeline and scenario
scenario_cfg = Config.configure_scenario(id="my_scenario",
                                                    task_configs=[first_task_cfg,
                                                                  second_task_cfg])

Config.export("config_07.toml")