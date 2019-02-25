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
def H1_rot1(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return cos(omegad * t)*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return cos(omegad * t)*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotpp(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotpm(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotmp(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotmm(t,*args):
	return cos(omegad * t)*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

omegad = 10
omega1 = 10
omega2 = 15

R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

print(R * sigmay() * R)

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2))
q2 = tensor(qeye(2),a)

H0  = 0 * tensor(a,a)

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[0.5*q1*q2,H1_rotpp],[0.5*q1*q2.dag(),H1_rotpm],[0.5*q1.dag()*q2,H1_rotmp],[0.5*q1.dag()*q2.dag(),H1_rotmm]]

psi0 = tensor(zero,one)

tlist = np.linspace(0,10,1000)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R)

c_ops = [0.01*q1,0.01*q2,0.02*sz1,0.02*sz2]

result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2])

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