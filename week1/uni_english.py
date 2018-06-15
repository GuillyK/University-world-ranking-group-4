import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DataRange1d
import numpy as np
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper


data = pd.read_csv('../DATA/ranking_with_country_2017.csv')


english = ['Australia','Canada', 'New Zealand', 'United Kingdom', 'United States', 'Ireland']
eng_unis = []

for country in english:
        name = data.loc[data['country'] == country, 'name'].values
        eng_unis.append(list(name))
print(eng_unis)