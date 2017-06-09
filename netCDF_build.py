# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 11:04:08 2017

@author: Hannah.N
"""

import hdf_pull
from netCDF4 import Dataset
import numpy as np
from operator import itemgetter


file_info = hdf_pull.file_path('\Aqua')
file_info = file_info + (hdf_pull.file_path('\Terra'))
    
#operator.sorted(file_info, key = lambda x:)
#file = hdf_pull.read_in(files[i])
print file_info
file_info.sort(key = itemgetter(2))
#sat, date_time = hdf_pull.name_data_pull(files, 0)
#hdf_pull.list_sds(file)
#FP_data=hdf_pull.FP_data_pull(file)