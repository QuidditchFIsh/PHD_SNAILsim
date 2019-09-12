from qutip import *
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np



R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = R * basis(2,1)
zero = R * basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

q1_before = tensor(sigmap(), qeye(2),qeye(2))
q2_before = tensor(qeye(2),sigmap(),qeye(2))
q3_before = tensor(qeye(2),qeye(2),sigmap())

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(2),qeye(2),qeye(2))


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,10,num=1000)
#R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R)

#H2 = EJ *(I - s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
H = 0.25*(I - sy1)*(I - sy2)*(I + sx3)

# visualize H

#lbls_list = [[str(d) for d in range(N)], ["u", "d"]]

#xlabels = []

#for inds in tomography._index_permutations([len(lbls) for lbls in lbls_list]):
#	xlabels.append("".join([lbls_list[k][inds[k]] for k in range(len(lbls_list))]))
   

fig, ax = matrix_histogram(H)

ax.view_init(azim=-55, elev=45)

plt.show()