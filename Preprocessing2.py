# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 20:56:13 2021

@author: Choti
"""

import pandas as pd

city = ['BK','CM','CR','NS','CB','RY','RB','KB','KK','UR','NT','PK']

for c in city:
    df = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'.csv')
    df.drop(['Year','Month','Day','UTC Hour'],axis=1,inplace=True)
    df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'_Ndt.csv',index=False)