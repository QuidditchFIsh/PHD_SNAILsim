import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def H1_rot1(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot3(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot3d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot12_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

#All of the variables defined wihtin the constants class now write the hamiltonian 

#beginning with the Time independant Hamiltonian we are using H/hbar for convience

H0 = omega1 * q1.dag()*q1 + omega2 * q2.dag()*q2 + omega3 * q3.dag()*q3

H0 += U1 * q1.dag() * q1.dag() * q1 * q1 + U2 * q2.dag() * q2.dag() * q2 * q2 + U3 * q3.dag() * q3.dag() * q3 * q3

H0 += omegaP * sP.dag() * sP + omegaM * sM.dag() * sM

#Define the Time independant Hamtiltonian
coeff1_12_coeff 	= 3  		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
coeff1_3_coeff  	=-6 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
	
coeff2_1_coeff  	= 1 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
coeff2_23_coeff		=-2 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())

coeff3_coeff    	= 0.666667  * E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())

H = [H0,[coeff1_12_coeff * q1,H1_rot1],[coeff1_12_coeff * q2,H1_rot1d],[coeff1_12_coeff * q2,H1_rot2],[coeff1_12_coeff * q2,H1_rot2d],[coeff1_3_coeff * q3,H3_rot1],[coeff1_3_coeff * q3,H3_rot1d],
[coeff2_1_coeff  * q1 * q2,H1_rot12_pp],[coeff2_1_coeff  * q1.dag() * q2,H1_rot12_mp],[coeff2_1_coeff  * q1 * q2.dag(),H1_rot12_pm],[coeff2_1_coeff  * q1.dag() * q2.dag(),H1_rot12_mm],
[coeff2_23_coeff * q1 * q3,H1_rot13_pp],[coeff2_23_coeff * q1.dag() * q3,H1_rot13_mp],[coeff2_23_coeff * q1 * q3.dag(),H1_rot13_pm],[coeff2_23_coeff * q1.dag() * q3.dag(),H1_rot13_mm],
[coeff2_23_coeff * q2 * q3,H1_rot23_pp],[coeff2_23_coeff * q3.dag() * q3,H1_rot23_mp],[coeff2_23_coeff * q2 * q3.dag(),H1_rot23_pm],[coeff2_23_coeff * q2.dag() * q3.dag(),H1_rot23_mm],
[coeff3_coeff * q1 * q2 * q3,H1_rot_123_ppp],[coeff3_coeff * q1.dag() * q2 * q3,H1_rot_123_mpp],[coeff3_coeff * q1 * q2.dag() * q3,H1_rot_123_pmp],[coeff3_coeff * q1 * q2 * q3.dag(),H1_rot_123_ppp],
[coeff3_coeff * q1.dag() * q2.dag() * q3,H1_rot_123_mmp],[coeff3_coeff * q1.dag() * q2 * q3.dag(),H1_rot_123_mpm],[coeff3_coeff * q1 * q2.dag() * q3.dag(),H1_rot_123_pmm],
[coeff3_coeff * q1.dag() * q2.dag() * q3.dag(),H1_rot_123_mmm]]

# Set up the calculations

tlist = np.linspace(0,2**10,2**11)

R=1

sx1 = tensor(R 		* sigmax() * R,i,i,i,i)
sx2 = tensor(i, R 	* sigmax() * R,i,i,i)
sx3 = tensor(i,i, R * sigmax() * R,i,i)

sy1 = tensor(R 		* sigmay() * R,i,i,i,i)
sy2 = tensor(i, R 	* sigmay() * R,i,i,i)
sy3 = tensor(i,i, R * sigmay() * R,i,i)

sz1 = tensor(R 		* sigmaz() * R,i,i,i,i)
sz2 = tensor(i, R 	* sigmaz() * R,i,i,i)
sz3 = tensor(i,i, R * sigmaz() * R,i,i)

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.002*sz1,0.002*sz2,0.002*sz3]

outputstr = ''
today = '21-03-19'

start = time.time()
for i in range(0,3):
	if i == 0:
		psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
		outputstr = 'Output/Data/Toffoli_Real_' + today +'/fidelity000.dat'
		print('1')
	if i == 1:
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Data/Toffoli_Real_' + today +'/fidelity110.dat'
		print('2')
	if i == 2:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Data/Toffoli_Real_' + today +'/fidelity111.dat'
		print('3')
		
	result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2,sx3,sy3,sz3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


	fidelity_dat = []
	for j in range(0,len(tlist)):
	 		fidelity_dat.append(fidelity(result.states[j],Tdm))

	with open(outputstr,'w') as f1:
		for j in fidelity_dat:
			f1.write(str(j) + "\n")


end = time.time()
print('Time Taken for Simulation:')
print(end - start)