import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime



((-1*cos(omega3 * t) + 2*cos(omega2*t + 0.5*PI) + 2*cos(omega1 * t + 0.5*PI) + 4*cos((omega1 + omega2)*t) - 4*cos((omega1 - omega2)*t) + 2*cos((omega1 + omega3)*t + 0.5*PI) + 2*cos((omega1-omega2)*t) + 2*cos((omega2 + omega3)*t) + 2*cos((omega2 - omega3)*t) - 4*cos((omega1 + omega2 + omega3)*t) - 4*cos((omega1 + omega2 - omega3)*t) - 4*cos((omega1 - omega2 + omega3)*t) - 4*cos((omega1 - omega2 - omega3)*t)))
((-1*cos(omega3 * t) + 2*cos(omega2*t + 0.5*PI) + 2*cos(omega1 * t + 0.5*PI) + 4*cos((omega1 + omega2)*t) - 4*cos((omega1 - omega2)*t) + 2*cos((omega1 + omega3)*t + 0.5*PI) + 2*cos((omega1-omega2)*t) + 2*cos((omega2 + omega3)*t) + 2*cos((omega2 - omega3)*t) - 4*cos((omega1 + omega2 + omega3)*t) - 4*cos((omega1 + omega2 - omega3)*t) - 4*cos((omega1 - omega2 + omega3)*t) - 4*cos((omega1 - omega2 - omega3)*t)))

