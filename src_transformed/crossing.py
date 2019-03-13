import numpy as np
import matplotlib.pyplot as plt



x = np.genfromtxt("../Output/Toffoli_13-02-19/fidelity000.dat")
f = np.genfromtxt("../Output/Toffoli_13-02-19/fidelity000.dat")
g = np.genfromtxt("../Output/Toffoli_13-02-19/fidelity111.dat")

plt.plot(x, '-')
#plt.plot(x, g, '-')

idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
plt.plot(g[idx], 'ro')
plt.show()

#data = np.genfromtxt("../Output/Toffoli_13-02-19/fidelity000.dat")
