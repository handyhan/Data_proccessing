import hdf_pull 
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


files = hdf_pull.file_path("\Terra")
"""plotting frp with frp intensity colour for single hdf file"""
def plot_fire(FP_data):
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
    m.scatter(x, y, c=FRP, s = 100, marker ='^', zorder=10,norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=((FRP.max())+20)))
    m.shadedrelief()
    cb = m.colorbar()
    cb.set_ticks([0,10,100,400])
    plt.show()
 
file = files[25]
print file
file = hdf_pull.read_in(file[0])

FP_data = hdf_pull.FP_data_pull(file)
#FRP_map_plot.plot_fire(FP_data) 
plot_fire(FP_data)