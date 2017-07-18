"""
Created on Tue Jul 18 11:42:41 2017
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


#pull and lable append into data
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
        data = pd.DataFrame({'datetime': cut, 'SAT':SAT, 'LATITUDE': FP_data[0] , 'LONGITUDE': FP_data[1],'FRP':FP_data[2],'confidence':FP_data[3]})
        appended_data.append(data)
        
        
    except ValueError as error:
        bad_files = []
        bad_files.append(files)
        print'hey'
   
        
print bad_files

#put it all together an swap to datetime, make datetime the index
data = pd.concat(appended_data,axis=0) 
data['datetime'] = pd.to_datetime(data['datetime'],format='%Y%j.%H%M')
data = data.set_index(pd.DatetimeIndex(data['datetime']))


#select on fires occuring in time window
start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 0 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 29,23,59))
data = data.ix[start:end]

#select only fires in spatial range
data = data[(data['LATITUDE'] < -17.2) & (data['LATITUDE'] > -18.2)]
data = data[(data['LONGITUDE'] < 130.8) & (data['LONGITUDE'] > 128.2)]

            
#save to file
data.to_csv('J:\PhD\earth_observation\Data\Oct_2015\MODIS_20151014_20151029_177_129.csv',sep=',')




"""
with open('J:\PhD\earth_observation\Databad_files\Oct_2015\MODIS L2\bad_files', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(bad_files) 
"""