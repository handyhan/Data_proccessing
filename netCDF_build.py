# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 11:04:08 2017

@author: Hannah.N
"""

import hdf_pull
from netCDF4 import Dataset
import numpy as np
from operator import itemgetter

def file_info():
    file_info = hdf_pull.file_path('\Aqua')
    file_info = file_info + (hdf_pull.file_path('\Terra'))
    file_info.sort(key = itemgetter(2))
    return file_info

#print file_info()

#FP_data=hdf_pull.FP_data_pull(file)
#file = hdf_pull.read_in(files[i])