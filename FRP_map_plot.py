import hdf_pull 
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



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
    m = Basemap(llcrnrlon=120,llcrnrlat=-20,urcrnrlon=140,urcrnrlat=-10,
                resolution='i',projection='tmerc',lon_0=130,lat_0=-15)
                
    m.drawcoastlines()
    #m.fillcontinents(color='coral',lake_color='aqua')
    # draw parallels and meridians.
    
    m.drawparallels(np.arange(-40,61.,2.), labels = [True])
    m.drawmeridians(np.arange(100.,140.,2.), labels = [True])
    #m.drawmapboundary(fill_color='aqua')
    #FRP.max()
    x, y = m(longitude, latitude)
    m.scatter(x, y, c=FRP, norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=((FRP.max())+20)))
    plt.show()
 
#plot_fire()