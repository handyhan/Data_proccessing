# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 11:42:41 2017

@author: Hannah.N
"""
#Pull data from hdf MODIS with pandas

import pandas as pd
import datetime
import numpy as np
import glob
import csv
import hdf_pull


data_loc = 'J:\PhD\earth_observation\Data\Oct_2015\MODIS L2\*'
path_cut = 'J:\PhD\earth_observation\Data\Oct_2015\MODIS L2\\'
#pull and lable terra data
appended_data=[]
for files in glob.glob(data_loc):
    try:
        #print x[0]
        stuff = hdf_pull.read_in(files)
        FP_data = hdf_pull.FP_data_pull(stuff)
        sat = files.replace(path_cut,"")[0:3]
        cut =files.replace(path_cut,"")
        cut = cut.replace(cut[0:7],'')
        cut = (cut.replace(cut[12:],''))
        date = np.full((1,(FP_data[0].size)),cut,dtype=float)
        SAT = [sat for x in range((FP_data[0].size))]
        data = pd.DataFrame({'datetime': cut, 'SAT':SAT, 'LATIDUTE': FP_data[0] , 'LONGITUDE': FP_data[1],'FRP':FP_data[2],'confidence':FP_data[3]})
        appended_data.append(data)
        

        """
        print datetime.datetime.strptime(files.replace(path_cut,""),"14.A%Y*")
        print datetime
        data = pd.DataFrame({'datetime': files.replace(path_cut,"")[4:] , 'SAT':sat, 'LATIDUTE': FP_data[0] , 'LONGITUDE': FP_data[1],'FRP':FP_data[2],'confidence':FP_data[3]})
        #data['datetime'] = pd.to_datetime(data['datetime'],format='14.A%Y%d.%H%M')
        #print data['datetime']"""
        
        
        
        
    except ValueError as error:
        bad_files = []
        bad_files.append(files)
        print'hey'
        
print bad_files
data = pd.concat(appended_data,axis=0) 
data['datetime'] = pd.to_datetime(data['datetime'],format='%Y%j.%H%M')

"""
with open('J:\PhD\earth_observation\Databad_files\Oct_2015\MODIS L2\bad_files', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(bad_files)

    
 

for files in glob.glob(terra_files):
    hdf = pd.HDFStore(files)
    print hdf
     
    
    
  

#read in the file and data
df = pd.read_csv(file_path)
confidence = df.FIRE_CONFIDENCE
FRP = df.FRP_0
latitude = df.LATITUDE
longitude = df.LONGITUDE
year=df.year
month=df.month
day = df.day
time=df.time """