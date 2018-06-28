######################################################################################
#calculates average score of a university for every year and the deviation between these
#scores
# calculates deviation per university and plots it against the overall scores as a
# scatter plot with a trend line in it.

######################################################################################

import googlemaps
import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.close

def meanscorer(university, dataset):
        score = data.loc[dataset['name'] == university, ['overall']]
        return(score['overall'].mean())

data = pd.read_csv("../DATA/ranking_with_country_2016.csv")
data1 = pd.read_csv("../DATA/ranking_with_country_2017.csv")
data2 = pd.read_csv("../DATA/ranking_with_country_2018.csv")

#for ratio in data['ratio']:
    #print(ratio)

countrylist = []
deviationlist = []
meancountrylist = []
universitylist = []
topdeviation = 0

for university in data['name']:
        universitylist = universitylist + [university]

        meanuniversityscore2016 = meanscorer(university, data)
        meanuniversityscore2017  = meanscorer(university, data1)
        meanuniversityscore2018  = meanscorer(university, data2)
        meanlist = [meanuniversityscore2016] + [meanuniversityscore2017] + [meanuniversityscore2018]
        meancountryoverall = pd.Series(meanlist)
        meancountry = meancountryoverall.mean()
        meancountrylist = meancountrylist + [meancountry]
        deviationoverall = meancountryoverall.std()
        deviationlist = deviationlist + [deviationoverall]
        if deviationoverall > topdeviation:
            topdeviation = deviationoverall
            print(university, '2016 =' ,meanuniversityscore2016)
            print(university, '2017 =' ,meanuniversityscore2017)
            print(university, '2018 =' ,meanuniversityscore2018)
            print("overall deviation for", university, ' = ', deviationoverall)

    #print(studentsperstaff)
#plt.scatter(meancountrylist, deviationlist )
#plt.show()

#print(meancountrylist, '\n')
#print(deviationlist)
