######################################################################################
# calculates the average in x top of universities
######################################################################################

import googlemaps

import csv
import pandas as pd
import numpy

def calc(file, file1, file2):
    data = pd.read_csv(file)
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)

    n_average = []
    n_average1 = []
    n_average2 = []

    for score in data["overall"]:
        n_average.append(score)

    for score in data1["overall"]:
        n_average1.append(score)

    for score in data2["overall"]:
        n_average2.append(score)

    print('All 2016: ',numpy.average(n_average))
    print('All 2017: ',numpy.average(n_average1))
    print('All 2018: ',numpy.average(n_average2))



def calc2(file, file1, file2, top):
    data = pd.read_csv(file)
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)

    n_average = []
    n_average1 = []
    n_average2 = []


    for score in data["overall"][:top]:
        n_average.append(score)

    for score in data1["overall"][:top]:
        n_average1.append(score)

    for score in data2["overall"][:top]:
        n_average2.append(score)

    print('Top', top,':',round(numpy.average(n_average),1))
    print('Top', top,':',round(numpy.average(n_average1),1))
    print('Top', top,':',round(numpy.average(n_average2),1))

#     print(len(n_average), len(n_average1), len(n_average2))

data16 = "../DATA/ranking_with_country_2016.csv" #  800 uni's
data17 = "../DATA/ranking_with_country_2017.csv" #  981 uni's
data18 = "../DATA/ranking_with_country_2018.csv" # 1103 uni's


calc(data16,data17,data18)
print( '')
calc2(data16,data17,data18, 10)
print( '')
calc2(data16,data17,data18, 50)
print('')
calc2(data16,data17,data18, 100)
print( '')
calc2(data16,data17,data18, 200)
print( '')
calc2(data16,data17,data18, 300)
print( '')
calc2(data16,data17,data18, 400)
print( '')
calc2(data16,data17,data18, 500)
print( '')
calc2(data16,data17,data18, 600)
print( '')
calc2(data16,data17,data18, 700)
print( '')
calc2(data16,data17,data18, 800)
print( '')
calc2(data16,data17,data18, 900)
print( '')
calc2(data16,data17,data18, 1000)
print( '')
calc2(data16,data17,data18, 1103)
