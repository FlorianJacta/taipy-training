from taipy import Config
from algos.algos import *

# Configuration of Data Nodes
input_cfg = Config.configure_data_node("input", default_data=21)
intermediate_cfg = Config.configure_data_node("intermediate")
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



def compare_function(*data_node_results):
    # example of function
    compare_result = {}
    current_res_i = 0
    for current_res in data_node_results:
        compare_result[current_res_i] = {}
        next_res_i = 0
        for next_res in data_node_results:
            print(f"comparing result {current_res_i} with result {next_res_i}")
            compare_result[current_res_i][next_res_i] = next_res - current_res
            next_res_i += 1
        current_res_i += 1
    return compare_result


scenario_cfg = Config.configure_scenario(id="multiply_scenario",
                                                    name="my_scenario",
                                                    task_configs=[first_task_cfg, second_task_cfg],
                                                    comparators={output_cfg.id: compare_function})

Config.export("config_08.toml")