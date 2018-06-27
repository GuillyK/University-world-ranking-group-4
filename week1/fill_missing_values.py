######################################################################################
# searches for missing values and fills them in with a given value

######################################################################################
import csv
import pandas as pd
import numpy
import math

data = pd.read_csv("../DATA/ranking_with_country_2018.csv")

with open("../DATA/ranking_with_country_2018.csv") as out:
    counter = 0
    for ratio in data['ratio']:
        # print(ratio)
        #print(type(ratio))
        if math.isnan(ratio):
            data.at[data.index[counter], 'ratio'] = 49
        counter += 1

    data.to_csv("../DATA/ranking_with_country_2018.csv", index=False)