def H1_rot1(t,*args):
<<<<<<< HEAD
	return (-0.25*cos(omega1 * t + 0.5*PI) )*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (-0.25*cos(omega1 * t + 0.5*PI) )*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (-0.25*cos(omega2*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (-0.25*cos(omega2*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot3(t,*args):
	return ((0.25*cos(omega3 * t))*(cos(omega3 * t) + (0+1j)*sin(omega3*t)))
def H1_rot3d(t,*args):
	return ((0.25*cos(omega3 * t))*(cos(omega3 * t) - (0+1j)*sin(omega3*t)))

def H1_rot12_pp(t,*args):
	return ( 0.25*cos((omega1 + omega2)*t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return ( 0.25*cos((omega1 - omega2)*t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return (0.25*cos((-omega1 + omega2)*t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (0.25*cos((-omega1 - omega2)*t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return ( -0.25*cos((omega1 + omega3)*t + 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return ( -0.25*cos((omega1 - omega3)*t + 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return ( -0.25*cos((-omega1 + omega3)*t + 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return ( -0.25*cos((-omega1 - omega3)*t + 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return ( -0.25*cos((omega2 + omega3)*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return ( -0.25*cos((omega2 - omega3)*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return ( -0.25*cos((-omega2 + omega3)*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return ( -0.25*cos((-omega2 - omega3)*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return ( 0.25*cos((omega1 + omega2 + omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return ( 0.25*cos((omega1 + omega2 - omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return ( 0.25*cos((omega1 - omega2 + omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return ( 0.25*cos((omega1 - omega2 - omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return ( 0.25*cos((-omega1 + omega2 + omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return ( 0.25*cos((-omega1 + omega2 - omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return ( 0.25*cos((-omega1 - omega2 + omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return ( 0.25*cos((-omega1 - omega2 - omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(2),qeye(2),qeye(2))

#Define the multipliers for the system
EJ = 0.1

mult1_2 	= EJ 	 
mult3  		= EJ

mult12 		= EJ 
mult13_23	= EJ 

mult123	 	= EJ 

H = [H0,
#The Hamiltonian is split into three parts due to the expansion of the sin and cos terms in H_int.
#s * sin(0.5) term
[mult1_2 *  q1,H1_rot1],[mult1_2 *  q1.dag(),H1_rot1d],[mult1_2 *  q2,H1_rot2],[mult1_2 *  q2.dag(),H1_rot2d],[mult3 *  q3,H1_rot3],[mult3 *  q3.dag(),H1_rot3d],
[mult12 *  q1*q2,H1_rot12_pp],[mult12 *  q1*q2.dag(),H1_rot12_pm],[mult12 *  q1.dag()*q2,H1_rot12_mp],[mult12 *  q1.dag()*q2.dag(),H1_rot12_mm],
[mult13_23 *  q1*q3,H1_rot13_pp],[mult13_23 *  q1*q3.dag(),H1_rot13_pm],[mult13_23 * mult13_23 *  q1.dag()*q3,H1_rot13_mp],[mult13_23 *  q1.dag()*q3.dag(),H1_rot13_mm],
[mult13_23 *  q2*q3,H1_rot23_pp],[mult13_23 *  q2*q3.dag(),H1_rot23_pm],[mult13_23 * mult13_23 *  q2.dag()*q3,H1_rot23_mp],[mult13_23 *  q2.dag()*q3.dag(),H1_rot23_mm],
[mult123 *  q1*q2*q3,H1_rot_123_ppp],[mult123 *  q1*q2*q3.dag(),H1_rot_123_ppm],[mult123 *  q1*q2.dag()*q3,H1_rot_123_pmp],[mult123 *  q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult123 *  q1.dag()*q2*q3,H1_rot_123_mpp],[mult123 *  q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult123 *  q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult123 *  q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm]]


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,800,1000)
#R = 1/sqrt(2) * (sigmay() + sigmaz())
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

#print(s1z)
#print(sy1)

H2 = 0.25*(I + s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
#print(H2)


c_ops = [0.01*q1,0.01*q2,0.01*q3,0.02*sz1,0.02*sz2,0.02*sz3]

outputstr = ''

#freqs = np.genfromtxt('Frequencies3.dat')
freqs = [[4,10,17]]
for j in freqs:
	print(j)
	omega1   = j[0]
	omega2   = j[1]
	omega3   = j[2]
	f1 = j[0]
	f2 = j[1]
	f3 = j[2]
	for i in range(0,2):
		if i == 0:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			outputstr_fidelity = 'Output/Toffoli_04-05-19/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_1 = 'Output/Toffoli_04-05-19/occupation000_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_2 = 'Output/Toffoli_04-05-19/occupation000_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_3 = 'Output/Toffoli_04-05-19/occupation000_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 10:	
			psi0 = tensor(zero,zero,one);Tdm = tensor(zero,zero,one)
			outputstr = 'Output/Toffoli_04-05-19/fidelity001.dat'
			print('001')
		if i == 20:
			psi0 = tensor(zero,one,zero);Tdm = tensor(zero,one,zero)
			outputstr = 'Output/Toffoli_04-05-19/fidelity010.dat'
			print('010')
		if i == 30:
			psi0 = tensor(zero,one,one);Tdm = tensor(zero,one,one)
			outputstr = 'Output/Toffoli_04-05-19/fidelity011.dat'
			print('011')
		if i == 40:
			psi0 = tensor(one,zero,zero);Tdm = tensor(one,zero,zero)
			outputstr = 'Output/Toffoli_04-05-19/fidelity100.dat'
			print('100')
		if i == 50:
			psi0 = tensor(one,zero,one);Tdm = tensor(one,zero,one)
			outputstr = 'Output/Toffoli_04-05-19/fidelity101.dat'
			print('101')
		if i == 60:
			psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
			outputstr = 'Output/Toffoli_04-05-19/fidelity110-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('110')
		if i == 1:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			outputstr_fidelity = 'Output/Toffoli_04-05-19/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_1 = 'Output/Toffoli_04-05-19/occupation111_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_2 = 'Output/Toffoli_04-05-19/occupation111_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_occupation_3 = 'Output/Toffoli_04-05-19/occupation111_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


		fidelity_dat = []
		occupation1 = []
		occupation2 = []
		occupation3 = []
		for j in range(0,len(tlist)):
		 		fidelity_dat.append(fidelity(result.states[j],Tdm))
		 		occupation1.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(0)).real)
		 		occupation2.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(1)).real)
		 		occupation3.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(2)).real)

		with open(outputstr_fidelity,'w') as f:
			for j in fidelity_dat:
				f.write(str(j) + "\n")
		with open(outputstr_occupation_1 , 'w') as f:
			for j in occupation1:
				f.write(str(j) + "\n")
		with open(outputstr_occupation_2 , 'w') as f:
			for j in occupation2:
				f.write(str(j) + "\n")
		with open(outputstr_occupation_3 , 'w') as f:
			for j in occupation3:
				f.write(str(j) + "\n")

