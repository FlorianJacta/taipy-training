from taipy import Config
import taipy as tp

def read_text(path: str) -> str:
    with open(path, 'r') as text_reader:
        data = text_reader.read()
    return data


def write_text(data: str, path: str) -> None:
    with open(path, 'w') as text_writer:
        text_writer.write(data)


historical_data_cfg = Config.configure_generic_data_node(
    id="historical_data",
    read_fct=read_text,
    write_fct=write_text,
    read_fct_args=["../data.txt"],
    write_fct_args=["../data.txt"])


scenario_cfg = Config.configure_scenario(id="my_scenario", additional_data_node_configs=[historical_data_cfg])

scenario = tp.create_scenario(scenario_cfg)
