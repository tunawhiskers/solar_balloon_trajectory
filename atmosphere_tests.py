import atmosphere
import numpy as np
import matplotlib.pyplot as plt

atm = atmosphere.atmosphere("file.anl")

for i in np.linspace(atm.lat_min, atm.lat_max, atm.lat_max - atm.lat_min):
    for j in np.linspace(atm.lon_min, atm.lon_max, atm.lon_max - atm.lon_min):
        print(i,j, atm.get_orog(i,j))

#plt.figure()
#m.pcolormesh(x,y,t_data[10],shading='flat',cmap=plt.cm.jet)
#m.colorbar(location='right')
#m.drawcoastlines()
##m.fillcontinents()
#m.drawmapboundary()
#m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
#m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
#plt.rcParams["figure.figsize"] = [20,15]
#plt.show()
