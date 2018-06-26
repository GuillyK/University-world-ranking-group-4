from bokeh.plotting import figure, output_file, show

x16 = [10,50,100,200,300,400,500,600,700,800]
x17 = [10,50,100,200,300,400,500,600,700,800,900, 981]
x18 = [10,50,100,200,300,400,500,600,700,800,900,1000,1100,1103]

y16 = [91.5, 80.4, 71.7, 62.6,56.5,51.9,48.0,44.5,40.9,38.2]
y17 = [92.1, 81.3, 72.8, 64.0,58.3,53.8,50.1,46.8,43.4,40.9,38.0, 36.1]
y18 = [91.4, 81.2, 73.0, 64.5,59.2,55.0,51.5,48.4,45.2,42.8,40.1,38.0,35.7,35.7]

output_file("patch.html")

p = figure(plot_width=400, plot_height=400)

p.line(x16,y16, legend="2016", color="#01baef", line_width=2)
p.line(x17,y17, legend="2017", color="#f17105", line_width=2)
p.line(x18,y18, legend="2018", color="#9be564", line_width=2)


p.legend.click_policy="hide"

show(p)
