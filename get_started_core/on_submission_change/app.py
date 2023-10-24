import taipy as tp

from taipy.gui import Markdown

from config.config import *
from pages.scenario.scenario import scenario_md

import pages.scenario.scenario as scenario

df_metrics = None
data_node = None

def on_init(state):
    scenario.init(state)

pages = {'/':'<|navbar|> <|toggle|theme|> <br/>',
         'Scenario': scenario_md,
         'Data-Node': Markdown('pages/data_node.md')}


if __name__ == "__main__":
    tp.Core().run()
    tp.Gui(pages=pages).run(port=4999)