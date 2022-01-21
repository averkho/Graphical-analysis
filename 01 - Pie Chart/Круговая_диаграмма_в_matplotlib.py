# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# загрузка необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#importing the data
dat=pd.read_excel('./Статусы проектов Данные.xlsx')

# Prepare data for pie chart constructing
dat_Jan=dat['Январь'].value_counts()
dat_Nov=dat['Ноябрь'].value_counts()


fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.pie(dat_Jan,labels=dat_Jan.index,autopct='%1.1f%%')
plt.title('Проекты в январе',fontsize=14)

#Применение разрывов для расставления акцентов
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
plt.title('Проекты в январе')

# Построение двух диаграмм на одном графике
fig=plt.figure(3)
ax=fig.add_subplot(121)

ax=fig.add_subplot(121)

ax.pie(dat_Jan,labels=dat_Jan.index,autopct='%1.1f%%',counterclock=False,startangle=90)
plt.title('Проекты в январе')

ax2=fig.add_subplot(122)
ax2.pie(dat_Nov,labels=dat_Nov.index,autopct='%1.1f%%',counterclock=False,startangle=90)

plt.tight_layout(True)
plt.title('Проекты в ноябре')


