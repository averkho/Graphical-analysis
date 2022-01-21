# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:29:23 2021

@author: AVERKHO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
import seaborn as sns

import plotly.graph_objs as go
from plotly.offline import plot


dat=pd.read_excel('./Производство.xlsx')
dat_by_days=dat.groupby('Дата').agg({'Произведено, т':'sum'})

def figure_captions():
    '''
    The function for making figure captions    
    Returns
    -------
    None.

    '''
    ax.set_ylabel('Тонны')
    ax.set_xlabel('')
    ax.set_title('Производстов по дням, тонны')
    ax.grid(True)
    

# Использование библиотеки matplotlib
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.plot(dat_by_days)
figure_captions()

# Использование библиотеки seaborn
dat_by_days.reset_index(inplace=True)
fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.lineplot(dat_by_days['Дата'],dat_by_days['Произведено, т'])
figure_captions()

# Использование библиотеки plotly
fig=go.Figure()
fig.add_traces(go.Scatter(x=dat_by_days['Дата'],y=dat_by_days['Произведено, т']))
title={'text':'Производство, тонны',
       'y':0.9,'x':0.5,
       'xanchor':'center','yanchor':'top'}
fig.update_layout(title=title,yaxis={'title':'тонны'})
plot(fig)


# Анализ по сменам
table = dat.pivot_table(dat,  index=['Дата'], columns=['Смена'])
table.columns=['Смена_1','Смена_2','Смена_3']

fig=plt.figure(3)
ax=fig.add_subplot(111)
ax.plot(table['Смена_1'],label='Смена №1',color='blue')
ax.plot(table['Смена_2'],label='Смена №2',color='red')
ax.plot(table['Смена_3'],label='Смена №3',color='green')
figure_captions()
ax.legend()
ax.grid(True)