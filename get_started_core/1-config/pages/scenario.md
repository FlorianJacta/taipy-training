<|1 3 4|layout|
<|{scenario}|scenario_selector|>

**Day of prediction**
<|{scenario.day if scenario else None}|data_node|>

**Scenario**
<|{scenario}|scenario|>
|>

<|job_selector|>
<|{scenario}|scenario_dag|>