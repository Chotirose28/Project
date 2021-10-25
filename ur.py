import pandas as pd
import matplotlib.pyplot as plt

ur = pd.read_csv("UR.csv")

ur_m = ur.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
ur_m = ur_m.reset_index(level=['Year'])
ur_19 = ur_m[ur_m['Year']==2019]
ur_20 = ur_m[ur_m['Year']==2020]

#Temp (celcius)
ur_19.loc[:,'temp'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'temp'].plot(kind='line',label='2020', title='Level of temperature per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Temperature (celcius)")
plt.legend()
plt.show()

#Dew point (celcius)
ur_19.loc[:,'dwpt'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'dwpt'].plot(kind='line',label='2020', title='Level of dew point per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Dew point (celcius)")
plt.legend()
plt.show()

#relative humudity (%)
ur_19.loc[:,'rhum'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'rhum'].plot(kind='line',label='2020', title='Level of relative humudity per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Relative humudity (%)")
plt.legend()
plt.show()

#precipitation level (mm)
ur_19.loc[:,'prcp'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'prcp'].plot(kind='line',label='2020', title='Level of precipitation per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Precipitation level (mm)")
plt.legend()
plt.show()

#wind speed (km/h)
ur_19.loc[:,'wspd'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'wspd'].plot(kind='line',label='2020', title='Level of wind speed per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Wind speed (km/h)")
plt.legend()
plt.show()

#air pressure (hPa)
ur_19.loc[:,'pres'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'pres'].plot(kind='line',label='2020', title='Level of air pressure per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("Air pressure (hPa)")
plt.legend()
plt.show()

#PM2.5 ((µg/m3))
ur_19.loc[:,'PM2.5'].plot(kind='line',label='2019', figsize=(10,5))
ur_20.loc[:,'PM2.5'].plot(kind='line',label='2020', title='Level of PM2.5 per month in Ubon Ratchathani 2019-2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5")
plt.legend()
plt.show()