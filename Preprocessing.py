# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 01:33:07 2021
Preprocessing data
@author: Chotirose
"""

import pandas as pd

df = pd.DataFrame(columns=['time','time_local','temp','dwpt','rhum','prcp','snow','wdir'
                           ,'wspd','wpgt','pres','tsun','coco'])
year =['19','20']
numf = ['1','2','3','4']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
n = 0
for i in year:
    for j in month:
        for k in numf:
            dF = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/Bangkok_'+j+'_'+i+'_'+k+'.csv')
            df = df.append(dF)