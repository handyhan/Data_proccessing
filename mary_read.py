# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:37:42 2017

@author: Hannah.N
"""

from pyhdf.SD import SD, SDC
import numpy as np


#select the folder and file you want to get data from
def file_path():
    import glob
    data_loc = 'C:\Users\Hannah.N' #'C:\Users\Hannah.N\Documents\Data'
    folder = '\Downloads' #sat_name must include \ in front
    file_name='\MOD11A1.A2016241.h26v04.005.2016243042221.hdf'
    info = glob.glob(data_loc+folder+file_name)
    return info
    
    #file_name = '\MYD14.A2016279.1650.006.2016280120152.hdf'
    #MYD14.A2016271.0510.006.2016271135353
    #MOD14.A2016269.0235.006.2016269094430
    #file_name = data_loc+folder+file_name
 

#pull the time and date from the filename (not UTC)
def name_data_pull(data_loc, folder, files,i):
    import datetime
    file = files[i].replace(data_loc + folder,"") 
    sat = file[0:3]
    date = file[7:14]
    time = file[15:19]
    #print sat,date,time
    date_time =datetime.datetime(int(date[0:4]), 1, 1,int(time[0:2]),int(time[2:4]))+ datetime.timedelta(int(date[4:7]) - 1) 
    date_time =date_time + datetime.timedelta(0,0,0,0,0,8) 
    return [sat,date_time]
        
       
#read in the hdf file
def read_in(file_name):
    return SD(file_name, SDC.READ)

#list the datasets in the file
def list_sds(file):
    datasets_dic = file.datasets()
    for idx,sds in enumerate(datasets_dic.keys()):
        print idx,sds
 
#pull the data from a spesific dataset called 'sds_feild'
def sds_data_pull(file, sds_field):  
    sds_obj = file.select(sds_field)
    return sds_obj.get()

#pull data from multiple datasets in the file and put them all in 1 array (must be of the same dimentions)
def FP_data_pull(file):
    LST_Day = sds_data_pull(file,'LST_Day_1km')
    Emis_31 = sds_data_pull(file,'Emis_31')
    LST_Night = sds_data_pull(file,'LST_Night_1km')
    LST_Night = sds_data_pull(file,'LST_Night_1km')
    return np.concatenate(([LST_Day],[Emis_31],[LST_Night],[LST_Night]),axis=0)

#running the above functions to get out data from hdf file
info = file_path()
file = read_in(info[0])
print list_sds(file)

data = FP_data_pull(file)
print data

