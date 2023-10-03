from taipy.gui import Gui
import taipy as tp

from pages.data_viz import historical
from pages.predictions import predictions, scenario

ticker = 'AAPL'

pages = {"/":"<|navbar|>",
         "Historical":historical,
         "Prediction":predictions}

tp.Core().run()
Gui(pages=pages).run(port=5001)