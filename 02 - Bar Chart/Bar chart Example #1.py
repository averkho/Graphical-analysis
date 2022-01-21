# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 21:30:44 2020

@author: AVERKHO
"""

# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#Importing the data
dat=pd.read_excel('./Lumber defects.xlsx','Data')

'''
Task #1. Evaluate the level of defects in the company. Prioritize the efforts of SixSigma team
'''

# Data preparation
defects=dat['Defects'].value_counts()

def autolabels(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height=rect.get_height() # values of bars
        ax.annotate('{}'.format(height),  # adding values to the bars
                    xy=(rect.get_x()+rect.get_width()/2,height), # coordinates of labels
                    xytext=(0,4), # 4 points vertical offset
                    textcoords="offset points",  # the coordinate system that xytext is given in.
                    ha='center',va='bottom') #horizontal and vertical positions of text
    
# Plotting figure 1
fig=plt.figure(1)
ax=fig.add_subplot(111)
rects=ax.bar(defects.index,defects,color='blue') # PLotting bar chart
ax.set_ylabel('Counts of defects') # Y labels
autolabels(rects) # Labeling the bars
ax.grid(True) # Adding gridlines to the plot
plt.title('Lumber defects') # The title of the chart

'''
Task #2. Compare the first and second quarters and make conclusions.

'''

#Defects by quarters
dat_Q1=dat[dat['Quarter']=='Q1']['Defects'].value_counts()
dat_Q2=dat[dat['Quarter']=='Q2']['Defects'].value_counts()

dat_Q1_Q2=pd.concat([dat_Q1,dat_Q2],axis=1) # concatenating two series into one DataFrame
dat_Q1_Q2.columns=['Q1','Q2'] # Assigning the names of columns
width=0.35 # width of bars

x=np.arange(len(dat_Q1_Q2))  # x-ticks

fig=plt.figure(2)
ax=fig.add_subplot(111)
rects1=ax.bar(x-width/2,dat_Q1_Q2['Q1'],width,label='Quarter 1') # The first bar chart
rects2=ax.bar(x+width/2,dat_Q1_Q2['Q2'],width,label='Quarter 2') # The second bar chart
ax.set_ylabel('Counts of defects') # Y axis label
ax.set_title('The defects by Quarters') # The title of the chart
ax.set_xticks(x)  # setting X axis ticks
ax.set_xticklabels(dat_Q1_Q2.index) # Setting labels to the ticks

autolabels(rects1) # Adding labels to the first bar chart
autolabels(rects2) # Adding labels to the secind bar chart
ax.legend() # Adding legend to the chart
plt.grid(True) # Adding gridlines
fig.tight_layout()
