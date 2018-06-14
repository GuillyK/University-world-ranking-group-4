import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.close


data = pd.read_csv("../DATA/ranking_with_country_2018.csv")
var = data['fte_students']
var1 = data['international_students']
print(var)
plt.scatter(var, var1)
#plt.hist(var)
plt.savefig('fte_students_international_students_scatter.png')
plt.show()
