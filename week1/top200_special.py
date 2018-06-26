######################################################################################
#special code to only look at attributes of the top 200

######################################################################################

import googlemaps
import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt

data = pd.read_csv("ranking_with_country_2016.csv")
data1 = pd.read_csv("ranking_with_country_2017.csv")
data2 = pd.read_csv("ranking_with_country_2018.csv")

# counter = 0
# for teaching in data['teaching']:
#     if counter < 200:
#         print(teaching)
#         # print(data['country']==teaching)
#     else:
#         break
#     counter+=1
teaching = []
for i in range(200):
    print(data['country'][i] ,data['teaching'][i])
    if teaching == []
        teaching.append[]

# print(len(data))
