import matplotlib.pyplot as plt
import numpy as np


file = "Max_occupation_12A.dat"

fileI = np.loadtxt(file,usecols=[0],dtype=np.float32)
fileJ = np.loadtxt(file,usecols=[1],dtype=np.float32)
file1 = np.loadtxt(file,usecols=[2],dtype=np.float32)
file2 = np.loadtxt(file,usecols=[3],dtype=np.float32)
fileA = np.loadtxt(file,usecols=[4],dtype=np.float32)

print(file2)

x = np.unique(fileI)
y = np.unique(fileJ)

X,Y = np.meshgrid(x,y)

Z1=file1.reshape(len(x),len(y))
Z2=file2.reshape(len(x),len(y))
ZA=fileA.reshape(len(x),len(y))

fig,ax = plt.subplots()

im=ax.pcolormesh(X,Y,Z1)
fig.colorbar(im,orientation='horizontal')
plt.savefig("Phase_diagram1.png")

#plt.clf()

im=ax.pcolormesh(X,Y,Z2)
#fig.colorbar(im,orientation='horizontal')
plt.savefig("Phase_diagram2.png")

#plt.clf()

im=ax.pcolormesh(X,Y,ZA)
#fig.colorbar(im,orientation='horizontal')
plt.savefig("Phase_diagramA.png")


