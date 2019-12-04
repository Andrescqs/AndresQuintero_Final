import numpy as np
import matplotlib.pylab as plt



datos = np.loadtxt("monthrg.dat")
dat=[]

for i in range(len(datos)):
	if(datos[i][3]==-99):
		datos[i][3]=0
	if(datos[i][0] >= 1900):
		dat.append(datos[i][:4])
	
		
datarr = np.array(dat)
	

y = np.fft.fft(datarr[:][3])
x = datarr[:][2]

plt.figure()
plt.plot(x, np.real(y))
plt.xlabel("t")
plt.ylabel("# Manchas")
plt.savefig("solar.png")

