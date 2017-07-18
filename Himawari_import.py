# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 14:42:07 2017

@author: Hannah.N
"""

import pandas as pd
import datetime
import numpy as np
file_path = "J:\PhD\earth_observation\Data\Oct_2015\H8_201510_atm.csv"

df = pd.read_csv(file_path)
confidence = df.FIRE_CONFIDENCE
FRP = df.FRP_0
latitude = df.LATITUDE
longitude = df.LONGITUDE
year=df.year
month=df.month
day = df.day
time=df.time



year=year.astype(int)
month=month.astype(int)
day=day.astype(int)
time=time.astype(int)
time = time.apply(lambda x: '{0:0>4}'.format(x))
day = day.apply(lambda x: '{0:0>2}'.format(x))
time['datetime'] = year.map(str)+month.map(str)+day.map(str)+time.map(str)
time['datetime'] = pd.to_datetime(time['datetime'],format='%Y%m%d%H%M')
#print time['datetime']


def datetime_pull(): #another way to convert to datetime object
    date_time = []
    for i in range(10000,100000,100):
        times = str(time[i])
        date = datetime.datetime(int(year[i]),int(month[i]),int(day[i]),int(times[0:2]),int(times[2:4]))
        date_time.append(date)
     
    
    df_datetime = pd.DataFrame({'datetime': date_time})
    
  


data = pd.concat([latitude,longitude,FRP,confidence], axis=1)
data = data.set_index(pd.DatetimeIndex(time['datetime']))

start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 0 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 29,23,59))
data_in_period = data.ix[start:end]

#data = data.set_index(['datetime'])
#data_in_period = (data.loc[start_date:end_date])
print data_in_period