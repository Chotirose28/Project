# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:08:11 2021

@author: Omen
"""

import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

city = ['BK_Ndt','CM_Ndt','CR_Ndt','NS_Ndt','CB_Ndt','RY_Ndt','RB_Ndt','KB_Ndt','KK_Ndt','UR_Ndt','NT_Ndt','PK_Ndt']

scr = []
rs = []
for c in city:
    df = pd.read_csv('D:/ปอโท Nirawit/Science programing (Wed noon)/Project/Project-Preprocessing/'+c+'.csv')
#df = pd.read_csv('BK_Ndt.csv')

    x = df.drop('PM2.5', axis=1)
    y = df['PM2.5']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
    LR = LinearRegression()
    model=LR.fit(x_train,y_train)
    y_prediction =  LR.predict(x_test)
    score = r2_score(y_test,y_prediction)
    mse = mean_squared_error(y_test,y_prediction)
    rsme = sqrt(mean_squared_error(y_test,y_prediction))
    print(c,'r2 score is', score)
    print(c,'mean_sqrd_error is==',mse)
    print(c,'root_mean_squared error of is==',rsme)
    scr.append(score)
    rs.append(rsme)
    



    