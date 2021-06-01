import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models import FactorRange
from bokeh.transform import factor_cmap

df = pd.read_csv('admission.csv')
year = df['Year'].apply(str).tolist()
male = df['Male'].tolist()
female = df['Female'].tolist()

line_graph = figure(title = "UofA Medical School Admission", x_range=year, y_range=(0,100), 
                 x_axis_label = "Year", y_axis_label = "Percentage of Admission", plot_height = 300, plot_width = 800)

line_graph.line(year, male, line_width = 3)
line_graph.line(year, female, line_width = 3)
show(line_graph)

data = dict(year=year, male=male, female=female)
#print(data)

source = ColumnDataSource(data=data)
categories = ('male','female')
colors = ["#718dbf", "#e84d60"]


stacked_visual = figure(title = "UofA Medical School Admission", x_range=year, y_range=(0,100), 
                 x_axis_label = "Year", y_axis_label = "Percentage of Admission", plot_height = 300, plot_width = 800)


stacked_visual.vbar_stack(categories, x='year', width=0.7, color=colors, source=source, legend_label=categories)

stacked_visual.xgrid.grid_line_color = None
stacked_visual.legend.orientation = "horizontal"
stacked_visual.legend.location = "top_left"

show(stacked_visual)

categories1 = ['m','f']
x = [(years, category) for years in year for category in categories1]
y = sum(zip(data['male'], data['female']), ())
data1 = dict(x=x, y=y)
# print(data1)

source1 = ColumnDataSource(data=data1)
grouped_visual = figure(title="Total Male vs. Female Enrollment at UofA Med by Year", x_range = FactorRange(*x), 
                y_range = (0,60),  x_axis_label = "Year", y_axis_label = "Percentage of Admission", plot_height = 300, plot_width = 800)
grouped_visual.vbar(x='x', top='y', width=0.7, source=source1, fill_color=factor_cmap('x', palette=colors, factors=categories1, start=1, end=2))
grouped_visual.xgrid.grid_line_color = None
show(grouped_visual)

