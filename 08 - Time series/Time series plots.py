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


dat=pd.read_excel('./Production.xlsx')
dat_by_days=dat.groupby('date').agg({'Prod, t':'sum'})

def figure_captions():
    '''
    The function for making figure captions    
    Returns
    -------
    None.

    '''
    ax.set_ylabel('Tons')
    ax.set_xlabel('')
    ax.set_title('Production by days, tons')
    ax.grid(True)
    

# plotting with matplotlib
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.plot(dat_by_days)
figure_captions()

# Plotting with seaborn
dat_by_days.reset_index(inplace=True)
fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.lineplot(dat_by_days['date'],dat_by_days['Prod, t'])
figure_captions()

# Plotting with plotly
fig=go.Figure()
fig.add_traces(go.Scatter(x=dat_by_days['date'],y=dat_by_days['Prod, t']))
title={'text':'Production tons',
       'y':0.9,'x':0.5,
       'xanchor':'center','yanchor':'top'}
fig.update_layout(title=title,yaxis={'title':'tons'})
plot(fig)


# plotting by shifts
table = dat.pivot_table(dat,  index=['date'], columns=['shift'])
table.columns=['shift_1','shift_2','shift_3']

fig=plt.figure(3)
ax=fig.add_subplot(111)
ax.plot(table['shift_1'],label='Shift #1',color='blue')
ax.plot(table['shift_2'],label='shift #2',color='red')
ax.plot(table['shift_3'],label='shift #3',color='green')
figure_captions()
ax.legend()
ax.grid(True)