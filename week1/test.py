import csv
import pandas as pd
import numpy
import matplotlib.pyplot as plt
plt.close

def scorer(university, dataset):
        score = data.loc[dataset['country'] == university, ['overall']]
        print(score)
        score = score.iloc[0]['overall']
        return(score)

data = pd.read_csv("ranking_with_country_2016.csv")
data1 = pd.read_csv("university_ranking_2017.csv")
data2 = pd.read_csv("university_ranking_2018.csv")

#for ratio in data['ratio']:
    #print(ratio)
print(data)
counter = 0
counter1 = 0
#for country in data['country']:
#    print(country)
    #score2016 = scorer(country, data)
            #score2017 = scorer(university, data1)
            #score2018 = scorer(university, data2)
            #print(university, ' 2016=' ,score2016)
            #print(university, ' 2017=' ,score2017)
            #print(university, ' 2018=' ,score2018)
    #print(score2016)

    #print(studentsperstaff)
    #plt.scatter(studentlist, studentsperstaff)
    #plt.show()
