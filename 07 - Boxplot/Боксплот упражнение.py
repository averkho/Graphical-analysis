# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:12:36 2021

@author: AVERKHO
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
import seaborn as sns


dat=pd.read_excel('./Влажность.xlsx')

fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.boxplot(dat['Содержание влаги'])
ax.axhline(4,color='red')
ax.set_ylabel('%')
ax.set_title('Производство сухого молока')
ax.grid(True)

dat['месяц']=dat['Время'].dt.month

fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.boxplot(data=dat,y='Содержание влаги',x='месяц')
ax.axhline(4,color='red')
ax.set_ylabel('%')
ax.set_title('Производство сухого молока')
ax.grid(True)