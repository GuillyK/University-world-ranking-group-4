######################################################################################
# calculates amount of universities in off a country that are in the timeshighereducation
# top 1000
# calculates percentage top1000 universities per country aswell

######################################################################################

import googlemaps

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
allunis = pd.read_csv("../DATA/alluniversities.csv")

#for ratio in data['ratio']:
    #print(rat

countrylist = []
university1000list = []
for university in data['name']:
    if university not in university1000list:
        university1000list = university1000list + [university]
print(university1000list)

for country in allunis['afkorting']:
    if country not in countrylist:
        countrylist = countrylist + [country]

precentagelist = []
countrylist2 = []
for country in countrylist:
    counter1000 = 0
    totalcounter = 0
    universityincountry = allunis.loc[allunis['afkorting'] == country , ['university']]
    for university in universityincountry['university']:
        totalcounter += 1
        if university in university1000list:
            counter1000 += 1
        precentage = counter1000/ totalcounter * 100

    if counter1000 is not 0:
        print (country, counter1000 ,'/', totalcounter,'=', precentage)
        precentagelist = precentagelist + [precentage]
        countrylist2 = countrylist2 + [country]
        print(len(precentagelist))
        print(len(countrylist2))


#meancountryscore2016 = meanscorer(country, data)
#meancountryscore2017 = meanscorer(country, data1)
#meancountryscore2018 = meanscorer(country, data2)
#meanlist = [meancountryscore2016] + [meancountryscore2017] + [meancountryscore2018]
#print(country, '2016 =' ,meancountryscore2016)
#print(country, '2017 =' ,meancountryscore2017)
#print(country, '2018 =' ,meancountryscore2018)
#3meancountryoverall = pd.Series(meanlist)
#deviationoverall = meancountryoverall.std()
#print("overall deviation for", country, ' = ', deviationoverall)

#print(studentsperstaff)
plt.scatter(precentagelist, countrylist2 )
plt.show()
