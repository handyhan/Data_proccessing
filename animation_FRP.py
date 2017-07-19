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

file = 'J:\PhD\earth_observation\Data\Oct_2015\H8_20151014_20151029_177_129.csv'

data = pd.DataFrame.from_csv(file)
data = data.dropna()
start = data.index.searchsorted(datetime.datetime(2015, 10, 14, 12 ,0))
end = data.index.searchsorted(datetime.datetime(2015, 10, 14,12,20))
data = data.ix[start:end]
print data.shape

def plot_map(lons, lats, FRP, llcrnrlon=128,llcrnrlat=-18.5,urcrnrlon=132,urcrnrlat=-16.5,
                resolution='i',projection='tmerc', s = 150, marker ='^',lon_0=129.5,lat_0=-17.6, min_marker_size=2):
    
    bins = np.linspace(0, FRP.max(), 10)
    colour = np.digitize(FRP, bins) + min_marker_size
    print colour
    #print colour

    m = Basemap(projection=projection, llcrnrlat=llcrnrlat, urcrnrlat=urcrnrlat, llcrnrlon=llcrnrlon, urcrnrlon=urcrnrlon, resolution=resolution,lon_0=lon_0,lat_0=lat_0)
    m.drawcoastlines()
    m.drawmapboundary()
    #m.fillcontinents(lake_color='aqua', zorder = 0)
    m.shadedrelief()

    for lon, lat, FRP in zip(lons, lats, colour):
        #print lons.shape, FRP.shape
        x, y = m(lons, lats)
        #print lons.shape, FRP.shape
        m.scatter(x, y, c=colour, s = 150, marker ='^', zorder=10)#norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=(500)) )#norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=50)) #c=np.abs(FRP),
        cb = m.colorbar()
        #cb.set_ticks([0,10,100,500,1000])

    return m


plt.figure()
plot_map(data['LONGITUDE'].values, data['LATITUDE'].values, data['FRP_0'].values)
plt.show()
#plt.savefig('C:\Users\Hannah.N\Documents\Data\test.png')





"""
m = Basemap(llcrnrlon=128,llcrnrlat=-18.5,urcrnrlon=132,urcrnrlat=-16,
                resolution='i',projection='tmerc',lon_0=129.5,lat_0=-17.6)
                
m.drawcoastlines()
m.drawmapboundary()#(color='lightgray',fill_color='aqua')
m.fillcontinents(lake_color='aqua',zorder=0)


# draw parallels and meridians.  
m.drawparallels(np.arange(-40,61.,0.5), labels = [True])
m.drawmeridians(np.arange(100.,140.,0.5), labels = [128,129,130,131])

#m.drawmapboundary(fill_color='aqua')


x, y = m(lat[0:100],longi[0:100])
m.scatter(x, y, c=np.abs(FRP[0:100]), s = 150, marker ='^', zorder=10, norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=(1000)))
#m.shadedrelief()
cb = m.colorbar()
cb.set_ticks([0,10,100,500,1000])
plt.title(data['datetime'])

plt.show()
x,y = my_map(0, 0)
point = m.plot(x, y, 'ro', markersize=5)[0]

def init():
    point.set_data([], [])
    return point,

# animation function.  This is called sequentially
def animate(i):
    lons, lats =  np.random.random_integers(-130, 130, 2)
    x, y = my_map(lons, lats)
    point.set_data(x, y)
    return point,

# call the animator.  blit=True means only re-draw the parts that have changed.
#anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               #frames=20, interval=500, blit=True)

#plt.show()"""