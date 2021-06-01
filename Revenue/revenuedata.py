import pandas as pd 
from bokeh.plotting import figure, show, output_notebook
#from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource

#output_notebook()

df = pd.read_csv("facebookR.csv")
df.index += 1

years = (df['Year']).apply(str)
revenue = df['Revenue']
source = ColumnDataSource(data=dict(years=years, revenue=revenue))
visual = figure(title="Annual Revenue of Facebook in the Past 12 Years", x_range=years, y_range=(0,100),
                x_axis_label = "Year", y_axis_label = "Revenue (in billion dollars)", plot_height = 300, plot_width = 800)
visual.vbar(x='years', top='revenue', width=0.7, source=source)
visual.xgrid.grid_line_color = None
show(visual)

# stats from https://www.statista.com/statistics/268604/annual-revenue-of-facebook/ 

df1 = pd.read_csv("AppleR.csv")
df1.index += 1

fiscalyears = (df1['Fiscalyears']).apply(str)
income = df1['Netincome']
source1 = ColumnDataSource(data=dict(fiscalyears=fiscalyears, income=income))
visual1 = figure(title="Annual Revenue of Apple in the Past 10 Years", x_range=fiscalyears, y_range=(0,100),
                x_axis_label = "Fiscal Years", y_axis_label = "Net income (in billion dollars)", plot_height = 300, plot_width = 600)
visual1.vbar(x='fiscalyears', top='income', width=0.6, source=source1)
visual1.xgrid.grid_line_color = None
show(visual1)

# stats from https://www.statista.com/statistics/267728/apples-net-income-since-2005/ 

