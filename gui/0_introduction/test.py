from taipy.gui import Gui
from math import cos, exp

value = 10

page = """
Markdown
# Taipy *Demo*

<|layout|columns=1 1 1 1|
Text: <|{value*2}|text|>
lekjfnsdlkfn
mek,sflk

<|{value}|slider|>

<|{value}|input|>

<|{compute_data(value)}|chart|>
|>
"""


def compute_data(decay:int)->list:
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

 

Gui(page).run(use_reloader=True, port=5002)