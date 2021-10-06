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
numf = ['1','2','3','4','5']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
city = ['Bangkok','CM','CR','NS','CB','RY','RB','KB','KK','UR','NT','PK']

for i in city:
    for j in year:
        for k in month:
            if k == '02':
                for m in numf[:-1]:
                    data = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'_'+k+'_'+j+'_'+m+'.csv')
                    df = df.append(data)
            else:
                for m in numf:
                    data = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'_'+k+'_'+j+'_'+m+'.csv')
                    df = df.append(data)
    df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'.csv',index=False)



