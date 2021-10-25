import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

kk = pd.read_csv("KK.csv")

kk_m = kk.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
kk_m = kk_m.reset_index(level=['Year'])
kk_19 = kk_m[kk_m['Year']==2019]
kk_20 = kk_m[kk_m['Year']==2020]

#Temp (celcius)
kk_19.loc[:,'temp'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'temp'].plot(kind='line',label='2020', title='Level of temperature per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Temperature (celcius)")
plt.legend()
plt.show()

#Dew point (celcius)
kk_19.loc[:,'dwpt'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'dwpt'].plot(kind='line',label='2020', title='Level of dew point per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Dew point (celcius)")
plt.legend()
plt.show()

#relative humudity (%)
kk_19.loc[:,'rhum'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'rhum'].plot(kind='line',label='2020', title='Level of relative humudity per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Relative humudity (%)")
plt.legend()
plt.show()

#precipitation level (mm)
kk_19.loc[:,'prcp'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'prcp'].plot(kind='line',label='2020', title='Level of precipitation per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Precipitation level (mm)")
plt.legend()
plt.show()

#wind speed (km/h)
kk_19.loc[:,'wspd'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'wspd'].plot(kind='line',label='2020', title='Level of wind speed per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Wind speed (km/h)")
plt.legend()
plt.show()

#air pressure (hPa)
kk_19.loc[:,'pres'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'pres'].plot(kind='line',label='2020', title='Level of air pressure per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Air pressure (hPa)")
plt.legend()
plt.show()

#PM2.5 ((µg/m3))
kk_19.loc[:,'PM2.5'].plot(kind='line',label='2019', figsize=(10,5))
kk_20.loc[:,'PM2.5'].plot(kind='line',label='2020', title='Level of PM2.5 per month in Khon Kaen 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.legend()
plt.show()

#Correlation plot
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.set_title('Correlation Plot in Khon Kaen', fontsize=20)
sns.heatmap(kk_m[['temp', 'dwpt', 'rhum', 'prcp', 
                 'wspd','pres', 'PM2.5']].corr(), ax=ax)