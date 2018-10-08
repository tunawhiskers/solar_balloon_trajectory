import atmosphere
import numpy as np
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap

#test: draw worldwide orog
def test_wordwide_orog():
    lat_range = (-90, 90)
    lon_range = (0, 360)
    now = datetime.now()
    hr = 0
    date_hr = "%d%02d%02d%02d" % (now.year, now.month, now.day, hr)
    #atmosphere.atmosphere.download_file(lat_range, lon_range, date_hr, "file.anl")
    atm = atmosphere.atmosphere("file.anl")
    lon_range = np.linspace(atm.lon_min, atm.lon_max, atm.lon_max - atm.lon_min+1)
    lat_range = np.linspace(atm.lat_min, atm.lat_max, atm.lat_max - atm.lat_min+1)
    nx = len(lat_range)
    ny = len(lon_range)
    ground = np.zeros((nx,ny))
    for i in range(len(lat_range)):
        for j in range(len(lon_range)):
            ground[i][j] = atm.get_orog(lat_range[i], lon_range[j])
    fig, ax = plt.subplots(1,1)
    P = ax.pcolormesh(lon_range, lat_range, ground)
    m = Basemap(projection='cyl', llcrnrlat=-90,urcrnrlat=90,\
                llcrnrlon=0,urcrnrlon=360)
    m.drawcoastlines()
    fig.savefig("hello.png", dpi = 300)


#test: demonstrate that pressure, velocity temperpolation are valid
atm = atmosphere.atmosphere("file.anl")
lat = 34.0
lon = 180.-106
ground_h = atm.get_orog(lat, lon)
(i,j,k) = atm.get_bin(lat, lon, 1000)
# print (i,j,k)
# print(atm.h_ar[i,j,0])
# print(atm.u_ar[i,j,0])
# print(atm.u_ar[i,j,1])
# print(atm.u_ar[i,j,2])
# print(atm.u_ar[i,j,3])
# print(atm.g_ar[i,j])
print(atm.get_P(lat, lon, 100))
