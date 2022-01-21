# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:48:30 2021

@author: AVERKHO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

dat=pd.read_excel('./Котлы.xlsx')

#Creating separate Series for each boiler
boiler_1=dat['Котел_1']
boiler_2=dat['Котел_2']
boiler_3=dat['Котел_3']

def check_non_numeric(df)->str:
    
    ''' checking if the DataFrame contains string values/
        проверка данных на наличие строковых значений
    '''
    
    ss=list(df[df.apply(lambda x: isinstance(x,str))].unique())
    return ss


# The lists of non numeric (string) data in each Series
# Списки нечисловых (строковых) данных в кажодом объекте Серия
ss_1=check_non_numeric(boiler_1)
ss_2=check_non_numeric(boiler_2)
ss_3=check_non_numeric(boiler_3)

# How many non numeric data do we have?
#  Сколько нечисловых значений мы имеем?
percent_of_strings=len(boiler_1[boiler_1==ss_1[0]])/len(boiler_1)*100
print(np.round(percent_of_strings,2),'%')

# Removing string data from boiler #1
# Избавимся от тектовых значений в таблице данных котла №1
boiler_1=boiler_1[boiler_1!=ss_1[0]]

# Checking if there are any string data in a Series left
# Проверим, осталось ли что-нибудь еще удалять 
ss_=check_non_numeric(boiler_1)

def histogram_plotting(df,fig_num,title,n_bins=35):
    
    ''' 
    plotting histograms for boilers. Построение гистограмм для котлов
    The finction recieves data in form of Series (df). Функция получает данные в формате Серия (df)
    fig_num - the figure number to be plotted. Порядковый номер графика для построения
    title - the title of the histogram. Заголовок диаграммы
    n_bins - number of bins in the histogram. Количество бинов
    
    '''
    
    fig=plt.figure(fig_num)
    ax=fig.add_subplot(111)
    ax.hist(df,bins=n_bins,edgecolor='black',facecolor='blue')
    ax.set_title(title)
    ax.set_xlabel('т/час')
    ax.set_ylabel('часы')
    ax.grid(True)

# Boiler #1
histogram_plotting(boiler_1,fig_num=1,title='Котел №1')

#removing the first peak
boiler_1=boiler_1[boiler_1>10]

histogram_plotting(boiler_1,fig_num=2,title='Котел №1')

# Boiler #2
histogram_plotting(boiler_2,fig_num=3,title='Котел №2')

boiler_2=boiler_2[boiler_2>10]

histogram_plotting(boiler_2,fig_num=4,title='Котел №2')

#Boiler #3
histogram_plotting(boiler_3,fig_num=5,title='Котел №3')

boiler_3=boiler_3[boiler_3>10]

histogram_plotting(boiler_3,fig_num=6,title='Котел №3')

# Total productivity calculation and plotting/Расчет и отображение суммарной производительности котлов
# Removing string values from the DataFrame / Удаление строковых значений из всей таблицы
dat=dat[dat['Котел_1']!=ss_1[0]]

# Reseting index - to simplify math operations with the DataFrame in the future
# Переустановка индекса - упрощение математических операций с массивом в будущем
dat=dat.set_index('Дата_время')

# Calculating total productivity of Boielrs
# Расчет суммарной производительности котлов
dat['Общая производительность']=dat.sum(axis=1)

# Plotting total productivity of the Boilers
# Построение суммарной производительности Котлов
histogram_plotting(dat['Общая производительность'],fig_num=7,title='Общая производительность')

# Removing the first peak
dat=dat[dat['Общая производительность']>10]

histogram_plotting(dat['Общая производительность'],fig_num=8,title='Общая производительность')

