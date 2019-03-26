from math import *
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
import time
import datetime

PI 		= 3.14159265359 

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


R 			= 1	
i 			= qeye(2) # Identity
a 			= R * sigmap() * R # anhilation operator
one  		= R*basis(2,1)#Basis vetors
zero 		= R*basis(2,0)

Identity 	= tensor(i,i,i,i,i)
q1 			= tensor(a,i,i,i,i)
q2 			= tensor(i,a,i,i,i)
q3 			= tensor(i,i,a,i,i)
sP 			= tensor(i,i,i,a,i)
sM 			= tensor(i,i,i,i,a)

phiM = 0.05 * (sM + sM.dag())

omega1 		= 20
omega2 		= 15
omega3 		= 8
omegaP 		= 50
omegaM 		= 10

U1			= 5.8
U2 			= 3.27
U3			= 1.04

E_J 		= 0.1
phiAC 		= 0.1

H0 = omega1 * q1.dag()*q1 + omega2 * q2.dag()*q2 + omega3 * q3.dag()*q3 + omegaP * sP.dag() * sP + omegaM * sM.dag() * sM + U1 * q1.dag() * q1.dag() * q1 * q1 + U2 * q2.dag() * q2.dag() * q2 * q2 + U3 * q3.dag() * q3.dag() * q3 * q3
'''
mult  = 0.01
mult2 = 0.01

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[q3,H1_rot3],[q3.dag(),H1_rot3d],
[mult * q1*q2,H1_rot12_pp],[mult * q1*q2.dag(),H1_rot12_pm],[mult * q1.dag()*q2,H1_rot12_mp],[mult * q1.dag()*q2.dag(),H1_rot12_mm],
[mult * q1*q3,H1_rot13_pp],[mult * q1*q3.dag(),H1_rot13_pm],[mult * q1.dag()*q3,H1_rot13_mp],[mult * q1.dag()*q3.dag(),H1_rot13_mm],
[mult * q2*q3,H1_rot23_pp],[mult * q2*q3.dag(),H1_rot23_pm],[mult * q2.dag()*q3,H1_rot23_mp],[mult * q2.dag()*q3.dag(),H1_rot23_mm],
[mult2 * q1*q2*q3,H1_rot_123_ppp],[mult2 * q1*q2*q3.dag(),H1_rot_123_ppm],[mult2 * q1*q2.dag()*q3,H1_rot_123_pmp],[mult2 * q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult2 * q1.dag()*q2*q3,H1_rot_123_mpp],[mult2 * q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult2 * q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult2 * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm]]
'''

coeff1_12_coeff 	= 3  		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
coeff1_3_coeff  	=-6 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
	
coeff2_1_coeff  	= 1 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())
coeff2_23_coeff		=-2 		* E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())

coeff3_coeff    	= 0.666667  * E_J * phiAC * ((0.5*phiM).cosm() + (0.5*phiM).sinm())

H = [H0,[coeff1_12_coeff * q1,H1_rot1],[coeff1_12_coeff * q2,H1_rot1d],[coeff1_12_coeff * q2,H1_rot2],[coeff1_12_coeff * q2,H1_rot2d],[coeff1_3_coeff * q3,H1_rot3],[coeff1_3_coeff * q3,H1_rot3d],
[coeff2_1_coeff  * q1 * q2,H1_rot12_pp],[coeff2_1_coeff  * q1.dag() * q2,H1_rot12_mp],[coeff2_1_coeff  * q1 * q2.dag(),H1_rot12_pm],[coeff2_1_coeff  * q1.dag() * q2.dag(),H1_rot12_mm],
[coeff2_23_coeff * q1 * q3,H1_rot13_pp],[coeff2_23_coeff * q1.dag() * q3,H1_rot13_mp],[coeff2_23_coeff * q1 * q3.dag(),H1_rot13_pm],[coeff2_23_coeff * q1.dag() * q3.dag(),H1_rot13_mm],
[coeff2_23_coeff * q2 * q3,H1_rot23_pp],[coeff2_23_coeff * q3.dag() * q3,H1_rot23_mp],[coeff2_23_coeff * q2 * q3.dag(),H1_rot23_pm],[coeff2_23_coeff * q2.dag() * q3.dag(),H1_rot23_mm],
[coeff3_coeff * q1 * q2 * q3,H1_rot_123_ppp],[coeff3_coeff * q1.dag() * q2 * q3,H1_rot_123_mpp],[coeff3_coeff * q1 * q2.dag() * q3,H1_rot_123_pmp],[coeff3_coeff * q1 * q2 * q3.dag(),H1_rot_123_ppp],
[coeff3_coeff * q1.dag() * q2.dag() * q3,H1_rot_123_mmp],[coeff3_coeff * q1.dag() * q2 * q3.dag(),H1_rot_123_mpm],[coeff3_coeff * q1 * q2.dag() * q3.dag(),H1_rot_123_pmm],
[coeff3_coeff * q1.dag() * q2.dag() * q3.dag(),H1_rot_123_mmm]]


tlist = np.linspace(0,2**9,2**9)

sx1 = tensor(R 		* sigmax() * R,i,i,i,i)
sx2 = tensor(i, R 	* sigmax() * R,i,i,i)
sx3 = tensor(i,i, R * sigmax() * R,i,i)

sy1 = tensor(R 		* sigmay() * R,i,i,i,i)
sy2 = tensor(i, R 	* sigmay() * R,i,i,i)
sy3 = tensor(i,i, R * sigmay() * R,i,i)

sz1 = tensor(R 		* sigmaz() * R,i,i,i,i)
sz2 = tensor(i, R 	* sigmaz() * R,i,i,i)
sz3 = tensor(i,i, R * sigmaz() * R,i,i)
sz5 = tensor(i,i,i,i,sigmaz())

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.002*sz1,0.002*sz2,0.002*sz3,0.001*sM,0.001*sP]

outputstr = ''
today = datetime.date.today().strftime("%B_%d_%Y")

start = time.time()
psi0 = tensor(one,one,one,zero,zero);Tdm = tensor(one,one,zero,zero,zero)
outputstr = 'Output/Data/Toffoli_Real_' + today +'/Five_test.dat'


result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2,sx3,sy3,sz3,sz5],options = Options(nsteps = 2**14,store_states = True,store_final_state = True))


fidelity_dat = []
for j in range(0,len(tlist)):
 		fidelity_dat.append(fidelity(result.states[j],Tdm))

with open(outputstr,'w') as f1:
	for j in fidelity_dat:
		f1.write(str(j) + "\n")
for j in result.expect[9]:
	print(j)
#for j in range(0,len(tlist)):
#print(fidelity(result.states[j],sM))


end = time.time()
print('Time Taken for Simulation:')
print(end - start)