# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:30:44 2020

@author: AVERKHO
"""

# Импорт необходимых библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
def autolabels(rects):
    """Добавление текста на каждый столбец. Текст - высота столбца"""
    for rect in rects:
        height=rect.get_height() # Значения - высота столбцов
        ax.annotate('{}'.format(height), # Добавление значений на столбцы
                    xy=(rect.get_x()+rect.get_width()/2,height), # координаты подписей
                    xytext=(0,4), # Вертикальное  смещение на 4 единицы
                    textcoords="offset points",  # координатная система xytext
                    ha='center',va='bottom') # горизонтальное и вертикальное расположение текста
    
# Построение фигуры №1
fig=plt.figure(1)
ax=fig.add_subplot(111)
rects=ax.bar(defects.index,defects,color='blue') # Построение столбчатой диаграммы
ax.set_ylabel('Количество дефектов') # Название оси Y
autolabels(rects) # Добавление подписей на столбцы
ax.grid(True) # Добавление линий сетки
plt.title('Дефекты пиломатериалов') # Название графика

'''
Задача №2. Сравнить первый и второй кварталы и сделать соответствующие выводы

'''

#Дефекты по кварталам
dat_Q1=dat[dat['квартал']=='первый']['дефекты'].value_counts()
dat_Q2=dat[dat['квартал']=='второй']['дефекты'].value_counts()

dat_Q1_Q2=pd.concat([dat_Q1,dat_Q2],axis=1) # объединение двух объектов Series в DataFrame
dat_Q1_Q2.columns=['первый','второй']  # Имена колонок
width=0.35  # Ширина столбцов

x=np.arange(len(dat_Q1)) # метки для столбцов

#Построение группированного графика

fig=plt.figure(2)
ax=fig.add_subplot(111)
rects1=ax.bar(x-width/2,dat_Q1_Q2['первый'],width,label='Первый квартал') # Первая столбчатая диаграмма
rects2=ax.bar(x+width/2,dat_Q1_Q2['второй'],width,label='Второй квартал') # Вторая столбчатая диаграмма
ax.set_ylabel('Количество') # Подпись оси Y
ax.set_title('Дефекты в первом и втором кварталах') # Название графика
ax.set_xticks(x) # Добавление меток на ось X
ax.set_xticklabels(dat_Q1_Q2.index)  # Доавление пописей меток

autolabels(rects1)  # Добавление подписей на первый график
autolabels(rects2) # Добавление подписей на второй график
plt.grid(True) # Добавление линий сеток
ax.legend() # Добавление легенды на график
fig.tight_layout()
