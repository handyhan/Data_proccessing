# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 14:42:07 2017

@author: Hannah.N
"""

import pandas as pd

file_path = "J:\PhD\earth_observation\Data\Oct_2015\H8_201510_atm.csv"

df = pd.read_csv(file_path)
fire_conf = df.FIRE_CONFIDENCE
FRP = df.FRP_0
latitude = df.LATITUDE
longitude = df.LONGITUDE
year=df.year
month=df.month
day = df.day
time=df.tim