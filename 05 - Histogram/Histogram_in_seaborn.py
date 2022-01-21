# -*- coding: utf-8 -*-+-*
"""
Created on Tue Jan 12 20:10:11 2021

@author: AVERKHO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import seaborn as sns
import scipy.stats as stats


dat=pd.read_excel('./Gravity rollers.xlsx','Rollers_1')

dat=dat[dat['Shaft length']<100]


fig=plt.figure(1)
ax=fig.add_subplot(111)
sns.histplot(x=dat['Shaft length'],kde=True)
ax.set(xlabel='mm',ylabel='frequency',title='Gravity rollers')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
ax.grid(True)


fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.histplot(x=dat['Shaft length'],bins=20,stat='density')
ax.set(xlabel='mm',ylabel='frequency',title='Gravity rollers')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
mean=dat['Shaft length'].mean()
std=dat['Shaft length'].std()
x=np.linspace(mean-3*std,mean+3*std,1000)
sns.lineplot(x,stats.norm.pdf(x,mean,std),color='red',lw=2)
ax.grid(True)

dat2=pd.read_excel('./Gravity rollers.xlsx','Rollers_2')

dat['roller']='A'
dat2['roller']='B'

dat=pd.concat([dat,dat2])

fig=plt.figure(3)
ax=fig.add_subplot(111)
sns.histplot(data=dat,x='Shaft length',hue='roller',bins=40,stat='count')
ax.set(xlabel='mm',ylabel='counts',title='Gravity rollers')
ax.grid(True)



