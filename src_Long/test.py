import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def H1_sin(t,*args):
	return cos((omega * t) + 0.5 * PI)

def H1_cos(t,*args):
	return cos(omega * t)

omega = 1

R = 1/sqrt(2) * (sigmax() + sigmay())

H0  = 15*sigmam()* sigmap()*0
H1s = 0 * (R*sigmam()*R + R*sigmap()*R)
H1c = 2 * (R*sigmam()*R + R*sigmap()*R)

H = [H0,[H1s,H1_sin],[H1c,H1_cos]]

psi0 = R*basis(2,0)

tlist = np.linspace(0,5,1000)

c_ops = [0.05*R*sigmam()*R,0.05*R*sigmaz()*R]

result = mesolve(H,psi0,tlist,c_ops,[sigmax(),sigmay(),sigmaz()])

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(tlist, np.real(result.expect[0]), 'r')
ax.plot(tlist, np.real(result.expect[1]), 'b')
ax.plot(tlist, -1 * np.real(result.expect[2]), 'g')
ax.legend(("sx", "sy", "sz"))
ax.set_xlabel('Time')
ax.set_ylabel('expectation value')

#plt.show()#

sphere=Bloch()
sphere.add_points([result.expect[0],result.expect[1],-1 *result.expect[2]], meth='l')
sphere.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
sphere.show()