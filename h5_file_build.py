"""
Created on Tue May 30 09:41:08 2017

@author: Han
"""

import h5py
import numpy as np
import hdf_pull



f = h5py.File('Sept_Oct_16', 'w')


files = hdf_pull.file_path()
file = hdf_pull.read_in(files[0])

sat_date_time = hdf_pull.name_data_pull()
sat, date_time = sat_date_time

#hdf_pull.list_sds()
FP_data = hdf_pull.FP_data_pull() # FP_data is a array with lat,long,FRP and Confidane

PO = f.create_group("PO_data")

print PO.name

#print dir(f)

f.close()