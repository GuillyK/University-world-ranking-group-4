######################################################################################
# preproccessing of names.
# splits name and country so country could be in its own columm

######################################################################################

import googlemaps

import pandas as pd
import re
import csv

r = pd.read_csv('university_ranking_2016.csv')


df1 = pd.DataFrame(r,columns=['name'])
df2 = pd.DataFrame(data=None, columns=df1.columns)
list = []
for index, name in df1.iterrows():
    test = name["name"]

    t = re.sub(r"(\w)([A-Z])", r"\1 \2", test)
    list = list + [[t]]
    print(list)



with open("out.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerows(list)
