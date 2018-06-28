######################################################################################
# Makes the vbar graph for the average score of english universities versus non-english

######################################################################################

from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge

output_file("overall_English.html")

fruits = ['2016', '2017', '2018']
years = ['English', 'Non-English']

data = {'fruits' : fruits,
        'English'   : [46.16, 46.69, 47.39],
        'Non-English'   : [33.43, 31.06, 30.67]}

source = ColumnDataSource(data=data)

p = figure(x_range=fruits, y_range=(0, 70), plot_height=250, title="Overall score countries",
           toolbar_location=None, tools="")


p.vbar(x=dodge('fruits',  -0.13,  range=p.x_range), top='English', width=0.2, source=source,
       color="#e84d60", legend=value("English"))

p.vbar(x=dodge('fruits',  0.13, range=p.x_range), top='Non-English', width=0.2, source=source,
       color="#718dbf", legend=value("Non-English"))

p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

show(p)
