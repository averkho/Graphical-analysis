# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:57:20 2021

@author: AVERKHO
"""

import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
import numpy as np
import scipy.stats as stats
import plotly.figure_factory as ff

#import plotly.plotly as py


dat=pd.read_excel('./Gravity rollers.xlsx','Rollers_1')
dat2=pd.read_excel('./Gravity rollers.xlsx','Rollers_2')
dat.columns
dat=dat[dat['Shaft length']<100]

fig=go.Figure(data=[go.Histogram(x=dat['Shaft length'],histnorm='density',nbinsx=20)])
#fig.add_trace(go.Histogram(x=dat2['Shaft length'],histnorm='density',nbinsx=20))
fig.update_traces()

plot(fig)

mean=dat['Shaft length'].mean()
std=dat['Shaft length'].std()
x=np.linspace(mean-3*std,mean+3*std,1000)
y=stats.norm.pdf(x,mean,std)
'''
fig2=go.Figure()
fig2.add_trace(go.Histogram(x=dat['Shaft length'],histnorm='density',nbinsx=20))
fig2.add_trace(ff.create_distplot(x))
plot(fig2)
'''
group_labels = ['Group 1']
fig2 = ff.create_distplot([dat['Shaft length']], group_labels,bin_size=0.1,
                         curve_type='normal', show_rug=False # override default 'kde'
                         )
fig2.update_layout(title={'text':'Shaft length of rollers',
                          'y':0.9,
                          'x':0.5,
                          'xanchor':'center',
                          'yanchor':'top'},
                   yaxis={'title':'Density'},
                   xaxis={'title':'mm'})
plot(fig2)