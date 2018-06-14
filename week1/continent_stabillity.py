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
countries = pd.read_csv("../DATA/Countries-Continents.csv")

#for ratio in data['ratio']:
    #print(ratio)

countrylist = []
continentlist = {}
counter = {}
for country in data['country']:
    if country not in countrylist:
        countrylist = countrylist + [country]
        #print(country)
        dictonary = countries.to_dict('split')
        meancountryscore2016 = meanscorer(country, data)
        meancountryscore2017 = meanscorer(country, data1)
        meancountryscore2018 = meanscorer(country, data2)

        for continent in dictonary['data']:
            if country in continent:
                if continent[0] not in continentlist:
                    counter[continent[0]] = 1
                    continentlist[continent[0]] = meancountryscore2016
                    #print(continentlist)
                else:
                    counter[continent[0]] += 1
                    #print(continentlist[continent[0]])
                    nummer = int(meancountryscore2016) +  continentlist[continent[0]]
                    continentlist[continent[0]] = nummer
                    #print(continentlist)
                    #print(counter)
for continent in counter:
    nummerofcountries = counter[continent]
    scoreofcontinent  = continentlist[continent]
    averagecontinentscore = scoreofcontinent / nummerofcountries
    print(continent, 'score' , averagecontinentscore)

#        meanlist = [meancountryscore2016] + [meancountryscore2017] + [meancountryscore2018]
#        print(country, '2016 =' ,meancountryscore2016)
#        print(country, '2017 =' ,meancountryscore2017)
#        print(country, '2018 =' ,meancountryscore2018)
#        meancountryoverall = pd.Series(meanlist)
#        deviationoverall = meancountryoverall.std()
#        print("overall deviation for", country, ' = ', deviationoverall)

    #print(studentsperstaff)
    #plt.scatter(studentlist, studentsperstaff)
    #plt.show()
