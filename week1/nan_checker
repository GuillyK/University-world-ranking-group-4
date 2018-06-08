import csv
import pandas as pd
import numpy
import math


def nan_checker(file, nan_column, output_column):
    data = pd.read_csv(file)

    with open(file) as out:
        counter = 0
        for value in data[nan_column]:
            if math.isnan(value):
                print(data[output_column][counter])
            counter += 1

        
nan_checker("ranking_with_country_2018.csv", "international_students", "name")
