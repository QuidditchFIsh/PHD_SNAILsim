import numpy as np
import matplotlib.pyplot as plt



x = np.genfromtxt("Output/Toffoli_13-02-19/fidelity000.dat")
f = np.genfromtxt("Output/Toffoli_13-02-19/fidelity000.dat")
g = np.genfromtxt("Output/Toffoli_13-02-19/fidelity110.dat")
#print(len(x))
#plt.plot(x, '-')
#plt.plot(g, '-')

idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
print(idx)
print(max(f[idx]))
#plt.plot(x,'-gD',markevery=idx)
#plt.plot(g,'-')
#plt.plot(g[idx], 'ro')
#plt.show()

#data = np.genfromtxt("../Output/Toffoli_13-02-19/fidelity000.dat")
