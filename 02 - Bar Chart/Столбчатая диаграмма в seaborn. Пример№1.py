# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:40:24 2020

@author: AVERKHO
"""


#Импорт необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.close('all')

#Импорт данных
dat=pd.read_excel('./Дефекты пиломатериалов.xlsx','Данные')

'''
Задача №1. Оценить уровень дефектов в компании. 
Выделить приоритетные направления для работы команды Шесть Сигм.
'''

# Подготовка данных
defects=dat['дефекты'].value_counts()

#Функция по добавлению названий на столбики
def autolabel(rects):
    for p in rects.patches:
        x=p.get_x()+p.get_width()/2 # координата x
        y=p.get_y()+p.get_height()*1.05 # координата y
        value='{}'.format(int(p.get_height())) # подпись - данные
        ax.text(x,y,value,ha='center') # добавление подписи на график



fig=plt.figure(1)
ax=fig.add_subplot(111)
rects=sns.barplot(x=defects.index,y=defects) # bar plot
rects.set_title('Дефекты пиломатериалов',fontsize=13,style='italic') # title of the figure
rects.set_ylabel('Количество') # title of y axes
ax.grid(True) # gridlines
autolabel(rects)

'''
Задача №2. Сравнить первый и второй кварталы и сделать соответствующие выводы

'''

dat_tab=dat.groupby(['дефекты','квартал']).agg({'дефекты':'count'})
dat_tab.columns=['Количество']
dat_tab=pd.DataFrame(dat_tab)
dat_tab=dat_tab.reset_index()

fig=plt.figure(2)
ax=fig.add_subplot(111)
rects=sns.barplot(x='дефекты',y='Количество',data=dat_tab,
                  hue='квартал',order=defects.index
                  )
ax.set_title('Дефекты пиломатериалов по кварталам')
autolabel(rects)
ax.grid()
fig.tight_layout()
