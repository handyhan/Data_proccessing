# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 11:48:21 2017

@author: Hannah.N
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon

def plot_fire():
    # FP_data is a array with lat,long,FRP and Confidane
    
    
    # llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
    # are the lat/lon values of the lower left and upper right corners
    # of the map.
    # resolution = 'i' means use intermediate resolution coastlines.
    # lon_0, lat_0 are the central longitude and latitude of the projection.
    m = Basemap(llcrnrlon=100,llcrnrlat=-40,urcrnrlon=160,urcrnrlat=-5,
                resolution='i',projection='tmerc',lon_0=130,lat_0=-20)
                
    m.drawcoastlines()
    m.drawmapboundary()#(color='lightgray',fill_color='aqua')
    m.fillcontinents(lake_color='aqua',zorder=0)
    # draw parallels and meridians.
    
    m.drawparallels(np.arange(-40,61.,5.0), labels = [True])
    m.drawmeridians(np.arange(100.,180.,10.0), labels = [1,1,1,1])
    #m.drawmapboundary(fill_color='aqua')
    #FRP.max()
    #x, y = m(longitude, latitude)
    #m.scatter(x, y, c=FRP, s = 150, marker ='^', zorder=10,norm=mpl.colors.SymLogNorm(linthresh=10, vmin=0, vmax=(1000)))
    m.shadedrelief()
    #cb = m.colorbar()
    #cb.set_ticks([0,10,100,500,1000])
    #plt.title(date_time)
    x1,y1 = m(120,-11)
    x2,y2 = m(146,-11)
    x3,y3 = m(146,-22)
    x4,y4 = m(120,-22)
    poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='none',edgecolor='red',linewidth=3)
    plt.gca().add_patch(poly)
    plt.show()
    plt.savefig('C:\Users\Hannah.N\Dropbox\PhD\Writting\Jan-July(17)\sitemap.png')
    #plt.close()

plot_fire()