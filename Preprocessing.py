# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 01:33:07 2021
Preprocessing data
@author: Chotirose
"""

import pandas as pd

#combine data .csv of each week of the city together and export one file per each city
year =['19','20']
numf = ['1','2','3','4','5']
month = ['01','02','03','04','05','06','07','08','09','10','11','12']
city = ['Bangkok','CM','CR','NS','CB','RY','RB','KB','KK','UR','NT','PK']

for i in city:
    df = pd.DataFrame(columns=['time','time_local','temp','dwpt','rhum','prcp','snow','wdir'
                           ,'wspd','wpgt','pres','tsun','coco'])
    for j in year:
        for k in month:
            if k == '02': #Feb is the only month which has 4 week (28 - 29 days)
                for m in numf[:-1]:
                    data = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'_'+k+'_'+j+'_'+m+'.csv')
                    df = df.append(data)
            else: #another months cover 5 weeks (30 - 31 days)
                for m in numf:
                    data = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'_'+k+'_'+j+'_'+m+'.csv')
                    df = df.append(data)
    df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+i+'_W.csv',index=False)
    
#change .txt file to .csv file
city = ['BK','CM','CR','NS','CB','RY','RB','KB','KK','UR','NT','PK']
for c in city:
    f = open('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'.txt','r')
    lines = f.readlines()
    f.close()
    data = lines[9:]
    data[0] = data[0].replace('%', '')
    data[0] = data[0].split(',')
    
    for i in range(len(data[0])):
        data[0][i] = data[0][i].strip()
    
    for i in range(1,len(data)):
        data[i] = data[i].replace('\t', ',')
        data[i] = data[i].strip()
        data[i] = data[i].split(',')
        for j in range(len(data[i])):
            if j in [0,1,2,3]:
                data[i][j] = int(data[i][j])
            else:
                data[i][j] = float(data[i][j])
    head = data[0]
    data = data[1:]
    df = pd.DataFrame(data,columns=head)
    df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'_PM.csv',index=False)

