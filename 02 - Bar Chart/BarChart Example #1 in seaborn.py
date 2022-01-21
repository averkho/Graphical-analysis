# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 22:40:24 2020

@author: AVERKHO
"""


#importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.close('all')

# Importing data
dat=pd.read_excel('./Lumber defects.xlsx','Data')



defects=dat['Defects'].value_counts()

def autolabel(rects):
    for p in rects.patches:
        x=p.get_x()+p.get_width()/2 # x coordinate of the label
        y=p.get_y()+p.get_height()*1.05 # y coordinatw of the label
        value='{}'.format(int(p.get_height())) # value of the label
        ax.text(x,y,value,ha='center') # adding labels the the figure



fig=plt.figure(1)
ax=fig.add_subplot(111)
rects=sns.barplot(x=defects.index,y=defects) # bar plot
rects.set_title('Lumber defects',fontsize=13,style='italic') # title of the figure
rects.set_ylabel('Counts') # title of y axes
ax.grid(True) # gridlines
autolabel(rects)

dat_tab=dat.groupby(['Defects','Quarter']).agg({'Defects':'count'})
dat_tab.columns=['Counts']
dat_tab=pd.DataFrame(dat_tab)
dat_tab=dat_tab.reset_index()

fig=plt.figure(2)
ax=fig.add_subplot(111)
rects=sns.barplot(x='Defects',y='Counts',data=dat_tab,
                  hue='Quarter',order=defects.index
                  )
ax.set_title('Lumber defects by quarters')
autolabel(rects)
ax.grid()
fig.tight_layout()
