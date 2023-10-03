import taipy as tp

from taipy.gui import Markdown

from config.config import *

scenario = None
df_metrics = None
data_node = None


pages = {'/':'<|navbar|> <|toggle|theme|> <br/>',
         'Scenario': Markdown('pages/scenario.md'),
         'Data-Node': Markdown('pages/data_node.md')}


if __name__ == "__main__":
    tp.Core().run()
    tp.Gui(pages=pages).run(port=4999)