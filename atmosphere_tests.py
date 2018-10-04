import atmosphere
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

atm = atmosphere.atmosphere("file.anl")

lon_range = np.linspace(atm.lon_min+1, atm.lon_max-1, atm.lon_max - atm.lon_min)
lat_range = np.linspace(atm.lat_min+1, atm.lat_max-1, atm.lat_max - atm.lat_min)

nx = len(lat_range)
ny = len(lon_range)

ground = np.zeros((nx,ny))


for i in range(len(lat_range)):
    for j in range(len(lon_range)):
        ground[i][j] = atm.get_orog(lat_range[i], lon_range[j])


fig, ax = plt.subplots(1,1)

print(ground)
#plt.figure()
P = ax.pcolormesh(lon_range, lat_range, ground)
fig.savefig("hello.png")
#plt.pcolormesh(x,y,t_data[10],shading='flat',cmap=plt.cm.jet)
#m.colorbar(location='right')
#m.drawcoastlines()
##m.fillcontinents()
#m.drawmapboundary()
#m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
#plt.rcParams["figure.figsize"] = [20,15]
#plt.show()
