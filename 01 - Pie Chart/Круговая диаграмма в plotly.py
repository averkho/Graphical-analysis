# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# импорт необходиммых библиотек
import pandas as pd
import numpy as np
import plotly.graph_objs as go

from plotly.offline import plot
from plotly.subplots import make_subplots

#импорт данных
dat=pd.read_excel('./Дефекты пиломатериалов.xlsx')

# Подготоска данных
defects=dat['Defects'].value_counts()


# Построение круговой диаграммы
fig1=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan)])
plot(fig1)

#Форматирование круговой диаграммы
fig2=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan)])
fig2.update_traces(hoverinfo='label+percent',textinfo='percent',textfont_size=20,
                  marker=dict(line=dict(color='black', width=2)),
                  textposition='inside')
plot(fig2)

#Выделение необходимой информации
explode=[]
for ind in dat_Jan.index:
    if ind==dat_Jan.idxmax():
        explode.append(0.2)
    else:
        explode.append(0)
     



# Построение круговой диаграммы с выделенным максимумом

fig3=go.Figure(data=[go.Pie(labels=dat_Jan.index,values=dat_Jan)])
fig3.update_traces(hoverinfo='label+percent',textinfo='percent',textfont_size=20,
                  marker=dict(line=dict(color='black', width=2)),
                  textposition='inside',pull=explode)

plot(fig3)

# Построение двух диаграмм на одной странице
fig4=make_subplots(rows=1,cols=2,specs=([[{'type':'domain'},{'type':'domain'}]]))
fig4.add_trace(go.Pie(labels=dat_Jan.index,values=dat_Jan),1,1)
fig4.add_trace(go.Pie(labels=dat_Nov.index,values=dat_Nov),1,2)
fig4.update_traces(textinfo='label+percent',hoverinfo='value')
fig4.update_layout(title={
        'text': "Развитие проектов",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        })

plot(fig4)

