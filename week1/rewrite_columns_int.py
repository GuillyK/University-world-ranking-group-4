import csv
import pandas as pd
import numpy
import math

data = pd.read_csv("University-world-ranking-group-4/DATA/ranking_with_country_2018.csv")
ch_data = pd.read_csv('ranking_2018_with_int.csv')
continent_data = pd.read_csv('University-world-ranking-group-4/DATA/Countries-Continents.csv')
# data_2018 = pd.read_csv('ranking_2016_with_int.csv')
# CHANGE SIZE TO INT
# c_counter = 0
# for size in data['size']:
#     if size == 'small':
#         print('0')
#         ch_data['size'][c_counter] = 0
#     elif size == 'medium':
#         print('1')
#         ch_data['size'][c_counter] = 1
#     elif size == 'large':
#         print('2')
#         ch_data['size'][c_counter] = 2
#     else:
#         print('kut')
#     c_counter += 1
# ch_data.to_csv("ranking_2017_with_int.csv", index=False)


# ADD NUMBERS FOR UNI NAMES 2018 ONLY
# c_counter = 0
# for name in data['name']:
#     print(c_counter)
#     ch_data['number_name'][c_counter] = c_counter
#     c_counter += 1
# ch_data.to_csv("ranking_2018_with_int.csv", index=False)


# ADD NUMBERS FOR UNIS 2016 / 2017
# c_counter = 0
# for name in data['name']:
#     print(c_counter)
#     counter_2018 = 0
#     check = False
#     # ch_data['number_name'][c_counter] = '0'
#     for name_2018 in data_2018['name']:
        
#         if name == name_2018:
#             print(data_2018['number_name'][counter_2018])
#             ch_data['number_name'][c_counter] = data_2018['number_name'][counter_2018]
#             check = True
#         counter_2018 += 1
#     if check == False:
#         ch_data['number_name'][c_counter] = 'none'
        
#     c_counter += 1
# ch_data.to_csv("ranking_2016_with_int.csv", index=False)

# ADD NUMBERS FOR COUNTRIES
# counter = 0
# for country in continent_data['Country']:
#     print(counter, country)
#     continent_data['Number_country'][counter] = counter
#     counter += 1
# continent_data.to_csv('University-world-ranking-group-4/DATA/Countries-Continents.csv', index=False)

# counter = 0
# for country in data['country']:
#     con_counter = 0
#     for country_check in continent_data['Country']:
#         if country == country_check:
#             ch_data['country'][counter] = continent_data['Number_country'][con_counter]
#             print(continent_data['Number_country'][con_counter])
#         con_counter += 1
#     counter += 1
# ch_data.to_csv("ranking_2016_with_int.csv", index=False)


# counter = 0
# for continent in continent_data['Continent']:
#     if continent == 'Africa':
#         continent_data['Number_continent'][counter] = 0
#     elif continent == 'Asia':
#         continent_data['Number_continent'][counter] = 1
#     elif continent == 'Europe':
#         continent_data['Number_continent'][counter] = 2
#     elif continent == 'North America':
#         continent_data['Number_continent'][counter] = 3
#     elif continent == 'Oceania':
#         continent_data['Number_continent'][counter] = 4
#     elif continent == 'South America':
#         continent_data['Number_continent'][counter] = 5
#     counter += 1
# continent_data.to_csv('University-world-ranking-group-4/DATA/Countries-Continents.csv', index=False)

counter = 0
for continent in data['continent']:
    con_counter = 0
    for continent_check in continent_data['Continent']:
        if continent == continent_check:
            ch_data['continent'][counter] = continent_data['Number_continent'][con_counter]
            print(continent_data['Number_continent'][con_counter], data['rank'][con_counter])
            break
        con_counter += 1
    counter += 1
ch_data.to_csv("ranking_2018_with_int.csv", index=False)
