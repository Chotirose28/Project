import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

kb = pd.read_csv("KB.csv")

kb_m = kb.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
kb_m = kb_m.reset_index(level=['Year'])
kb_19 = kb_m[kb_m['Year']==2019]
kb_20 = kb_m[kb_m['Year']==2020]

#Temp (celcius)
kb_19.loc[:,'temp'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'temp'].plot(kind='line',label='2020', title='Level of temperature per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Temperature (celcius)")
plt.legend()
plt.show()

#Dew point (celcius)
kb_19.loc[:,'dwpt'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'dwpt'].plot(kind='line',label='2020', title='Level of dew point per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Dew point (celcius)")
plt.legend()
plt.show()

#relative humudity (%)
kb_19.loc[:,'rhum'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'rhum'].plot(kind='line',label='2020', title='Level of relative humudity per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Relative humudity (%)")
plt.legend()
plt.show()

#precipitation level (mm)
kb_19.loc[:,'prcp'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'prcp'].plot(kind='line',label='2020', title='Level of precipitation per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Precipitation level (mm)")
plt.legend()
plt.show()

#wind speed (km/h)
kb_19.loc[:,'wspd'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'wspd'].plot(kind='line',label='2020', title='Level of wind speed per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Wind speed (km/h)")
plt.legend()
plt.show()

#air pressure (hPa)
kb_19.loc[:,'pres'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'pres'].plot(kind='line',label='2020', title='Level of air pressure per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Air pressure (hPa)")
plt.legend()
plt.show()

#PM2.5 ((µg/m3))
kb_19.loc[:,'PM2.5'].plot(kind='line',label='2019', figsize=(10,5))
kb_20.loc[:,'PM2.5'].plot(kind='line',label='2020', title='Level of PM2.5 per month in Kanchanaburi 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.legend()
plt.show()

#Correlation plot
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()
ax.set_title('Correlation Plot in Kanchanaburi', fontsize=20)
sns.heatmap(kb_m[['temp', 'dwpt', 'rhum', 'prcp', 
                 'wspd','pres', 'PM2.5']].corr(), ax=ax)
