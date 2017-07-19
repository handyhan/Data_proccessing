# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 14:42:07 2017

@author: Hannah.N
"""

import pandas as pd
import datetime
import numpy as np
file_path = "J:\PhD\earth_observation\Data\Oct_2015\H8_201510_atm.csv"

#read in the file and data
df = pd.read_csv(file_path)
confidence = df.FIRE_CONFIDENCE
FRP = df.FRP_0
latitude = df.LATITUDE
longitude = df.LONGITUDE
year=df.year
month=df.month
day = df.day
time=df.time


#format columns into datetime object
year=year.astype(int)
month=month.astype(int)
day=day.astype(int)
time=time.astype(int)
time = time.apply(lambda x: '{0:0>4}'.format(x))
day = day.apply(lambda x: '{0:0>2}'.format(x))
time['datetime'] = year.map(str)+month.map(str)+day.map(str)+time.map(str)
time['datetime'] = pd.to_datetime(time['datetime'],format='%Y%m%d%H%M')

#make dataframe of alldata indexed with datetime
data = pd.concat([latitude,longitude,FRP,confidence], axis=1)
data = data.set_index(pd.DatetimeIndex(time['datetime']))


#select time period can edit period here
start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 0 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 29,23,59))
data = data.ix[start:end]

#select latitude and longitude of interest
data = data[(data['LATITUDE'] < -17.2) & (data['LATITUDE'] > -18.2)]
data = data[(data['LONGITUDE'] < 130.8) & (data['LONGITUDE'] > 128.2)]

#write the data to a seperate file
data.to_csv('J:\PhD\earth_observation\Data\Oct_2015\H8_20151014_20151029_177_129.csv',sep=',')