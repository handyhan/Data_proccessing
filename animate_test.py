# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 16:30:04 2017

@author: Hannah.N
"""

import random
import os
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import animation
import pandas as pd
from IPython.display import HTML

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation




my_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
          lat_0=0, lon_0=-130)
my_map.drawcoastlines()
my_map.drawcountries()
my_map.fillcontinents(color = 'gray')
my_map.drawmapboundary()
my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

x,y = my_map(0, 0)
point = my_map.plot(x, y, 'ro', markersize=5)[0]

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
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                               frames=20, interval=500, blit=True)

plt.show()

"""
FRAMES = 20
POINTS_PER_FRAME = 30
LAT_MIN = 40.5
LAT_MAX = 40.95
LON_MIN = -74.15
LON_MAX = -73.85
FIGSIZE = (10,10)
MAP_BACKGROUND = '.95'
MARKERSIZE =     


class AnimatedMap(object):
     #An animated scatter plot over a basemap
    def __init__(self, data_frames):
        self.dfs = data_frames
        self.fig = plt.figure(figsize=FIGSIZE)
        self.event_map = Basemap(projection='merc', 
                resolution='i', area_thresh=1.0, # Medium resolution
                lat_0 = (LAT_MIN + LAT_MAX)/2, lon_0=(LON_MIN + LON_MAX)/2, # Map center 
                llcrnrlon=LON_MIN, llcrnrlat=LAT_MIN, # Lower left corner
                urcrnrlon=LON_MAX, urcrnrlat=LAT_MAX) # Upper right corner 
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=FRAMES, interval=1000, 
                                           init_func=self.setup_plot, blit=True,
                                           repeat=False)

    def setup_plot(self):
        self.event_map.drawcoastlines() 
        self.event_map.drawcounties()
        self.event_map.fillcontinents(color=MAP_BACKGROUND) # Light gray
        self.event_map.drawmapboundary()
        self.scat = self.event_map.scatter(x = [], y=[], s=MARKERSIZE,marker='o', zorder=10) 
        return self.scat

    def project_lat_lons(self, i):
        df = data_frames[i]
        x, y = self.event_map(df.lon.values, df.lat.values)
        x_y = pd.DataFrame({'x': x, 'y': y}, index=df.index)
        df = df.join(x_y)
        return df

    def update(self, i):
       #Update the scatter plot.
        df = self.project_lat_lons(i)
        new_offsets = np.vstack([df.x.values, df.y.values]).T
        self.scat.set_offsets(new_offsets)
        return self.scat,


s = AnimatedMap(data_frames)
s.ani"""