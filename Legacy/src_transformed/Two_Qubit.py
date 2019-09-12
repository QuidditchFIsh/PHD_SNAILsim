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


omega1 = 10
omega2 = 23
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

g = 0.05

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[g * q1*q2,H1_rotpp],[g * q1*q2.dag(),H1_rotpm],[g * q1.dag()*q2,H1_rotmp],[g * q1.dag()*q2.dag(),H1_rotmm]]

tlist = np.linspace(0,2**9,2**10)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R)

c_ops = [0.001*q1,0.001*q2,0.002*sz1,0.002*sz2]

freqs = np.genfromtxt('Frequencies2')

start = time.time()
Max_minFid = []
for j in freqs:
	print(j)
	for i in range(0,4):
		omega1 = j[0]
		omega2 = j[1]
		omegad1 = omega1 + omega2
		omegad2 = omega1 - omega2
		omegad3 = omega1
		omegad4 = omega2
		if i == 0:
			psi0 = tensor(zero,zero);Tdm = tensor(zero,zero)
			outputstr = 'Output/CNOT_18-03-19/fidelity00-' + str(omega1) + '_' + str(omega2) + '.dat'
			#print('1')
		if i == 1:
			psi0 = tensor(zero,one);Tdm = tensor(zero,one)
			outputstr = 'Output/CNOT_18-03-19/fidelity10-' + str(omega1) + '_' + str(omega2) + '.dat'
			#print('2')
		if i == 2:
			psi0 = tensor(one,zero);Tdm = tensor(one,one)
			outputstr = 'Output/CNOT_18-03-19/fidelity01-' + str(omega1) + '_' + str(omega2) + '.dat'
			#print('3')
		if i == 3:
			psi0 = tensor(one,one);Tdm = tensor(one,zero)
			outputstr = 'Output/CNOT_18-03-19/fidelity11-' + str(omega1) + '_' + str(omega2) + '.dat'
			#print('4')

		result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


		fidelity_dat = []
		for k in range(0,len(tlist)):
		 		fidelity_dat.append(fidelity(result.states[k],Tdm))

		with open(outputstr,'w') as f1:
			for k in fidelity_dat:
				f1.write(str(k) + "\n")


	x11 = np.genfromtxt('Output/CNOT_18-03-19/fidelity11-' + str(omega1) + '_' + str(omega2) + '.dat')
	x10 = np.genfromtxt('Output/CNOT_18-03-19/fidelity10-' + str(omega1) + '_' + str(omega2) + '.dat')
	x01 = np.genfromtxt('Output/CNOT_18-03-19/fidelity01-' + str(omega1) + '_' + str(omega2) + '.dat')
	x00 = np.genfromtxt('Output/CNOT_18-03-19/fidelity00-' + str(omega1) + '_' + str(omega2) + '.dat')


	tmp = []
	Min = []

	for k in range(0,len(x11)):
		tmp.append(x11[k])
		tmp.append(x10[k])
		tmp.append(x01[k])
		tmp.append(x00[k])
		Min.append(min(tmp))
		tmp = []
	#print('Fidelity Achieved:' + str(max(Min)))
	Max_minFid.append(max(Min))

	outputstr = 'Output/CNOT_18-03-19/Minimum-' + str(omega1) + '_' + str(omega2) + '.dat'

	with open(outputstr,'w') as f2:
		for k in Min:
			f2.write(str(k) + "\n")

end = time.time()
print('Time Taken for Simulation:')
print(end - start)

outputstr = 'Output/CNOT_18-03-19/__Max_Fidelity__.dat'

with open(outputstr,'w') as f3:
	for k in Max_minFid:
		f3.write(str(k) + "\n")

