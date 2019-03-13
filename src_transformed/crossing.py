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


#PBS -S /bin/sh
#PBS -V
#
#PBS -N Testing-Nye
#
#PBS -q short
#
#PBS -j oe
#
#PBS -M ajb17@hw.ac.uk
#PBS -m abe
#PBS -e /home/ajb17/Storage/Toffoli/src_transformed/Output/Toffoli_13-02-19
#PBS -o /home/ajb17/Storage/Toffoli/src_transformed/Output/Toffoli_13-02-19
# RESOURCE REQUEST
#PBS -l nodes=1:ppn=1:qutip
#PBS -l walltime=00:01:00

cd /home/ajb17/Storage/Toffoli/src_transformed
python Three_Qubit.py
