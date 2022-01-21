# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:49:11 2020

"""


# importing the libraries
import pandas as pd
import numpy as np
import plotly.graph_objs as go

from plotly.offline import plot

from plotly.subplots import make_subplots

#importing the data
dat=pd.read_excel('./Lumber defects.xlsx')

# Prepare data for pie chart constructing
defects=dat['Defects'].value_counts()


# constructing bar chart
fig1=go.Figure(data=[go.Bar(x=defects.index,y=defects,text=defects,textposition='outside',
                            textfont_color='black')])
fig1.update_layout(title={'text':'Lumber defects',
                          'y':0.9,
                          'x':0.5,
                          'xanchor':'center',
                          'yanchor':'top'})
fig1.update_layout(yaxis_title='Count of defects')


plot(fig1)


#Дефекты по кварталам
dat_Q1=dat[dat['Quarter']=='Q1']['Defects'].value_counts()
dat_Q2=dat[dat['Quarter']=='Q2']['Defects'].value_counts()

dat_Q1_Q2=pd.concat([dat_Q1,dat_Q2],axis=1) # объединение двух объектов Series в DataFrame
dat_Q1_Q2.columns=['Q1','Q2']  # Имена колонок



fig2=go.Figure(data=[go.Bar(name='Quarter 1',x=dat_Q1_Q2.index,y=dat_Q1_Q2['Q1'],
                            text=dat_Q1_Q2['Q1'],textposition='outside'),
                     go.Bar(name='Quarter 2',x=dat_Q1_Q2.index,y=dat_Q1_Q2['Q2'],
                            text=dat_Q1_Q2['Q2'],textposition='outside')])

fig2.update_layout(title={'text':'Lumber defects by Quarters',
                          'y':0.9,
                          'x':0.5,
                          'xanchor':'center',
                          'yanchor':'top'})
fig2.update_layout(yaxis_title='Count of defects')

plot(fig2)