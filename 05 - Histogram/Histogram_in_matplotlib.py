# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:11:54 2021

@author: AVERKHO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import scipy.stats as stats
import math

dat=pd.read_excel('./Gravity rollers.xlsx','Rollers_1')

fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.hist(dat['Shaft length'],50)

dat.describe()

dat_outliers=dat[dat['Shaft length']>100]

dat=dat[dat['Shaft length']<100]

fig=plt.figure(2)
ax=fig.add_subplot(111)
ax.hist(dat['Shaft length'],bins=30,edgecolor='black')
ax.set(xlabel='mm',ylabel='frequency',title='Gravity rollers')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
ax.grid(True)

fig=plt.figure(3)
ax=fig.add_subplot(111)
ax.hist(dat['Shaft length'],bins=25,edgecolor='black',density=True,facecolor='blue')
ax.set(xlabel='mm',ylabel='frequency',title='Gravity rollers')
plt.axvline(91,color='red',linestyle='--')
plt.axvline(89,color='red',linestyle='--')
ax.grid(True)
mean=dat['Shaft length'].mean()
std=dat['Shaft length'].std()
x=np.linspace(mean-3*std,mean+3*std,1000)
ax.plot(x,stats.norm.pdf(x,mean,std),linewidth=4)

dat2=pd.read_excel('./Gravity rollers.xlsx','Rollers_2')

fig=plt.figure(4)
ax=fig.add_subplot(111)
ax.hist(dat['Shaft length'],bins=20,edgecolor='black',facecolor='blue',density=True)
ax.hist(dat2['Shaft length'],bins=20,edgecolor='black',facecolor='green',density=True)
ax.set(xlabel='mm',ylabel='frequency',title='Gravity rollers')
ax.grid(True)
mean_1=dat['Shaft length'].mean()
std_1=dat['Shaft length'].std()
mean_2=dat2['Shaft length'].mean()
std_2=dat2['Shaft length'].std()
ax.text(mean_1*1.01, .9, r'$\mu={},\ \sigma={}$'.format(np.round(mean_1,1),np.round(std_1,2)))
ax.text(mean_2*1.01, .6, r'$\mu={},\ \sigma={}$'.format(np.round(mean_2,1),np.round(std_2,2)))


