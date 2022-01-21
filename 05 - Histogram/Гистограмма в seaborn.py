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


dat=pd.read_excel('./Гравитационные ролики.xlsx','Каток_1')

dat=dat[dat['Длина']<100]


fig=plt.figure(1)
ax=fig.add_subplot(111)
sns.histplot(x=dat['Длина'],kde=True)
ax.set(xlabel='мм',ylabel='частота',title='Гравитационные катки')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
ax.grid(True)


fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.histplot(x=dat['Длина'],bins=20,stat='density')
ax.set(xlabel='мм',ylabel='частота',title='Гравитационные катки')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
mean=dat['Длина'].mean()
std=dat['Длина'].std()
x=np.linspace(mean-3*std,mean+3*std,1000)
sns.lineplot(x,stats.norm.pdf(x,mean,std),color='red',lw=2)
ax.grid(True)

dat2=pd.read_excel('./Гравитационные ролики.xlsx','Каток_2')

dat['каток']='A'
dat2['каток']='B'

dat=pd.concat([dat,dat2])

fig=plt.figure(3)
ax=fig.add_subplot(111)
sns.histplot(data=dat,x='Длина',hue='каток',bins=40,stat='count')
ax.set(xlabel='мм',ylabel='частота',title='Гравитационные катки')
ax.grid(True)



