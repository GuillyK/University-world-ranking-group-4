import csv
import pandas as pd
import numpy

data = pd.read_csv("../DATA/ranking_with_country_2017.csv")
continent_find = pd.read_csv('../DATA/Countries-Continents.csv')

for country in data['country']:
    counter = 0
    for country_check in continent_find['Country']:
        check = False
        if country == country_check:
            check = True
            print(continent_find['Continent'][counter])
        counter += 1

    if check == False:
        print('none')
    # data.set_value(counter, "continent", continent)
    
# data.to_csv("../DATA/ranking_with_country_2017.csv", index=False)