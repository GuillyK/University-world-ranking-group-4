import csv
import pandas as pd
import numpy
import math


next_data = pd.read_csv('../data/ranking_with_country_2017.csv', encoding = 'utf-8')
next2_data = pd.read_csv('../data/ranking_with_country_2018.csv')
def nan_checker(file, nan_column, output_column):
    data = pd.read_csv(file)
    nan_list = []
    with open(file) as out:
        counter = 0
        
        for value in data[nan_column]:
            counter2 = 0
            counter3 = 0
            if math.isnan(value):
                uni1 = data[output_column][counter]
                for same in next_data[output_column]:
                    
                    if same == uni1:
                        print(same, uni1)
                        print(next_data[nan_column][counter2])
                        nan = next_data[nan_column][counter2]
                    counter2 += 1
                #print(next_data[])
               
                for same2 in next2_data[output_column]:
                    
                    if same2 == uni1:
                        print(same2, uni1)
                        print(next2_data[nan_column][counter3])
                        nan2 = next2_data[nan_column][counter3]
                    counter3 += 1
                if math.isnan(nan) and math.isnan(nan2):
                    nan_list.append(uni1)
                print('--------------------------------')
            
            counter += 1
        print(nan_list)

        
nan_checker("../data/ranking_with_country_2016.csv", "ratio", "name")
