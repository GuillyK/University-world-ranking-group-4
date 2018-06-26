######################################################################################
#maker of scatter plot of 2 dataset with a trendline and a calculated mean mean_squared_error

######################################################################################

import googlemaps
import numpy as np

import pandas as pd
from pandas import Series,DataFrame
from bokeh.layouts import gridplot, row, column

from bokeh.io import push_notebook, show, output_file, output_notebook
from bokeh.plotting import figure
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression


#output_file("meancountryXdeviation.html")

data = pd.read_csv("../DATA/ranking_with_country_2018.csv")
nan = 1.8
meancountrylist = [48.514549899107287, 41.979873824677192, 55.600000000000001, 43.4785641025641, 74.750000000000014, 50.784848484848489, 49.698804458560552, 42.794715821812595, 49.253571428571433, 29.03099271520324, 27.036528558570524, 56.744444444444447, 59.507692307692309, 38.49250744997871, 39.607407407407408, 48.12619047619048, 32.994411506368031, 38.459259259259262, 35.377575187969917, 31.831746031746032, 42.858333333333327, 39.466071428571432, 27.660345679012348, 31.6482905982906, 25.448322981366463, 36.579761904761902, 35.116666666666667, 50.0, 21.91418300653595, 43.883333333333333, 24.468421052631573, 31.988888888888891, 26.994579124579122, 23.923703703703705, 26.293650793650794, 35.649999999999999, 27.015740740740739, 30.783333333333331, 32.899999999999999, 23.224206349206352, 22.887500000000003, 36.133333333333333, 25.766666666666666, 20.383809523809521, 28.533333333333331, 23.055555555555554, 21.041666666666664, 20.752380952380953, 23.633333333333336, 23.194444444444443, 22.25277777777778, 24.300000000000001, 21.202380952380953, 16.205555555555559, 14.800000000000001, 17.699999999999999, 20.216666666666665, 15.1, 19.850000000000001, 14.199999999999999, 15.800000000000001, 24.050000000000001, 19.199999999999999, 14.699999999999999, 16.800000000000001, 14.1, 27.133333333333336, 20.699999999999999, 14.85, 20.766666666666666]


deviationlist = [0.81986314397716553, 1.6795386185354129, 0.52716221412388586, 1.555370473445054, 1.103403824535697, 0.73632622426471983, 1.1602441854945631, 0.89514205073160857, 0.91230078899003675, 0.67697188277651188, 1.2065369243911372, 2.5261044522552356, 0.53994301693647606, 2.0908708030835088, 0.61967069443965606, 1.783603514405214, 1.2665731954875774, 0.52778752427647491, 1.8715260469475994, 3.4051326249501117, 1.5804139753030946, 1.1799923793423914, 1.8818384399404455, 0.14368319608489039, 0.63285735926391518, 0.36373090337229375, 2.2578258962501443, 0.51961524227066236, 0.74141858099111635, 4.5333026959749052, 1.5761319219670806, 1.0304507284211628, 1.6630437217034439, 1.8034073830669604, 2.5157838850567864, 1.9150718002205562, 5.1161692463406316, 0.72341781380702153, 1.7521415467935251, 0.90539164592008881, 1.9514818087801882, 2.0207259421636903, 3.8552993831002715, 0.89531357331262651, 0.90737717258774608, 2.3528548459107985, 2.1601986791342447, 0.73752666272569067, 1.5135499110810102, 2.4014077661362019, 0.74331900833232112, 3.3893624441445906, 1.0859981615098264, 0.24171455464229974, nan, nan, 0.25658007197234439, nan, 0.21213203435596475, nan, nan, 9.2329572727268712, nan, nan, nan, nan, 5.2319531088622471, 0.0, nan, 1.2701705922171762]


newmeancountrylist = []
newdeviationlist = []


for item in meancountrylist:
    newitem = float(item)
    newmeancountrylist = newmeancountrylist + [newitem]
print(newmeancountrylist)

for item1 in deviationlist:
#    if not item1:
#        item1 = 2
    newitem1 = float(item1)
    newdeviationlist = newdeviationlist + [item1]

print(newdeviationlist)

# Set up X as median room values and use Use vstack to make X two-dimensional
# Remember that X normally is (N,) instead of (N,1).
X = np.vstack(newmeancountrylist)

# Set up Y as the target price of the houses.
Y = newdeviationlist

# Creating [X 1] (remember the useful np.ones function from the first notebook?)
X = np.vstack(newmeancountrylist)
X = np.column_stack((X, np.ones(X.shape[0])))

# Now get out m and b values for our best fit line
a, b = np.linalg.lstsq(X, Y)[0]
print(a, b)

f = figure(plot_width=1000, plot_height=500)

# Create a scatter-plot
f.scatter(newmeancountrylist, newdeviationlist)

# Create the line
x = pd.Series(newmeancountrylist)
#x = list(newlist)
f.line(x, a * x + b, color='red')

## Add some axis information
f.xaxis.axis_label = 'average score per country through the years'
f.yaxis.axis_label = "deviation in average through the years"

show(f)

from sklearn.metrics import mean_squared_error
r = np.array(newdeviationlist)
x = np.array(newmeancountrylist)
y = a * x + b
print(len(x))
smse = sum((r-y) **2) / len(x)
print(smse)
rmse = np.sqrt(smse)
print(rmse)


mse = mean_squared_error(r, y)
print(mse)
