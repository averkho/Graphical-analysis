# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#importing the data
dat=pd.read_excel('./Project statuses Data.xlsx')

# Prepare data for pie chart constructing
dat_Jan=dat['Status January'].value_counts()
dat_Nov=dat['Status November'].value_counts()


fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.pie(dat_Jan,labels=dat_Jan.index,autopct='%1.1f%%')
plt.title('Project in January',fontsize=14)

#using explode to highlight information
explode=[]
for ind in dat_Jan.index:
    if ind==dat_Jan.idxmax():
        explode.append(0.2)
    else:
        explode.append(0)
explode=tuple(explode)       

fig=plt.figure(2)
ax=fig.add_subplot(111)
ax.pie(dat_Jan,labels=dat_Jan.index,explode=explode,autopct='%1.1f%%')
plt.title('Project in January')

# Making two pie charts on the same graph
fig=plt.figure(3)
ax=fig.add_subplot(121)

ax=fig.add_subplot(121)

ax.pie(dat_Jan,labels=dat_Jan.index,autopct='%1.1f%%',counterclock=False,startangle=90)
plt.title('Project in January')

ax2=fig.add_subplot(122)
ax2.pie(dat_Nov,labels=dat_Nov.index,autopct='%1.1f%%',counterclock=False,startangle=90)

plt.tight_layout(True)
plt.title('Project in November')


