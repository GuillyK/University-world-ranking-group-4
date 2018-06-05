import pandas as pd
import re
import csv

r = pd.read_csv('university_ranking_2016.csv')


df1 = pd.DataFrame(r,columns=['name'])
df2 = pd.DataFrame(data=None, columns=df1.columns)
l = []
for index, name in df1.iterrows():
    t = re.sub(r"(\w)([A-Z])", r"\1 \2", str(name))
    print(t)
    l.append([t])
    test = t.split("\t")

    #df2.append(t)


with open("out.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerows(l)
