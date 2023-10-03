from config.config import scenario_cfg
from taipy.core import Status
import taipy as tp


def callback_scenario_state(scenario, job):
    """All the scenarios are subscribed to the callback_scenario_state function. It means whenever a job is done, it is called.
    Depending on the job and the status, it will update the message stored in a json that is then displayed on the GUI.

    Args:
        scenario (Scenario): the scenario of the job changed
        job (_type_): the job that has its status changed
    """
    print(scenario.name)
    if job.status == Status.COMPLETED:
        for data_node in job.task.output.values():
            print(data_node.read())



if __name__=="__main__":
    tp.Core().run()
    scenario_1 = tp.create_scenario(scenario_cfg)
    scenario_1.subscribe(callback_scenario_state)

    scenario_1.submit(wait=True)
    
    tp.Rest().run()


