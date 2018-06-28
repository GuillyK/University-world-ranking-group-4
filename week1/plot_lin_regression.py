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


output_file("meancontinentXdeviation.html")

data = pd.read_csv("../DATA/ranking_with_country_2018.csv")
nan = 1.8
meancountrylist = [40.9807256236, 34.0599759615,27.8954545455,39.8806451613,21.080952381,20.1264705882]


deviationlist = [0.819863143977,1.67953861854, 1.10340382454, 0.895142050732,3.40513262495, 0.741418580991]




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
