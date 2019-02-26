import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def H1_cos(t,*args):
	return cos(omega * t)
def H1_rot1(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotpp(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotpm(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotmp(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotmm(t,*args):
	return (cos(omegad4 * t + 0.5*PI) + cos(omegad5*t + 0.5*PI) + 1*cos(omegad1*t + 0.5*0) + 1*cos(omegad2*t+ 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )


omega1    = 9
omega2   = 6
omega3   = 7
omegad1  = omega1 
omegad2  = omega2
omegad3  = omega3
omegad4  = omega1 + omega2
omegad5  = omega1 - omega2
omegad6  = omega1 + omega3
omegad7  = omega1 - omega3
omegad8  = omega2 + omega3
omegad9  = omega2 - omega3
omegad10 =  omega1 + omega2 + omega3
omegad11 =  omega1 + omega2 - omega3
omegad12 =  omega1 - omega2 + omega3
omegad13 = -omega1 + omega2 + omega3


R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

H0  = 0 * tensor(a,a,a)

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[q1*q2,H1_rotpp],[q1*q2.dag(),H1_rotpm],[q1.dag()*q2,H1_rotmp],[q1.dag()*q2.dag(),H1_rotmm]]

#psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
#psi0 = tensor(zero,zero,one)
#psi0 = tensor(zero,one,zero);Tdm = tensor(zero,one,zero)
#psi0 = tensor(zero,one,one)
#psi0 = tensor(one,zero,zero);Tdm = tensor(one,one,zero)
#psi0 = tensor(one,zero,one)
psi0 = tensor(one,one,zero);Tdm = tensor(one,zero,zero)
#psi0 = tensor(one,one,one)

tlist = np.linspace(0,4*PI,1000)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R)

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.002*sz1,0.002*sz2,0.002*sz3]

result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2,sx3,sy3,sz3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))

figX, axX = plt.subplots(figsize=(12,6))
axX.plot(tlist, np.real(result.expect[0]), 'r')
axX.plot(tlist, np.real(result.expect[3]), 'b')
axX.plot(tlist, np.real(result.expect[6]), 'g')
axX.legend(("sx1", "sx2", "sx3"))
axX.set_xlabel('Time')
axX.set_ylabel('SigmaX Expectation Value')
figX.savefig('Output/SigmaX.png')

figY, axY = plt.subplots(figsize=(12,6))
axY.plot(tlist, np.real(result.expect[1]), 'r')
axY.plot(tlist, np.real(result.expect[4]), 'b')
axY.plot(tlist, np.real(result.expect[7]), 'g')
axY.legend(("sy1", "sy2", "sy3"))
axY.set_xlabel('Time')
axY.set_ylabel('SigmaY Expectation Value')
figY.savefig('Output/SigmaY.png')

figZ, axZ = plt.subplots(figsize=(12,6))
axZ.plot(tlist, np.real(result.expect[2]), 'r')
axZ.plot(tlist, np.real(result.expect[5]), 'b')
axZ.plot(tlist, np.real(result.expect[8]), 'g')
axZ.legend(("sz1", "sz2", "sz3"))
axZ.set_xlabel('Time')
axZ.set_ylabel('SigmaZ Expectation Value')
figZ.savefig('Output/SigmaZ.png')

#plt.show()#

sphere=Bloch()
sphere.add_points([result.expect[0],result.expect[1],result.expect[2]], meth='l')
sphere.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
#phere.show()

sphere1=Bloch()
sphere1.add_points([result.expect[3],result.expect[4],result.expect[5]], meth='l')
sphere1.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
#sphere1.show()

sphere2=Bloch()
sphere2.add_points([result.expect[6],result.expect[7],result.expect[8]], meth='l')
sphere2.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
#sphere1.show()


fidelity_dat = []
for j in range(0,len(tlist)):
 		fidelity_dat.append(fidelity(result.states[j],Tdm))

with open('Output/fidelity11.dat','w') as f1:
	for j in fidelity_dat:
		f1.write(str(j) + "\n")
