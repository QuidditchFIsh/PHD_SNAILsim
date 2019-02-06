import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
import datetime
import os

def H1_Coeff_On(t,*args):
	return cos((w1 + w2) * t)

w1 = 1.0 * 2 * pi
w2 = 3.0 * 2 * pi
w3 = 6.0 * 2 * pi

g = 0.5 * 2 * pi

tlist = np.linspace(0,5,1001)

#inital state 
psi0 = tensor(basis(2,0),basis(2,0),basis(2,1))

#operators
a = tensor(destroy(2),qeye(2),qeye(2))
b = tensor(qeye(2),destroy(2),qeye(2))
c = tensor(qeye(2),qeye(2),destroy(2))

sz1 = tensor(sigmaz(),qeye(2),qeye(2))
sz2 = tensor(qeye(2),sigmaz(),qeye(2))
sz3 = tensor(qeye(2),qeye(2),sigmaz())

H0 = w1 * a.dag() * a + w2 * b.dag() * b + w3 * c.dag() * c + 0.2 * w1 * a.dag() * a.dag() * a * a + 0.5 * w2 * b.dag() * b.dag() * b * b + 0.6 * w3 * c.dag() * c.dag() * c * c
H1 = g * (a.dag()*b + a.dag() * c + b.dag()*c + a * b.dag() + a * c.dag() + b * c.dag())

H = [H0,[H1,H1_Coeff_On]]

c_ops = [0.01*a,0.01*b,c]

output = mesolve(H,psi0,tlist,c_ops,[a.dag() * a,b.dag() * b,c.dag() * c,sz1,sz2,sz3])

n_a = output.expect[0]
n_b = output.expect[1]
n_c = output.expect[2]

fig, axes = plt.subplots(1, 1, figsize=(10,6))

axes.plot(tlist, n_a, label="a")
axes.plot(tlist, n_b, label="b")
axes.plot(tlist, n_c, label="c")
axes.legend(loc=0)
axes.set_xlabel('Time')
axes.set_ylabel('Occupation probability')
axes.set_title('Test 3 qubit oscillations')

plt.show()
'''



wc = 1.0  * 2 * pi  # cavity frequency
wa = 1.0  * 2 * pi  # atom frequency
wb = 1.0  * 2 * pi  # atom frequency
g  = 0.05 * 2 * pi  # coupling strength
kappa = 0.005       # cavity dissipation rate
gamma = 0.05        # atom dissipation rate
N = 2              # number of cavity fock states
n_th_a = 0.0        # avg number of thermal bath excitation
use_rwa = False

tlist = np.linspace(0,10,101)

# intial state
psi0 = tensor(basis(2,0),basis(2,1))    # start with an excited atom

# operators
a  = tensor(destroy(2),qeye(2))
sm = tensor(qeye(2), destroy(2))
sn = tensor(qeye(2),qeye(2), destroy(2))

# Hamiltonian
if use_rwa:
    H = wc * a.dag() * a + wa * sm.dag() * sm + g * (a.dag() * sm + a * sm.dag())
else:
    H = wc * a.dag() * a + wa * sm.dag() * sm + g * (a.dag() + a) * (sm + sm.dag())



c_ops = []

# cavity relaxation
rate = kappa * (1 + n_th_a)
if rate > 0.0:
    c_ops.append(sqrt(rate) * a)

# cavity excitation, if temperature > 0
rate = kappa * n_th_a
if rate > 0.0:
    c_ops.append(sqrt(rate) * a.dag())

# qubit relaxation
rate = gamma
if rate > 0.0:
    c_ops.append(sqrt(rate) * sm)

output = mesolve(H, psi0, tlist, c_ops, [a.dag() * a, sm.dag() * sm])

n_c = output.expect[0]
n_a = output.expect[1]
#n_b = output.expect[2]

fig, axes = plt.subplots(1, 1, figsize=(10,6))

axes.plot(tlist, n_c, label="Cavity")
axes.plot(tlist, n_a, label="Atom excited state")
#axes.plot(tlist,n_b)
axes.legend(loc=0)
axes.set_xlabel('Time')
axes.set_ylabel('Occupation probability')
axes.set_title('Vacuum Rabi oscillations')

plt.show()
'''