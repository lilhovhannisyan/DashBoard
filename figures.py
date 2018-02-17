from plotly.offline import plot
import plotly.graph_objs as go

#Figure1
trace1 = go.Bar(x=[12,52,15,20],
                y=['X8','X7','X6','X5'],
                name="<b>Negative</b>",
                orientation='h',
                marker=dict(
                line=dict(
                color='#42f4c4',
                width=2)),
                opacity = 0.5
                 )

trace2 = go.Bar(x=[-15,-52,-5,-35],
                y=['X4','X3','X2','X1'],
                name="Positive",
                orientation='h',
                marker=dict(
                line=dict(
                color='#42a4f4',
                width=2)),
                opacity = 0.5
               )
                   
data = [trace1,trace2]
layout=go.Layout(
title="<b>Correlations with employees probability of churn</b>",
yaxis=dict(
title='Variable'))
figure1 = dict(data=data,layout=layout)

#Figure2

import quandl
quandl.ApiConfig.api_key = '1mc69StJzxmo-ssYH3su' 
data = quandl.get('FRED/GDP')
data_GDP = data[:]

import pandas as pd
x_values = pd.to_datetime(data_GDP.index.values)
y_values = data_GDP.Value
trace = go.Scatter(x=x_values,y=y_values,mode="lines",fill='tonexty')

layout= dict(title = '<b>US GDP over time </b>')

data = [trace]
figure2 = dict(data=data, layout=layout)

#Figure3

data= quandl.get('WIKI/GOOGL')
data_WG = data[:]

data= quandl.get('BCHARTS/ABUCOINSUSD')
data_BA = data[:]


trace1 = go.Box(x=data_BA.Open.pct_change(),name="<b>Bitcoin</b>")
trace2 = go.Box(x=data_WG.Open.pct_change(),name="<b>Google</b>")
layout=dict(title='Distribution of Price Changes')
data = [trace1,trace2]
figure3 = dict(data=data,layout=layout)

#Figure4

BPer=data_BA.Open.pct_change()
GPer=data_WG.Open.pct_change()
header = dict(values=['Google','Bitcoin'],
              align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
             )
cells = dict(values=[GPer[1:5].round(3),BPer[1:5].round(3)],
             align=  ['left','center'],
             fill = dict(color=["yellow","white"])
            )
            
trace =go.Table(header=header, cells=cells)

data = [trace]
layout = dict(width=500, height=300)
figure4 = dict(data=data, layout=layout)

#Figure5
import plotly.figure_factory as ff
df = [dict(Task="Task1", Start='2018-01-01', Finish='2018-01-31',Resource='Idea Validation'),
      dict(Task="Task2", Start='2018-03-01', Finish='2018-04-15',Resource='Prototyping'),
      dict(Task="Task3", Start='2018-04-15', Finish='2018-09-30',Resource='Team Formation')]

figure5 = ff.create_gantt(df, index_col='Resource', show_colorbar=True,title='Startup Roadmap')




