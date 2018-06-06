import csv
import pandas as pd
import numpy

data = pd.read_csv("university_ranking_2016.csv")
counter = 0
for number in data['fte_students']:
    if number <= 5000:
        size = 'small'
        print('small')
    elif number > 5000 and number <= 15000:
        size = 'medium'
        print('medium')
    elif number > 15000:
        size = 'large'
        print('big')
    data.set_value(counter, "size", size)
    counter += 1
data.to_csv("university_ranking_2016.csv", index=False)