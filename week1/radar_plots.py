# makes the radar plots for top 200 anomaly. It works in jupyter notebook.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show


plt.close

data = pd.read_csv("../DATA/ranking_with_country_2016.csv")


df=pd.read_csv("../DATA/ranking_with_country_2016.csv")
df1=pd.read_csv("../DATA/ranking_with_country_2017.csv")
df2=pd.read_csv("../DATA/ranking_with_country_2018.csv")

output_file('radar.html')
def rank(university, dataset):
        score = data.loc[dataset['name'] == university, ['rank']]
        try:
            if type(score['rank'].mean()) == np.float64:
                return(score['rank'].mean())
            else:
                return(score.values)
        except ValueError:
            return(score.values)
        except TypeError:
            return(score.values)

        
countrylist = []

for name in df2['name'][:10]:
    if name not in countrylist:
        countrylist = countrylist + [name]
        rank2016 = rank(name, df)
        rank2017 = rank(name, df1)
        rank2018 = rank(name, df2)

        labels=np.array(['overall', 'industry_income', 'international_outlook', 'citations', 'teaching', 'research'])
        
        angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        angles=np.concatenate((angles,[angles[0]]))

        fig=plt.figure()
        ax = fig.add_subplot(111, polar=True)
        try:
            stats=df.loc[df['name'] == name,labels].values[0]
            stats=np.concatenate((stats,[stats[0]]))
            ax.plot(angles, stats, 'o-', linewidth=2, color = '#01baef', label = '2016, rank = {}'.format((df.loc[df['name'] == name,['rank']].values[0])[0]))
            ax.fill(angles, stats, alpha=0.1)
        except IndexError:
            pass
            
        try:
            stats1=df1.loc[df1['name'] == name,labels].values[0]
            stats1=np.concatenate((stats1,[stats1[0]]))
            ax.plot(angles, stats1, 'o-', linewidth=2, color = '#f17105', label = '2017, rank = {}'.format((df1.loc[df1['name'] == name,['rank']].values[0])[0]))
            ax.fill(angles, stats1, alpha=0.1)
        except IndexError:
            pass
        
        try:
            stats2=df2.loc[df2['name'] == name,labels].values[0]
            stats2=np.concatenate((stats2,[stats2[0]]))
            ax.plot(angles, stats2, 'o-', linewidth=2, color = '#9be564', label = '2018, rank = {}'.format((df2.loc[df2['name'] == name,['rank']].values[0])[0]))
            ax.fill(angles, stats2, alpha=0.1)
        except IndexError:
            pass





        # close the plot
        plt.legend(loc='upper right', bbox_to_anchor=(1.5, 0.1))

        plt.yticks([20,40,60,80,100], ["20","40","60","80","100"])
        ax.set_thetagrids(angles * 180/np.pi, labels)
        ax.set_title(name, fontweight = 'bold')
        ax.grid(True)
        

