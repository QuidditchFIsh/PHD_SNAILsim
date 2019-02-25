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
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotpp(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotpm(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotmp(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotmm(t,*args):
	return (cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )


omega1 = 11
omega2 = 19
omegad1 = omega1 + omega2
omegad2 = omega1 - omega2
omegad3 = omega1
omegad4 = omega2

R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2))
q2 = tensor(qeye(2),a)

H0  = 0 * tensor(a,a)

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[q1*q2,H1_rotpp],[q1*q2.dag(),H1_rotpm],[q1.dag()*q2,H1_rotmp],[q1.dag()*q2.dag(),H1_rotmm]]

#psi0 = tensor(zero,zero);Tdm = tensor(zero,zero)
#psi0 = tensor(zero,one);Tdm = tensor(zero,one)
#psi0 = tensor(one,zero);Tdm = tensor(one,one)
psi0 = tensor(one,one);Tdm = tensor(one,zero)

tlist = np.linspace(0,4*PI,1000)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R)

c_ops = [0.001*q1,0.001*q2,0.002*sz1,0.002*sz2]

result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2],options = Options(nsteps = 8000,store_states = True,store_final_state = True))

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(tlist, np.real(result.expect[0]), 'r')
ax.plot(tlist, np.real(result.expect[3]), 'b')
ax.legend(("sx1", "sx2"))
ax.set_xlabel('Time')
ax.set_ylabel('expectation value')

#plt.show()#

sphere=Bloch()
sphere.add_points([result.expect[0],result.expect[1],result.expect[2]], meth='l')
sphere.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
#phere.show()

fig1, ax1= plt.subplots(figsize=(12,6))
ax1.plot(tlist, np.real(result.expect[1]), 'r')
ax1.plot(tlist, np.real(result.expect[4]), 'b')
ax1.legend(("sy1", "sy2"))
ax1.set_xlabel('Time')
ax1.set_ylabel('expectation value')

fig2, ax2 = plt.subplots(figsize=(12,6))
ax2.plot(tlist, np.real(result.expect[2]), 'r')
ax2.plot(tlist, np.real(result.expect[5]), 'b')
ax2.legend(("sz1", "sz2"))
ax2.set_xlabel('Time')
ax2.set_ylabel('expectation value')

#plt.show()

sphere1=Bloch()
sphere1.add_points([result.expect[3],result.expect[4],result.expect[5]], meth='l')
sphere1.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
#sphere1.show()


fidelity_dat = []
for j in range(0,len(tlist)):
 		fidelity_dat.append(fidelity(result.states[j],Tdm))

with open('../Output/testing/fidelity11.dat','w') as f1:
	for j in fidelity_dat:
		f1.write(str(j) + "\n")
