
import numpy as np
from taipy.gui import Markdown
import plotly.express as px

from data.data import data, geojson, vaccination


def initialize_map(data):
    data['Province/State'] = data['Province/State'].fillna(data["Country/Region"])
    data_province = data.groupby(["Country/Region",
                                  'Province/State',
                                  'Longitude',
                                  'Latitude'])\
                         .max()
                         

    data_province_displayed = data_province[data_province['Deaths']>10].reset_index()

    # Size when using Taipy charts
    # data_province_displayed['Size'] = np.sqrt(data_province_displayed.loc[:,'Deaths']/data_province_displayed.loc[:,'Deaths'].max())*80 + 3
    # data_province_displayed['Text'] = data_province_displayed.loc[:,'Deaths'].astype(str) + ' deaths </br> ' + data_province_displayed.loc[:,'Province/State']

    # Size when using Plotly Python
    data_province_displayed['Size'] = ((data_province_displayed.loc[:,'Deaths']/data_province_displayed.loc[:,'Deaths'].max()) * 100) + 0.1
    return data_province_displayed


data_province_displayed = initialize_map(data)


map_md = Markdown("pages/map/map.md")