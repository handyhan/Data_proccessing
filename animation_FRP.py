# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 10:58:05 2017

@author: Hannah.N
"""

import matplotlib.animation as animation
import hdf_pull
import FRP_map_plot

files = hdf_pull.file_path()

sat_date_time = []
for i in range (0,len(files)):
    sat_date_time.append(hdf_pull.name_data_pull(i))

    

i=0
#print files[0]
file = hdf_pull.read_in(files[i])
#print file
FP_data = hdf_pull.FP_data_pull()
FRP_map_plot.plot_fire(FP_data) 

#######
#J:\PhD\earth_observation\Data\Sept_Oct_2016\MODIS L2\Aqua_25092016_20102016\MYD14.A2016289.0500.006.2016289123048.hdf
#J:\PhD\earth_observation\Data\Sept_Oct_2016\MODIS L2\Aqua_25092016_20102016\MYD14.A2016289.0500.006.2016289123048.hdf