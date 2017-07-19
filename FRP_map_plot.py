import hdf_pull 
import netCDF_build as netcdf
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv

files = hdf_pull.file_path("\Aqua")
#print files
"""plotting frp with frp intensity colour for single hdf file"""
def plot_fire(FP_data,i,date_time):
    # FP_data is a array with lat,long,FRP and Confidane
    
    latitude = FP_data[0,:]
    longitude = FP_data[1,:]
    FRP=FP_data[2,:]
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'i' means use intermediate resolution coastlines.
    # lon_0, lat_0 are the central longitude and latitude of the projection.
    m = Basemap(llcrnrlon=124,llcrnrlat=-17,urcrnrlon=129,urcrnrlat=-14,
                resolution='i',projection='tmerc',lon_0=126,lat_0=-15)
                
    m.drawcoastlines()
    m.drawmapboundary()#(color='lightgray',fill_color='aqua')
    m.fillcontinents(lake_color='aqua',zorder=0)
    # draw parallels and meridians.
    
    m.drawparallels(np.arange(-40,61.,0.5), labels = [True])
    m.drawmeridians(np.arange(100.,140.,0.5), labels = [True])
    #m.drawmapboundary(fill_color='aqua')
    #FRP.max()
    x, y = m(longitude, latitude)
    m.scatter(x, y, c=FRP, s = 150, marker ='^', zorder=10,norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=(1000)))
    m.shadedrelief()
    cb = m.colorbar()
    cb.set_ticks([0,10,100,500,1000])
    plt.title(date_time)
    plt.show()
    plt.savefig('C:\Users\Hannah.N\Documents\Data\Sept_Oct2016_data\images\MODIS_'+ str(i) +'.png')
    plt.close()

file_info = netcdf.file_info()
#print file_info


i=1
for x in file_info:
    try:
        #print x[0]
        data = hdf_pull.read_in(x[0])
        FP_data = hdf_pull.FP_data_pull(data)
        date_time = x[2]
        plot_fire(FP_data,i,date_time)
        i = i+1   
        
    except ValueError as error:
        bad_files = []
        bad_files.append(x)

with open('bad_files', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(bad_files)

"""

file = files[1]
data = hdf_pull.read_in(file[0])
hdf_pull.list_sds(data)
FP_data = hdf_pull.FP_data_pull(data)
FRP_map_plot.plot_fire(FP_data) 
"""


