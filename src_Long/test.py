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
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotpp(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotpm(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rotmp(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rotmm(t,*args):
	return 0.5*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*PI) + 1*cos(omegad4*t+ 0.5*0))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )


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

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[0.01*q1*q2,H1_rotpp],[0.01*q1*q2.dag(),H1_rotpm],[0.01*q1.dag()*q2,H1_rotmp],[0.01*q1.dag()*q2.dag(),H1_rotmm]]

#psi0 = tensor(zero,zero);Tdm = tensor(zero,zero)
psi0 = tensor(zero,one);Tdm = tensor(zero,one)
#psi0 = tensor(one,zero);Tdm = tensor(one,one)
#psi0 = tensor(one,one);Tdm = tensor(one,zero)

tlist = np.linspace(0,200*PI,1000)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R)

c_ops = [0.001*q1,0.001*q2,0.002*sy1,0.002*sy2]

outstr = ''
for i in range(0,4):
	if i == 0:
		psi0 = tensor(zero,zero);Tdm = tensor(zero,zero)
		outstr = '../Output/testing/fidelity00.dat'
	if i == 1:
		psi0 = tensor(zero,one);Tdm = tensor(zero,one)
		outstr = '../Output/testing/fidelity01.dat'
	if i == 2:
		psi0 = tensor(one,zero);Tdm = tensor(one,one)
		outstr = '../Output/testing/fidelity10.dat'		
	if i == 3:
		psi0 = tensor(one,one);Tdm = tensor(one,zero)
		outstr = '../Output/testing/fidelity11.dat'		

	result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2],options = Options(nsteps = 8000,store_states = True,store_final_state = True))

	fidelity_dat = []
	for j in range(0,len(tlist)):
	 		fidelity_dat.append(fidelity(result.states[j],Tdm))

	with open(outstr,'w') as f1:
		for j in fidelity_dat:
			f1.write(str(j) + "\n")
