######################################################################################
#calculates average score of a country for every year and the deviation between these
# calculates deviation per country and plots it against the overall scores as a scatter plot
# with a trend line in it.

######################################################################################
import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.close

def meanscorer(university, dataset):
        score = data.loc[dataset['country'] == university, ['overall']]
        return(score['overall'].mean())

data = pd.read_csv("../DATA/ranking_with_country_2016.csv")
data1 = pd.read_csv("../DATA/ranking_with_country_2017.csv")
data2 = pd.read_csv("../DATA/ranking_with_country_2018.csv")

#for ratio in data['ratio']:
    #print(ratio)

countrylist = []
deviationlist = []
meancountrylist = []
topdeviation = 0

for country in data['country']:
    if country not in countrylist:
        countrylist = countrylist + [country]

        meancountryscore2016 = meanscorer(country, data)
        meancountryscore2017 = meanscorer(country, data1)
        meancountryscore2018 = meanscorer(country, data2)
        meanlist = [meancountryscore2016] + [meancountryscore2017] + [meancountryscore2018]
        meancountryoverall = pd.Series(meanlist)
        meancountry = meancountryoverall.mean()
        meancountrylist = meancountrylist + [meancountry]
        deviationoverall = meancountryoverall.std()
        deviationlist = deviationlist + [deviationoverall]
        if deviationoverall > topdeviation:
            topdeviation = deviationoverall
            print(country, '2016 =' ,meancountryscore2016)
            print(country, '2017 =' ,meancountryscore2017)
            print(country, '2018 =' ,meancountryscore2018)
            print("overall deviation for", country, ' = ', deviationoverall)

    #print(studentsperstaff)
#plt.scatter(meancountrylist, deviationlist )
#plt.show()

print(meancountrylist)
print(deviationlist)
