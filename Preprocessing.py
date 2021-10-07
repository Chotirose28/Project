# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 01:33:07 2021
Preprocessing data
@author: Chotirose
"""

import pandas as pd
import numpy as np

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
    if i == 'Bangkok':
        df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/BK_W.csv',index=False)
    else:
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

#Preprocessing#################################################################
for c in city:
    df = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'_W.csv')
    df.drop(['time','snow','wpgt','tsun','coco','wdir'], axis=1,inplace=True)

    #extract UTC hour, year, month, day
    datetime = df['time_local'].astype(str)
    #hour
    time = [c.split(' ')[1] for c in datetime]
    hour = [c.split(':')[0] for c in time]
    #date
    date = [c.split(' ')[0] for c in datetime]
    year = []
    month = []
    day = []
    l = [i for i in range(1920,2088)]
    #if c == 'CM'
    if c == 'CM':
        r = [i for i in range(0,168)]
        for i in range(len(date)):
            if i in l:
                date[i] = date[i].split('/')
                year.append(date[i][2])
                month.append(date[i][0])
                day.append(date[i][1])
            elif i in r:
                date[i] = date[i].split('/')
                year.append(date[i][2])
                month.append(date[i][0])
                day.append(date[i][1])
            else:
                date[i] = date[i].split('-')
                year.append(date[i][0])
                month.append(date[i][1])
                day.append(date[i][2])
    else:        
        for i in range(len(date)):
            if i in l:
                date[i] = date[i].split('/')
                year.append(date[i][2])
                month.append(date[i][0])
                day.append(date[i][1])
            else:
                date[i] = date[i].split('-')
                year.append(date[i][0])
                month.append(date[i][1])
                day.append(date[i][2])
    #change '3' to '03'
    for i in range(len(month)):
        if month[i] == '3':
            month[i] = '03'
    #insert new column at specific position
    df.insert(0,'Year',year)
    df.insert(1,'Month',month)
    df.insert(2,'Day',day)
    df.insert(3,'UTC Hour',hour)
    df.drop(['time_local'],axis=1,inplace=True)

    #Missing value imputation
    for i in range(4,len(df.columns)):
        n = df.iloc[:,i].isnull().sum()
        if n != 0:
            if i == 7:
                df.iloc[:,i].fillna(0,inplace=True)
            else:
                df.iloc[:,i].fillna(method='bfill',inplace=True)
                df.iloc[:,i].fillna(method='ffill',inplace=True)
                
    #Change date into the same pattern
    df2 = pd.read_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'_PM.csv')
    df2.drop(['PM10_mask','Retrospective'],axis=1,inplace=True)
    df2['Year'] = df2['Year'].astype(str)

    for i in range(1,4):
        for j in range(len(df2)):
            if df2.iloc[j,i] < 10:
                df2.iloc[j,i] = '0' + str(df2.iloc[j,i])
        df2.iloc[:,i] = df2.iloc[:,i].astype(str)

    df3 = df2[(df2['Year'] == '2019')| (df2['Year'] == '2020')]

    #Join 2 table
    new_df = df.merge(df3, how='inner',left_on=['Year','Month','Day','UTC Hour'], 
                  right_on=['Year','Month','Day','UTC Hour'])
    #transform by log10
    for i in range(4,len(new_df.columns)):
        new_df.iloc[:,i] = np.log10(new_df.iloc[:,i]+1)

    #Min-max normalization
    for i in range(4,len(new_df.columns)):
        new_df.iloc[:,i] = (new_df.iloc[:,i] - new_df.iloc[:,i].min())/(new_df.iloc[:,i].max()-new_df.iloc[:,i].min())

    new_df.to_csv('C:/Users/Choti/Documents/270702/Term Project/Data/'+c+'.csv',index=False)

