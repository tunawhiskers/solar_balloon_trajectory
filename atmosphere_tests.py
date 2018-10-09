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
#print(ground_h)
(i,j,k) = atm.get_bin(lat, lon, ground_h+2000)

h1 = atm.h_ar[i,j,k]
h2 = atm.h_ar[i,j,k+1]
h3 = atm.h_ar[i,j,k+2]

print(80*'-')
print("z test")
print("binned values:")
print("%f %f %f" % (atm.u_ar[i,j,k], atm.u_ar[i,j,k+1], atm.u_ar[i,j,k+2]))
print("interp values:")
print("%f %f %f" % (atm.get_u(i-90,j,h1), atm.get_u(i-90,j,h2), atm.get_u(i-90,j,h3)))
print(80*'-')

fig, ax = plt.subplots(1,1)
discrete_x = [atm.h_ar[i,j,k], atm.h_ar[i,j,k+1], atm.h_ar[i,j,k+2]]
discrete_u = [atm.u_ar[i,j,k], atm.u_ar[i,j,k+1], atm.u_ar[i,j,k+2]]
cont_x = np.linspace(h1, h3, 50)
cont_u = np.zeros_like(cont_x)
for (m,x) in enumerate(cont_x):
    cont_u[m] = atm.get_u(i-90, j, x)
ax.plot(discrete_x, discrete_u, ".")
ax.plot(cont_x, cont_u)
ax.set_ylabel("u (m/s)")
ax.set_xlabel("h (m)")
ax.grid()
fig.savefig("u_h_interp.png", dpi = 300)
fig.clf()

h1 = atm.h_ar[i,j,k]
h2 = atm.h_ar[i+1,j,k]
h3 = atm.h_ar[i+2,j,k]
print(80*'-')
print("Lat test")
print("binned values:")
print("%f %f %f" % (atm.u_ar[i,j,k], atm.u_ar[i+1,j,k], atm.u_ar[i+2,j,k]))
print("interp values:")
print("%f %f %f" % (atm.get_u(i-90,j,h1), atm.get_u(i-90+1,j,h2), atm.get_u(i-90+2,j,h3)))
print(80*'-')

fig, ax = plt.subplots(1,1)
discrete_u = [atm.u_ar[i,j,k], atm.u_ar[i+1,j,k], atm.u_ar[i+2,j,k]]
discrete_x = [i,i+1,i+2]

cont_x = np.linspace(i,i+2, 50)
cont_u = np.zeros_like(cont_x)

for (m,x) in enumerate(cont_x):
    if(x < i+1):
        dh = atm.h_ar[i+1,j,k] - atm.h_ar[i,j,k]
        height = dh*(x-i) + atm.h_ar[i,j,k]        
    else:
        dh = atm.h_ar[i+2,j,k] - atm.h_ar[i+1,j,k]
        height = dh*(x-i-1) + atm.h_ar[i+1,j,k]
    cont_x[m] = x
    cont_u[m] = atm.get_u(x-90, j, height)

ax.plot(discrete_x, discrete_u, ".")
ax.plot(cont_x, cont_u)
ax.set_ylabel("u (m/s)")
ax.set_xlabel("lat (deg)")
ax.grid()
fig.savefig("u_lat_interp.png", dpi = 300)
fig.clf()


print(80*'-')
h1 = atm.h_ar[i,j,k]
h2 = atm.h_ar[i,j+1,k]
h3 = atm.h_ar[i,j+2,k]
print("Lon test")
print("binned values:")
print("%f %f %f" % (atm.u_ar[i,j,k], atm.u_ar[i,j+1,k], atm.u_ar[i,j+2,k]))
print("interp values:")
print("%f %f %f" % (atm.get_u(i-90,j,h1), atm.get_u(i-90,j+1,h2), atm.get_u(i-90,j+2,h3)))
print(80*'-')


fig, ax = plt.subplots(1,1)
discrete_u = [atm.u_ar[i,j,k], atm.u_ar[i,j+1,k], atm.u_ar[i,j+1,k]]
discrete_x = [j,j+1,j+2]

cont_x = np.linspace(j,j+2, 50)
cont_u = np.zeros_like(cont_x)

for (m,x) in enumerate(cont_x):
    if(x < j+1):
        dh = atm.h_ar[i,j+1,k] - atm.h_ar[i,j,k]
        height = dh*(x-j) + atm.h_ar[i,j,k]
        print(height)
    else:
        dh = atm.h_ar[i,j+2,k] - atm.h_ar[i,j+1,k]
        height = dh*(x-j-1) + atm.h_ar[i,j+1,k]
    cont_x[m] = x
    cont_u[m] = atm.get_u(i, x, height)

ax.plot(discrete_x, discrete_u, ".")
ax.plot(cont_x, cont_u)
ax.set_ylabel("u (m/s)")
ax.set_xlabel("lon (deg)")
ax.grid()
fig.savefig("u_lon_interp.png", dpi = 300)
fig.clf()





# print (i,j,k)
# print(atm.h_ar[i,j,0])
# print(atm.u_ar[i,j,0])
# print(atm.u_ar[i,j,1])
# print(atm.u_ar[i,j,2])
# print(atm.u_ar[i,j,3])
# print(atm.g_ar[i,j])
#print(atm.get_P(lat, lon, 100))
