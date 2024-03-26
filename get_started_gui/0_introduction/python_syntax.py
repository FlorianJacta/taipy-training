from taipy.gui import Gui 
import taipy.gui.builder as tgb
from math import cos, exp

value: int = 10

def compute_data(decay:int)->list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

data: list  = compute_data(value)

with tgb.Page() as page:
    tgb.text(value="# Taipy Demo", mode="md")
    tgb.text(value="Value: {value}")
    tgb.slider(value="{value}")
    tgb.chart(data="{compute_data(value)}") 


Gui(page=page).run(title="Frontend Demo", port=1001)

