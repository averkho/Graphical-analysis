# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:18:35 2020

@author: AVERKHO
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import seaborn as sns

dat=pd.read_excel('./pH measurement.xlsx')

dat['day_of_week']=dat['date'].dt.dayofweek

print(dat.describe())
print(dat.shape)
dat=dat.loc[(dat['pH']>0) & (dat['pH']<14)]
print(dat.shape)

def annotate(rects):
    for p in rects.patches:
        x=p.get_x()+p.get_width()/2 # x coordinate of the label
        y=p.get_y()+p.get_height()*1.05 # y coordinatw of the label
        value='{}'.format(np.round(p.get_height(),2)) # value of the label
        ax.text(x,y,value,ha='center') # adding labels the the figure

fig=plt.figure(1)
ax=fig.add_subplot(111)
rects=sns.barplot(x=dat['day_of_week'],y=dat['pH'],estimator=np.mean,ci=None)
ax.grid(True)
plt.title('pH by days of week')


annotate(rects)    
fig.tight_layout()

dat=pd.read_excel('./pH measurement_after.xlsx')

dat['day_of_week']=dat['date'].dt.dayofweek

print(dat.describe())

fig=plt.figure(2)
ax=fig.add_subplot(111)
rects=sns.barplot(x=dat['day_of_week'],y=dat['pH'],estimator=np.mean,ci=None)
ax.grid(True)
ax.set_ylim([0,11])
plt.title('pH by days of week')
annotate(rects)

fig.tight_layout()