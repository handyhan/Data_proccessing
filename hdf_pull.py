from pyhdf.SD import SD, SDC
import numpy as np



def file_path(sat_name):
    import glob
    data_loc = 'J:\PhD\earth_observation\Data' #'C:\Users\Hannah.N\Documents\Data'
    folder = '\Sept_Oct_2016\MODIS L2'+ sat_name + '_25092016_20102016\\' #sat_name must include \ in front
    file_name='\*'
    files = glob.glob(data_loc+folder+file_name)
    print files
    info = []
    for i in range(0, len(files)):
        sat,date_time = name_data_pull(data_loc, folder, files, i)
        #print files[i]
        info.append([files[i],sat,date_time])
    info = [tuple(x) for x in info]
    return info
    #file_name = '\MYD14.A2016279.1650.006.2016280120152.hdf'
    #MYD14.A2016271.0510.006.2016271135353
    #MOD14.A2016269.0235.006.2016269094430
    #file_name = data_loc+folder+file_name
 


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
        
       
        
def read_in(file_name):
    return SD(file_name, SDC.READ)

def list_sds(file):
    datasets_dic = file.datasets()
    for idx,sds in enumerate(datasets_dic.keys()):
        print idx,sds
 

def sds_data_pull(file, sds_field):  
    sds_obj = file.select(sds_field)
    return sds_obj.get()

def FP_data_pull(file):
    FP_lat = sds_data_pull(file,'FP_latitude')
    FP_long = sds_data_pull(file,'FP_longitude')
    FP_FRP = sds_data_pull(file,'FP_power')
    FP_confidence = sds_data_pull(file,'FP_confidence')
    return np.concatenate(([FP_lat],[FP_long],[FP_FRP],[FP_confidence]),axis=0)

# print np.count_nonzero(data == 7),np.count_nonzero(data == 8),np.count_nonzero(data == 9)


#sat_date_time = name_data_pull()
#file = read_in(files[0])

#FP_data = FP_data_pull() # FP_data is a array with lan,lat,FRP and Confidane
#print FP_data