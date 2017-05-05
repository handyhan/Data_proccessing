from pyhdf.SD import SD, SDC
import numpy as np

data_loc = 'C:\Users\Hannah.N\Documents\Data'
folder = '\Sept_Oct2016_data\MODIS L2\Aqua_25092016_20102016'
file_type='\*.hdf'

def file_path():
    import glob
    return glob.glob(data_loc+folder+file_type)
    #file_name = '\MYD14.A2016279.1650.006.2016280120152.hdf'
    #file_name = data_loc+folder+file_name
 
 
files = file_path()

def name_data_pull():
    import datetime
    for file in files:
        file = 'M'+file.strip(data_loc+folder)
        sat = file[0:3]
        date = file[7:14]
        time = file[15:19]
        date_time =datetime.datetime(int(date[0:4]), 1, 1,int(time[0:2]),int(time[2:4]))+ datetime.timedelta(int(date[4:7]) - 1) 
        date_time =date_time + datetime.timedelta(0,0,0,0,0,8) 
        return [sat,date_time]
        
        #from_zone = tz.gettz('UTC')
        #to_zone = date_time + datetime.timedelta(0,0,0,8)
        #date_time = date_time.replace(tzinfo=from_zone)
        #date_time = date_time.astimezone(to_zone.tzinfo)
        
def read_in(file_name):
    return SD(file_name, SDC.READ)

def list_sds():
    datasets_dic = file.datasets()
    for idx,sds in enumerate(datasets_dic.keys()):
        print idx,sds
 

def sds_data_pull(sds_field):  
    sds_obj = file.select(sds_field)
    return sds_obj.get()

def FP_data_pull():
    FP_lat = sds_data_pull('FP_latitude')
    FP_long = sds_data_pull('FP_longitude')
    FP_FRP = sds_data_pull('FP_power')
    FP_confidence = sds_data_pull('FP_confidence')
    return np.concatenate(([FP_lat],[FP_long],[FP_FRP],[FP_confidence]),axis=0)

# print np.count_nonzero(data == 7),np.count_nonzero(data == 8),np.count_nonzero(data == 9)


sat_date_time = name_data_pull()
file = read_in(files[0])

FP_data = FP_data_pull()
print FP_data