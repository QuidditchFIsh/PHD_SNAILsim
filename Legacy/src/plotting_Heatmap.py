import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('../Output/RF/RF_QuBit_AmpVSPhiBar_1.txt',delimiter=' ')

x=data[:,0]
y=data[:,1]
z=data[:,2]

x=np.unique(x)
y=np.unique(y)
X,Y = np.meshgrid(x,y)
Z=z.reshape(len(y),len(x))

plt.pcolormesh(X,Y,Z)

plt.show()