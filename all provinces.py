import pandas as pd
import matplotlib.pyplot as plt

bk = pd.read_csv("BK.csv")
bk_m = bk.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
bk_m = bk_m.reset_index(level=['Year'])
bk_19 = bk_m[bk_m['Year']==2019]
bk_20 = bk_m[bk_m['Year']==2020]

cb = pd.read_csv("CB.csv")
cb_m = cb.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
cb_m = cb_m.reset_index(level=['Year'])
cb_19 = cb_m[cb_m['Year']==2019]
cb_20 = cb_m[cb_m['Year']==2020]

cm = pd.read_csv("CM.csv")
cm_m = cm.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
cm_m = cm_m.reset_index(level=['Year'])
cm_19 = cm_m[cm_m['Year']==2019]
cm_20 = cm_m[cm_m['Year']==2020]

cr = pd.read_csv("CR.csv")
cr_m = cr.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
cr_m = cr_m.reset_index(level=['Year'])
cr_19 = cr_m[cr_m['Year']==2019]
cr_20 = cr_m[cr_m['Year']==2020]

kb = pd.read_csv("KB.csv")
kb_m = kb.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
kb_m = kb_m.reset_index(level=['Year'])
kb_19 = kb_m[kb_m['Year']==2019]
kb_20 = kb_m[kb_m['Year']==2020]

kk = pd.read_csv("KK.csv")
kk_m = kk.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
kk_m = kk_m.reset_index(level=['Year'])
kk_19 = kk_m[kk_m['Year']==2019]
kk_20 = kk_m[kk_m['Year']==2020]

ns = pd.read_csv("NS.csv")
ns_m = ns.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
ns_m = ns_m.reset_index(level=['Year'])
ns_19 = ns_m[ns_m['Year']==2019]
ns_20 = ns_m[ns_m['Year']==2020]

nt = pd.read_csv("NT.csv")
nt_m = nt.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
nt_m = nt_m.reset_index(level=['Year'])
nt_19 = nt_m[nt_m['Year']==2019]
nt_20 = nt_m[nt_m['Year']==2020]

pk = pd.read_csv("PK.csv")
pk_m = pk.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
pk_m = pk_m.reset_index(level=['Year'])
pk_19 = pk_m[pk_m['Year']==2019]
pk_20 = pk_m[pk_m['Year']==2020]

rb = pd.read_csv("RB.csv")
rb_m = rb.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
rb_m = rb_m.reset_index(level=['Year'])
rb_19 = rb_m[rb_m['Year']==2019]
rb_20 = rb_m[rb_m['Year']==2020]

ry = pd.read_csv("RY.csv")
ry_m = ry.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
ry_m = ry_m.reset_index(level=['Year'])
ry_19 = ry_m[ry_m['Year']==2019]
ry_20 = ry_m[ry_m['Year']==2020]

ur = pd.read_csv("UR.csv")
ur_m = ur.groupby(['Year','Month'])[['temp','dwpt','rhum','prcp','wspd','pres','PM2.5']].mean()
ur_m = ur_m.reset_index(level=['Year'])
ur_19 = ur_m[ur_m['Year']==2019]
ur_20 = ur_m[ur_m['Year']==2020]

#-----------------------------------------------------------------------------------------------------

#2019
bk_19.loc[:,'PM2.5'].plot(kind='line',label='Bangkok', figsize=(10,5))
cb_19.loc[:,'PM2.5'].plot(kind='line',label='Chon Buri', figsize=(10,5))
cm_19.loc[:,'PM2.5'].plot(kind='line',label='Chiang Mai', figsize=(10,5))
cr_19.loc[:,'PM2.5'].plot(kind='line',label='Chiang Rai', figsize=(10,5))
kb_19.loc[:,'PM2.5'].plot(kind='line',label='Kanchanaburi', figsize=(10,5))
kk_19.loc[:,'PM2.5'].plot(kind='line',label='Khon Kaen', figsize=(10,5))
ns_19.loc[:,'PM2.5'].plot(kind='line',label='Nakhon Sawan', figsize=(10,5))
nt_19.loc[:,'PM2.5'].plot(kind='line',label='Nakhon Si', figsize=(10,5))
pk_19.loc[:,'PM2.5'].plot(kind='line',label='Phuket', figsize=(10,5))
rb_19.loc[:,'PM2.5'].plot(kind='line',label='Ratchaburi', figsize=(10,5))
ry_19.loc[:,'PM2.5'].plot(kind='line',label='Rayong', figsize=(10,5))
ur_19.loc[:,'PM2.5'].plot(kind='line',label='Ubon', title='PM2.5 levels of all provinces in 2019', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5 (µg/m3)")
plt.legend()
plt.show()

#2020
bk_20.loc[:,'PM2.5'].plot(kind='line',label='Bangkok', figsize=(10,5))
cb_20.loc[:,'PM2.5'].plot(kind='line',label='Chon Buri', figsize=(10,5))
cm_20.loc[:,'PM2.5'].plot(kind='line',label='Chiang Mai', figsize=(10,5))
cr_20.loc[:,'PM2.5'].plot(kind='line',label='Chiang Rai', figsize=(10,5))
kb_20.loc[:,'PM2.5'].plot(kind='line',label='Kanchanaburi', figsize=(10,5))
kk_20.loc[:,'PM2.5'].plot(kind='line',label='Khon Kaen', figsize=(10,5))
ns_20.loc[:,'PM2.5'].plot(kind='line',label='Nakhon Sawan', figsize=(10,5))
nt_20.loc[:,'PM2.5'].plot(kind='line',label='Nakhon Si', figsize=(10,5))
pk_20.loc[:,'PM2.5'].plot(kind='line',label='Phuket', figsize=(10,5))
rb_20.loc[:,'PM2.5'].plot(kind='line',label='Ratchaburi', figsize=(10,5))
ry_20.loc[:,'PM2.5'].plot(kind='line',label='Rayong', figsize=(10,5))
ur_20.loc[:,'PM2.5'].plot(kind='line',label='Ubon', title='PM2.5 levels of all provinces in 2020', figsize=(10,5))
plt.xlabel("Month")
plt.ylabel("PM2.5 (µg/m3)")
plt.legend()
plt.show()