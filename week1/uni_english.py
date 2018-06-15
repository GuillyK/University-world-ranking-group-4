import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import DataRange1d
import numpy as np
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, HoverTool, LinearColorMapper


data = pd.read_csv('../DATA/ranking_with_country_2018.csv')


english = ['Australia','Canada', 'New Zealand', 'United Kingdom', 'United States', 'Ireland']
eng_unis = []

for country in english:
        name = data.loc[data['country'] == country, 'name'].values
        eng_unis.append(list(name))

english_spoken = []
for i in eng_unis:
    for j in i:
        english_spoken.append(j)
#print(eng_unis)
print(english_spoken)

counter = 0
for uni in data['name']:
    if uni in english_spoken:
        data['english_spoken'][counter] = '1'
        print('1')
    else:
        data['english_spoken'][counter] = '0'
        print('0')
    counter += 1

    data.to_csv("../DATA/ranking_with_country_2018.csv", index=False)