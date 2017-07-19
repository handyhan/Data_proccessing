# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 10:58:05 2017

@author: Hannah.N
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.animation as animation
import pandas as pd
import datetime

file = 'J:\PhD\earth_observation\Data\Oct_2015\MODIS_20151014_20151029_177_129.csv'

data = pd.DataFrame.from_csv(file)


data = data.dropna()
start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 12 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 14,23,59))
data = data.ix[start:end]
#print data['datetime']
#reformat datetime
#data['datetime'] = data['datetime'].astype(str)
#data['datetime'] = pd.to_datetime(data['datetime'],format='%Y-%m-%d %H:%M:%S')
#a = (data.ix[-1:]['datetime']-data.ix[0]['datetime'])
#FRAMES = (a[0].seconds//60)//10
#print FRAMES

def plot_map(lons, lats, FRPs, llcrnrlon=129,llcrnrlat=-18.5,urcrnrlon=132,urcrnrlat=-17,
                resolution='i',projection='tmerc', s = 150, marker ='^',lon_0=129.5,lat_0=-17.6, min_marker_size=2):
    
    #bins = np.linspace(0, FRP.max(), 10)
    #colour = np.digitize(FRP, bins) + min_marker_size
    #print colour
    #print colour

    m = Basemap(projection=projection, llcrnrlat=llcrnrlat, urcrnrlat=urcrnrlat, llcrnrlon=llcrnrlon, urcrnrlon=urcrnrlon, resolution=resolution,lon_0=lon_0,lat_0=lat_0)
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawparallels(np.arange(-40,61.,0.5), labels = [1,0,0,0])
    m.drawmeridians(np.arange(100.,140.,0.5), labels = [0,0,1,0])
    m.fillcontinents(lake_color='aqua', zorder = 0)
    m.shadedrelief()

    

    for lon, lat, FRP in zip(lons, lats, FRPs):
        
        x, y = m(lons, lats)
        #print lons.shape, FRP.shape
        m.scatter(x, y, c=FRPs, s = 300, marker ='^', zorder=10, alpha = 0.4, norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=(500)), cmap=plt.get_cmap('hot_r') )#norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=50)) #c=np.abs(FRP),
        cb = m.colorbar()
        cb.set_ticks([0,10,100,500,1000])
        
        
    return point

plt.figure()
plot_map(data['LONGITUDE'].values, data['LATITUDE'].values, data['FRP_0'].values)
#plt.savefig('C:\Users\Hannah.N\Documents\Data\test.png')
plt.show()
