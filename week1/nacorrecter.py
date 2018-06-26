######################################################################################
#??

######################################################################################

import googlemaps

import csv
import pandas as pd
import numpy

data = pd.read_csv("../DATA/ranking_with_country_2018.csv)

#for ratio in data['ratio']:
    #print(ratio)

# with open("ranking_with_country_2016.csv") as out:
#     counter = 0
#     for ratio in data['ratio']:
#         print(ratio)
#         #print(type(ratio))
#         if type(ratio) == float:
#             data.set_value(counter, "ratio", None)
#         counter += 1

#     data.to_csv("ranking_with_country_2016.csv", index=False)

# counter = 0
# for ratio in data['ratio']:
#     print(ratio)
#     if type(ratio)is not float:
#         print(ratio[:2])
#         data.set_value(counter, "ratio", ratio[:2])
#     counter+=1
# data.to_csv("ranking_with_country_2018.csv", index=False)


import csv
import pandas as pd
import numpy
import math


next_data = pd.read_csv('ranking_with_country_2017.csv')
next2_data = pd.read_csv('ranking_with_country_2018.csv')
def nan_checker(file, nan_column, output_column):
    data = pd.read_csv(file)

    with open(file) as out:
        counter = 0

        for value in data[nan_column]:
            counter2 = 0
            counter3 = 0
            if math.isnan(value):
                uni1 = data[output_column][counter]
                for same in next_data['name']:

                    if same == uni1:
                        print(same, uni1)
                        print(next_data['ratio'][counter2])

                    counter2 += 1
                #print(next_data[])

                for same2 in next2_data['name']:

                    if same2 == uni1:
                        print(same2, uni1)
                        print(next2_data['ratio'][counter3])

                    counter3 += 1
                print('--------------------------------')
            counter += 1


nan_checker("ranking_with_country_2016.csv", "ratio", "name")
