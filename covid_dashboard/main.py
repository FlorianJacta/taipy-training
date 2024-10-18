from taipy.gui import Gui
import taipy as tp

from pages.country.country import country_md
from pages.map.map import map_md
from pages.predictions.predictions import predictions_md
from pages.root import root, selected_country, selector_country, to_text

from config.config import Config


pages = {
    '/':root,
    "Country":country_md,
    "Map":map_md,
    "Predictions":predictions_md
}


gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    tp.Core().run()
    
    gui_multi_pages.run(title="Covid Dashboard")
