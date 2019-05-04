import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
import datetime
import os
from Constants import *

def H1_rot1(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot1d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot2(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot2d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot3(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot3d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot12_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot13_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot23_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))


def H1_rot_123_ppp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_ppm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_pmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_pmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_mpp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_mpm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_mmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 
def H1_rot_123_mmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) 


omega1   = 4
omega2   = 10
omega3   = 17

X = jmat(1,'x')
Y = jmat(1,'y')
Z = jmat(1,'z')

#R = 1/sqrt(2) * (Y + Z)
#R = 1/sqrt(2) * Qobj([[1+0j,0-1j,0],[0+1j,-1+0j,0],[0,0,1]])

R=1

one  = R * basis(3,1)
zero = R * basis(3,0)
two  = R * basis(3,2)

a = R * destroy(3) * R

q1 = 0.5*tensor(a, qeye(3),qeye(3))
q2 = 0.5*tensor(qeye(3),a,qeye(3))
q3 = 0.5*tensor(qeye(3),qeye(3),a)

#H0  = 0 * tensor(a,a,a)
H0 = omega1 * q1.dag()*q1 + omega2 * q2.dag()*q2 + omega3 * q3.dag()*q3 + U1 * q1.dag() * q1.dag() * q1 * q1 + U2 * q2.dag() * q2.dag() * q2 * q2 + U3 * q3.dag() * q3.dag() * q3 * q3

#Define the multipliers for the system
EJ = 0.1

mult1_2 	= EJ * 0.5	 
mult3  		= EJ * 1.0

mult12 		= EJ * 0.25
mult13_23	= EJ * 0.5

mult123	 	= EJ * 0.25

H = [H0,
#The Hamiltonian is split into three parts due to the expansion of the sin and cos terms in H_int.
#s * sin(0.5) term
[mult1_2 *  q1,H1_rot1],[mult1_2 *  q1.dag(),H1_rot1d],[mult1_2 *  q2,H1_rot2],[mult1_2 *  q2.dag(),H1_rot2d],[mult3 *  q3,H1_rot3],[mult3 *  q3.dag(),H1_rot3d],
[mult12 *  q1*q2,H1_rot12_pp],[mult12 *  q1*q2.dag(),H1_rot12_pm],[mult12 *  q1.dag()*q2,H1_rot12_mp],[mult12 *  q1.dag()*q2.dag(),H1_rot12_mm],
[mult13_23 *  q1*q3,H1_rot13_pp],[mult13_23 *  q1*q3.dag(),H1_rot13_pm],[mult13_23 * mult13_23 *  q1.dag()*q3,H1_rot13_mp],[mult13_23 *  q1.dag()*q3.dag(),H1_rot13_mm],
[mult13_23 *  q2*q3,H1_rot23_pp],[mult13_23 *  q2*q3.dag(),H1_rot23_pm],[mult13_23 * mult13_23 *  q2.dag()*q3,H1_rot23_mp],[mult13_23 *  q2.dag()*q3.dag(),H1_rot23_mm],
[mult123 *  q1*q2*q3,H1_rot_123_ppp],[mult123 *  q1*q2*q3.dag(),H1_rot_123_ppm],[mult123 *  q1*q2.dag()*q3,H1_rot_123_pmp],[mult123 *  q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult123 *  q1.dag()*q2*q3,H1_rot_123_mpp],[mult123 *  q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult123 *  q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult123 *  q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm]]

tlist = np.linspace(0,2000,2**10)

R=1
sx1 = tensor(R * X * R,qeye(3),qeye(3))
sx2 = tensor(qeye(3), R * X * R,qeye(3))
sx3 = tensor(qeye(3),qeye(3), R * X * R)

sy1 = tensor(R * Y * R,qeye(3),qeye(3))
sy2 = tensor(qeye(3), R * Y * R,qeye(3))
sy3 = tensor(qeye(3),qeye(3), R * Y * R)

sz1 = tensor(R * Z * R,qeye(3),qeye(3))
sz2 = tensor(qeye(3), R * Z * R,qeye(3))
sz3 = tensor(qeye(3),qeye(3), R * Z * R)

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.002*sz1,0.002*sz2,0.002*sz3]

outputstr = ''


for i in range(0,1):
	if i == 0:
		psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
		outputstr = 'Output/Toffoli_23-04-19/'
	if i == 1:	
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Toffoli_23-04-19/'
	if i == 2:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Toffoli_23-04-19/'
	'''
	if i == 3:
		psi0 = tensor(zero,one,one);Tdm = tensor(zero,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity011.dat'
	if i == 4:
		psi0 = tensor(one,zero,zero);Tdm = tensor(one,zero,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity100.dat'
	if i == 5:
		psi0 = tensor(one,zero,one);Tdm = tensor(one,zero,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity101.dat'
	if i == 6:
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity110.dat'
	if i == 7:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity111.dat'
	'''

	#print(psi0)

	result = mesolve(H,psi0,tlist,c_ops,[sy1,sy2,sy3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


	fidelity_dat = []

	Qubit_state_1_0 = []
	Qubit_state_1_1 = []
	Qubit_state_1_2 = []

	Qubit_state_2_0 = []
	Qubit_state_2_1 = []
	Qubit_state_2_2 = []

	Qubit_state_3_0 = []
	Qubit_state_3_1 = []
	Qubit_state_3_2 = []

	Expect_sz1 = []
	Expect_sz2 = []
	Expect_sz3 = []

	#print(result.states[0])

	for j in range(0,len(tlist)):
	 		fidelity_dat.append(fidelity(result.states[j],Tdm))
	 		Qubit_state_1_0.append(expect(result.states[j].ptrace(0),zero).real)
	 		Qubit_state_1_1.append(expect(result.states[j].ptrace(0),one).real)
	 		Qubit_state_1_2.append(expect(result.states[j].ptrace(0),two).real)

	 		Qubit_state_2_0.append(expect(result.states[j].ptrace(1),zero).real)
	 		Qubit_state_2_1.append(expect(result.states[j].ptrace(1),one).real)
	 		Qubit_state_2_2.append(expect(result.states[j].ptrace(1),two).real)

	 		Qubit_state_3_0.append(expect(result.states[j].ptrace(2),zero).real)
	 		Qubit_state_3_1.append(expect(result.states[j].ptrace(2),one).real)
	 		Qubit_state_3_2.append(expect(result.states[j].ptrace(2),two).real)

	 		Expect_sz1.append(result.expect[0][j])
			Expect_sz2.append(result.expect[1][j])
			Expect_sz3.append(result.expect[2][j])

	with open(outputstr + 'Qubit_state_1_0.dat','w') as f1:
		for j in Qubit_state_1_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_1_1.dat','w') as f1:
		for j in Qubit_state_1_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_1_2.dat','w') as f1:
		for j in Qubit_state_1_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Qubit_state_2_0.dat','w') as f1:
		for j in Qubit_state_2_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_2_1.dat','w') as f1:
		for j in Qubit_state_2_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_2_2.dat','w') as f1:
		for j in Qubit_state_2_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Qubit_state_3_0.dat','w') as f1:
		for j in Qubit_state_3_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_3_1.dat','w') as f1:
		for j in Qubit_state_3_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_3_2.dat','w') as f1:
		for j in Qubit_state_3_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Fidelity.dat','w') as f1:
		for j in fidelity_dat:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Expect_sz1.dat','w') as f1:
		for j in Expect_sz1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Expect_sz2.dat','w') as f1:
		for j in Expect_sz2:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Expect_sz3.dat','w') as f1:
		for j in Expect_sz3:
			f1.write(str(j) + "\n")