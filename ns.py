import pandas as pd
import matplotlib.pyplot as plt

ns = pd.read_csv("NS.csv")

ns_m = ns.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
ns_m = ns_m.reset_index(level=['Year'])
ns_19 = ns_m[ns_m['Year']==2019]
ns_20 = ns_m[ns_m['Year']==2020]

#Temp (celcius)
ns_19.loc[:,'temp'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'temp'].plot(kind='line',label='2020', title='Level of temperature per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Temperature (celcius)")
plt.legend()
plt.show()

#Dew point (celcius)
ns_19.loc[:,'dwpt'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'dwpt'].plot(kind='line',label='2020', title='Level of dew point per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Dew point (celcius)")
plt.legend()
plt.show()

#relative humudity (%)
ns_19.loc[:,'rhum'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'rhum'].plot(kind='line',label='2020', title='Level of relative humudity per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Relative humudity (%)")
plt.legend()
plt.show()

#precipitation level (mm)
ns_19.loc[:,'prcp'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'prcp'].plot(kind='line',label='2020', title='Level of precipitation per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Precipitation level (mm)")
plt.legend()
plt.show()

#wind speed (km/h)
ns_19.loc[:,'wspd'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'wspd'].plot(kind='line',label='2020', title='Level of wind speed per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Wind speed (km/h)")
plt.legend()
plt.show()

#air pressure (hPa)
ns_19.loc[:,'pres'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'pres'].plot(kind='line',label='2020', title='Level of air pressure per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Air pressure (hPa)")
plt.legend()
plt.show()

#PM2.5 ((µg/m3))
ns_19.loc[:,'PM2.5'].plot(kind='line',label='2019', figsize=(10,5))
ns_20.loc[:,'PM2.5'].plot(kind='line',label='2020', title='Level of PM2.5 per month in Nakhon Sawan 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.legend()
plt.show()

