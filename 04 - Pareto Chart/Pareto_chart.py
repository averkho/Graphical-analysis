# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:55:25 2020

@author: AVERKHO
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

dat=pd.read_excel('./Rejects PM.xlsx')


def pareto_chart(dat,category:str,values:str,title=None,percent_to_combne=None,k=1):
    
    """ 
    The function for construction Pareto chart. It should receive dataframe consisting of two columns:
    categorical variable and its values. Then it plot a pareto chart 
    dat - DataFrame
    category - the name of categorical column (str)
    values - value of categories (float)
    """
    dat=dat.groupby(by=category).sum() # Grouping DataFrame by category and summation 
    dat=dat.sort_values(by=values,ascending=False) # Sorting by values in descending order
    dat['percent']=np.round(dat[values]/dat[values].sum()*100,2) # Adding percents to DataFrame
    dat['cum_percent']=dat['percent'].cumsum()                   # Adding cumulative percent to DataFrame
    dat.reset_index(inplace=True)                               # Reseting index
    # Combing categories after which is less then (1-percent_to_combine)
    if percent_to_combne is not None:
        for i in range(dat.shape[0]):
            if dat.iloc[i]['cum_percent']>=percent_to_combne:
                dat.at[i,category]='other'
        
        dat_other=dat[dat[category]=='other']
        dat_other=dat_other.groupby(category).sum()
        dat_other.reset_index(inplace=True)
        dat_other['cum_percent']=100
        dat=dat[dat[category]!='other']
        dat=pd.concat([dat,dat_other])
    dat.set_index(category,inplace=True)    
    fig=plt.figure(k)
    ax=fig.add_subplot(111)
    dat[values].plot(kind='bar',ax=ax)
    ax.set_ylabel(values)
    ax2=ax.twinx()
    dat['cum_percent'].plot(kind='line',color='red',ax=ax2)
    ax2.set_ylabel('%')
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    
    
    
    
pareto_chart(dat,category='Reason',values='tons',title='Rejects on PM',percent_to_combne=95)

dat_2=pd.read_excel('./Rejected_rolls.xlsx')

pareto_chart(dat_2,category='Reason',values='kg',title='Rejects 2020',percent_to_combne=95,k=2)

# Converting kg to tons

dat_2['tons']=dat_2['kg']/1000

pareto_chart(dat_2,category='Reason',values='tons',title='Rejects 2020',percent_to_combne=95,k=3)

