import csv
import pandas as pd
import numpy

data = pd.read_csv("university_ranking_2016.csv")

#for ratio in data['ratio']:
    #print(ratio)

with open("university_ranking_2016.csv") as out:
    counter = 0
    for ratio in data['ratio']:
        print(ratio)
        #print(type(ratio))
        if type(ratio) == float:
            data.set_value(counter, "ratio", None)
        counter += 1

    data.to_csv("test.csv", index=False)


