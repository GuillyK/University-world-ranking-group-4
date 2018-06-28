######################################################################################
#calculates average when given a csv and a columm of wich you want to know the average.

######################################################################################
import csv
import pandas as pd
import numpy
import math

def calculate_average(file, column):
    data = pd.read_csv(file)
    all_ratios = []
    for ratio in data[column]:
        if not math.isnan(ratio):
            all_ratios.append(ratio)
    mean = numpy.mean(all_ratios)
    print(file , mean)



calculate_average('../DATA/ranking_with_country_2016.csv', 'ratio')
calculate_average('../DATA/ranking_with_country_2017.csv', 'ratio')
calculate_average('../DATA/ranking_with_country_2018.csv', 'ratio')
