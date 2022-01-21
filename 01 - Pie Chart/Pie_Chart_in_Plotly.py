# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# importing the libraries
import pandas as pd
import numpy as np
import plotly.graph_objs as go

from plotly.offline import plot

from plotly.subplots import make_subplots

#importing the data
dat=pd.read_excel('./Project statuses Data.xlsx')

# Prepare data for pie chart constructing
dat_Jan=dat['Status January'].value_counts()
dat_Nov=dat['Status November'].value_counts()

# constructing pie chart
fig1=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan)])
plot(fig1)

#customizing pie chart
fig2=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan)])
fig2.update_traces(hoverinfo='label+percent',textinfo='percent',textfont_size=20,
                  marker=dict(line=dict(color='black', width=2)),
                  textposition='inside')
plot(fig2)

#Implementing explode (pull) to highkight the maximum
explode=[]
for ind in dat_Jan.index:
    if ind==dat_Jan.idxmax():
        explode.append(0.2)
    else:
        explode.append(0)
     



# Pie chart with highlighted maximum

fig3=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan,name='Projects in January')])
fig3.update_traces(hoverinfo='label+percent',textinfo='percent',textfont_size=20,
                  marker=dict(line=dict(color='black', width=2)),
                  textposition='inside',pull=explode)

plot(fig3)

# Making to plots on one page
fig4=make_subplots(rows=1,cols=2,specs=([[{'type':'domain'},{'type':'domain'}]]))
fig4.add_trace(go.Pie(labels=dat_Jan.index,values=dat_Jan,name='Projects in January'),1,1)
fig4.add_trace(go.Pie(labels=dat_Nov.index,values=dat_Nov,name='Projects in November'),1,2)
fig4.update_traces(textinfo='label+percent',hoverinfo='value')
fig4.update_layout(title={
        'text': "Projects development",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        })

plot(fig4)

