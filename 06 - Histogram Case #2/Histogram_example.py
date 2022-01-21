# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:48:30 2021

@author: AVERKHO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

dat=pd.read_excel('./Boilers.xlsx')

#Creating separate Series for each boiler
boiler_1=dat['Boiler_1']
boiler_2=dat['Boiler_2']
boiler_3=dat['Boiler_3']

def check_non_numeric(df)->str:
    
    ''' checking if the DataFrame contains string values'''
    
    ss=list(df[df.apply(lambda x: isinstance(x,str))].unique())
    return ss


# The lists of non numeric (string) data in each Series
ss_1=check_non_numeric(boiler_1)
ss_2=check_non_numeric(boiler_2)
ss_3=check_non_numeric(boiler_3)

# How many non numeric data do we have?
percent_of_strings=len(boiler_1[boiler_1==ss_1[0]])/len(boiler_1)*100
print(np.round(percent_of_strings,2),'%')

# Removing string data from boiler #1
boiler_1=boiler_1[boiler_1!=ss_1[0]]

# Checking if there are any string data in a Series left
ss_=check_non_numeric(boiler_1)

def histogram_plotting(df,fig_num,title,n_bins=35):
    
    ''' 
    plotting histograms for boilers.
    The finction recieves data in form of Series (df).
    fig_num - the figure number to be plotted
    title - the title of the histogram
    n_bins - number of bins in the histogram
    
    '''
    
    fig=plt.figure(fig_num)
    ax=fig.add_subplot(111)
    ax.hist(df,bins=n_bins,edgecolor='black',facecolor='blue')
    ax.set_title(title)
    ax.set_xlabel('t/h')
    ax.set_ylabel('hours')
    ax.grid(True)

# Boiler #1
histogram_plotting(boiler_1,fig_num=1,title='Boiler #1')

#removing the first peak
boiler_1=boiler_1[boiler_1>10]

histogram_plotting(boiler_1,fig_num=2,title='Boiler #1')

# Boiler #2
histogram_plotting(boiler_2,fig_num=3,title='Boiler #2')

boiler_2=boiler_2[boiler_2>10]

histogram_plotting(boiler_2,fig_num=4,title='Boiler #2')

#Boiler #3
histogram_plotting(boiler_3,fig_num=5,title='Boiler #3')

boiler_3=boiler_3[boiler_3>10]

histogram_plotting(boiler_3,fig_num=6,title='Boiler #3')

# Total productivity calculation and plotting
# Removing string values from the DataFrame
dat=dat[dat['Boiler_1']!=ss_1[0]]

# Reseting index - to simplify math operations with the DataFrame in the future
dat=dat.set_index('Timestamp')

# Calculating total productivity of Boielrs
dat['total_productivity']=dat.sum(axis=1)

# Plotting total productivity of the Boilers
histogram_plotting(dat['total_productivity'],fig_num=7,title='Total productivity')

# Removing the first peak
dat=dat[dat['total_productivity']>10]

histogram_plotting(dat['total_productivity'],fig_num=8,title='Total productivity')

