import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.close


data = pd.read_csv("../DATA/ranking_with_country_2018.csv")
var = data['teaching'].sort_values(ascending = True)
print(var)
#plt.hist(var, cumulative = True, density = True)
plt.hist(var)
plt.savefig('teaching_score_hist.png')
plt.show()
