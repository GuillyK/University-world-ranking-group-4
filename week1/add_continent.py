import csv
import pandas as pd
import numpy

data = pd.read_csv("../DATA/ranking_with_country_2017.csv")
continent_find = pd.read_csv('../DATA/Countries-Continents.csv')

c_counter = 0
for country in data['country']:
    counter = 0
    check = False

    for country_check in continent_find['Country']:
        if country == country_check:
            check = True
            data['continent'][c_counter] = continent_find['Continent'][counter]
            print(continent_find['Continent'][counter])
        counter += 1
    c_counter += 1
    if check == False:
        print('none')
    
    # data.set_value(counter, "continent", continent)
    
data.to_csv("../DATA/ranking_with_country_2017.csv", index=False)