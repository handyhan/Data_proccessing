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
fire_conf = df.FIRE_CONFIDENCE
FRP = df.FRP_0
latitude = df.LATITUDE
longitude = df.LONGITUDE
year=df.year
month=df.month
day = df.day
time=df.time
time = time.apply(lambda x: '{0:0>6}'.format(x))
    
def datetime_pull():
    date_time = []
    for i in range(10000,100000,100):
        times = str(time[i])
        date = datetime.datetime(int(year[i]),int(month[i]),int(day[i]),int(times[0:2]),int(times[2:4]))
        date_time.append(date)
        
    
    df_datetime = pd.DataFrame({'datetime': date_time})
    
    data = pd.concat([df_datetime,latitude[0:10],longitude[0:10],FRP[0:10],fire_conf[0:10]], axis=1)
    return data

data = datetime_pull()

print data.iloc[np.r_[0:10, -10:0]]
    
data.index = data['datetime']
start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 0 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 29,23,59))
data_in_period = data.ix[start:end]

#data = data.set_index(['datetime'])
#data_in_period = (data.loc[start_date:end_date])
print data_in_period.size
