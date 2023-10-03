from taipy.gui import Gui, notify

import pandas as pd

path = ""
data = None

historical = """
<|{data}|table|rebuild|>

<|{path}|file_selector|on_action=upload|>
"""

def upload(state):
    state.data = pd.read_csv(state.path)


Gui(historical).run()