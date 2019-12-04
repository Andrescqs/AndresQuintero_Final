import numpy as np
import matplotlib.pyplot as plt


def gauss(x, sigma):
    return np.exp(-x**2/(2.0*sigma**2))/np.sqrt(2.0*np.pi*sigma**2)


def metropolis(sigma, N, delta=1.0):
    listarr = np.loadtxt("valores.txt")
    lista = listarr.tolist()

    for i in range(1,N):
        propuesta  = lista[i-1] + (np.random.random()-0.5)*delta
        r = min(1, gauss(propuesta, sigma)/gauss(lista[i-1], sigma))
        alpha = np.random.random()
        if(alpha<r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
    return np.array(lista)


plt.figure()

N=100000
sigma=1.0
x = metropolis(sigma, N)

xideal = np.linspace(x.min(), x.max(), N)
yideal = gauss(xideal, sigma)

media = x.mean()
mediastr = str(media)
desv = str(x.std())

_ = plt.hist(x, bins=30, density=True, label='Metropolis-Hastings')
plt.plot(xideal, yideal, label='Ideal')
plt.title("$\\barx=$" + mediastr +"," + " $\\sigma=$" + desv)
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("sigma.png")



