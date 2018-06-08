import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.close

def meanscorer(university, dataset):
        score = data.loc[dataset['name'] == university, ['overall']]

        return(score['overall'].mean())

data = pd.read_csv("ranking_with_country_2016.csv")
data1 = pd.read_csv("ranking_with_country_2017.csv")
data2 = pd.read_csv("ranking_with_country_2018.csv")

#for ratio in data['ratio']:
    #print(ratio)



def listmaker(data):
    universitylist = []
    for uni in data['name']:
        universitylist = universitylist + [uni]
    return(universitylist)

list = listmaker(data)
list1 = listmaker(data1)
list2 = listmaker(data2)


meanlist = []
meanlist1 = []
meanlist2 = []
for university in list:
    if university in list1:
        if university in list2:
            mean = meanscorer(university, data)
            mean1 = meanscorer(university, data1)
            mean2 = meanscorer(university, data2)
            meanlist = meanlist + [mean]
            meanlist1 = meanlist1 + [mean1]
            meanlist2 = meanlist2 + [mean2]
meanlist.mean()
        #meancountryscore2016 = meanscorer(country, data)
        ##meancountryscore2017 = meanscorer(country, data1)
        #eancountryscore2018 = meanscorer(country, data2)
        #meanlist = [meancountryscore2016] + [meancountryscore2017] + [meancountryscore2018]
        #print(country, '2016 =' ,meancountryscore2016)
        #print(country, '2017 =' ,meancountryscore2017)
        #print(country, '2018 =' ,meancountryscore2018)
        #meancountryoverall = pd.Series(meanlist)
        #deviationoverall = meancountryoverall.std()
        #print("overall deviation for", country, ' = ', deviationoverall)

    #print(studentsperstaff)
    #plt.scatter(studentlist, studentsperstaff)
    #plt.show()
