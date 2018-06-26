import csv
import pandas as pd
import numpy
from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
import matplotlib.pyplot as plt
plt.close
output_file("continentscores.html")

def meanscorer(university, dataset):
        score = data.loc[dataset['country'] == university, ['overall']]
        return(score['overall'].mean())

data = pd.read_csv("../DATA/ranking_with_country_2016.csv")
data1 = pd.read_csv("../DATA/ranking_with_country_2017.csv")
data2 = pd.read_csv("../DATA/ranking_with_country_2018.csv")
countries = pd.read_csv("../DATA/Countries-Continents.csv")

#for ratio in data['ratio']:
    #print(ratio)
averagecontinentscores = []
continents = []
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
    continents = continents + [continent]
    nummerofcountries = counter[continent]
    scoreofcontinent  = continentlist[continent]
    averagecontinentscore = scoreofcontinent / nummerofcountries
    averagecontinentscores = averagecontinentscores + [averagecontinentscore]
    print(continent, 'score' , averagecontinentscore)

data = ColumnDataSource(data=dict(continent3 = continents, score = averagecontinentscores, color=Spectral6))

p = figure(x_range = continents, y_range=(0,100), plot_height = 600, plot_width= 1000)
p.xaxis.axis_label = 'average score through the years'
p.yaxis.axis_label = "continents"
p.vbar(source=data, x ='continent3' , top='score', color ='color', width =1)
show(p)
    #print(studentsperstaff)
    #plt.scatter(studentlist, studentsperstaff)
    #plt.show()
