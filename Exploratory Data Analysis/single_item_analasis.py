import csv
import pandas as pd
import matplotlib.pyplot as plt
plt.close


data = pd.read_csv("../DATA/ranking_with_country_2018.csv")
var = data['country'].sort_values(ascending = False)
print(var)
#plt.hist(var, cumulative = True, density = True)
plt.plot(var)
plt.savefig('country_hist.png')
plt.show()
