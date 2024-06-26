import numpy as np

from taipy.gui import Gui

from pages.country import country_md, on_change_country,\
                          selected_representation, data_country_date, pie_chart
from pages.world import world_md
from pages.map import map_md
from pages.predictions import predictions_md, selected_scenario, result, scenario_country, scenario_date

from data.data import data

selector_country = list(np.sort(data['Country/Region'].astype(str).unique()))
selected_country = 'France'

pages = {
    "/":"<center><|navbar|></center>",
    "Country":country_md,
    "World":world_md,
    "Map":map_md,
    "Predictions":predictions_md
}


if __name__ == '__main__':
    gui_multi_pages = Gui(pages=pages)

    gui_multi_pages.run(title="Covid Dashboard",
    		            dark_mode=False,
                        use_reloader=False,
                        port=5039)