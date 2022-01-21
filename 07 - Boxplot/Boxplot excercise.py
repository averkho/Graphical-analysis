# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 14:12:36 2021

@author: AVERKHO
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')
import seaborn as sns


dat=pd.read_excel('./Moisture_data.xlsx')

fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.boxplot(dat['Moisture_content'])
ax.axhline(4,color='red')
ax.set_ylabel('%')
ax.set_title('Milk poweder production line')
ax.grid(True)

dat['month']=dat['Timestamp'].dt.month

fig=plt.figure(2)
ax=fig.add_subplot(111)
sns.boxplot(data=dat,y='Moisture_content',x='month')
ax.axhline(4,color='red')
ax.set_ylabel('%')
ax.set_title('Milk powder production line')
ax.grid(True)