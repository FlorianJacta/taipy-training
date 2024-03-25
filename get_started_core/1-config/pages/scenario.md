<|1 3 4|layout|
<|{scenario}|scenario_selector|>

**Prediction Start Date**
<|{scenario.day if scenario else None}|data_node|>

**Scenario**
<|{scenario}|scenario|show_properties=False|show_sequences=False|>
|>

<|job_selector|show_submitted_label=False|>
<|{scenario}|scenario_dag|>