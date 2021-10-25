# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:44:25 2021

@author: Omen
"""

import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
import statsmodels.api as sm



score_cv = []
score_train = []
score_test = []
rs = []


df = pd.read_csv('D:/ปอโท Nirawit/Science programing (Wed noon)/Project/Project-Preprocessing/BK.csv')

x_col = df.drop(['PM2.5'] ,axis=1)
y = df[['PM2.5']]
    
def get_stats():
    x = x_col
    results = sm.OLS(y, x).fit()
    print(results.summary())
get_stats()
    
x_col=x_col.drop(["prcp"],axis = 1)
get_stats()

x_train, x_test, y_train, y_test = train_test_split(x_col, y, test_size = 0.2, random_state = 42)

LR = LinearRegression()
LR.fit(x_train,y_train)

y_pred_train = LR.predict(x_train)
y_pred_test =  LR.predict(x_test)
score1 = cross_val_score(LR, x_train, y_train, scoring='r2', cv=10)
score2 = r2_score(y_train,y_pred_train)
score3 = r2_score(y_test,y_pred_test)
mse = mean_squared_error(y_test,y_pred_test)
rsme = sqrt(mean_squared_error(y_test,y_pred_test))
print('r2 train score is', score2)
print('r2 test score is', score3)
print('r2 CV score is', score1.mean())
#print(c,'mean_sqrd_error is==',mse)
print('root_mean_squared error of is==',rsme,'\n')
score_test.append(score3)
score_train.append(score2)
score_cv.append(score1.mean())
rs.append(rsme)

fig, ax = plt.subplots(figsize=(7, 3.5))

ax.plot(x_test, y_pred_test, color='k', label='Regression model')
ax.scatter(x_col, y, edgecolor='k', facecolor='grey', alpha=0.7, label='Sample data')
ax.set_ylabel('Prediction', fontsize=14)
ax.set_xlabel('Actual', fontsize=14)
ax.legend(facecolor='white', fontsize=11)
ax.text(0.55, 0.15, '$y = %.2f x_1 - %.2f $' % (LR.coef_[0], abs(LR.intercept_)), fontsize=17, transform=ax.transAxes)

fig.tight_layout()