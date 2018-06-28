######################################################################################
# adds an extra columm to the csv called country_int witch gives each country a index
# this code isnt in final product
######################################################################################
import csv
import pandas as pd
import numpy
import math

data = pd.read_csv("../DATA/ranking_with_country_2017.csv")
data_int = pd.read_csv("../DATA/ranking_2017_with_int.csv")

counter = 0
for country in data['country']:
    data['country_int'][counter] = data_int['country'][counter]
    counter += 1



data.to_csv("../DATA/ranking_with_country_2017.csv", index=False)
