'''
Author: Aneirin John Baker
Date : 14/01/2019
Description:Simulation of an RF Squid potential without the Hamiltonain for the RF squid to make things simpler. 
This siulation will be compared to the full simulation afterwards
'''
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time

#Define the time dependant terms in the Hamiltonian as functions to be called
omega = 35
Amplitude = 1

def H1_Coeff_On(t,*args):
	return Amplitude * cos(omega * t)
def H1_Coeff_Off(t,*args):
	return 1

#Constants will be defined in the constants class

print("============================================")
print("Begining Program, setting up calculations")

N = 2
q1 = tensor(destroy(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()

phi1 = phibar1 * (q1 + q1d)
phi2 = phibar2 * (q2 + q2d)
phi3 = phibar3 * (q3 + q3d)


H0 = 0
H1 = 0

H0 += (omega1 * q1d * q1) + (U1 * q1d * q1d * q1 * q1)
H0 += (omega2 * q2d * q2) + (U2 * q2d * q2d * q2 * q2)
H0 += (omega3 * q3d * q3) + (U3 * q3d * q3d * q3 * q3)

H1 += 0.25  * EJT * (phi1 + phi2 - (2 * phi3))**2

H1 += 0.5 * EJT * phi1 * phi2 * phi3

#Prepareing the rest of the calculations
tlist = np.linspace(0, 50, 50)
tlist1 = np.linspace(50, 100, 50)
#Basis states
psi_list = []
psi_list.append(basis(2,0))
for n in range(2):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)

#Define the Target Density Matricies
one  = basis(2,1)
zero = basis(2,0)

Tdm_111 = tensor(one ,one ,one  )
Tdm_110 = tensor(one ,one ,zero )
Tdm_101 = tensor(one ,zero,one  )
Tdm_011 = tensor(zero,one ,one  )
Tdm_100 = tensor(one ,zero,zero )
Tdm_001 = tensor(zero,zero,one  )
Tdm_010 = tensor(zero,one ,zero )


#collapse operator list
c_op_list = [q1,q2,q3]

#operators to be evaulated
sz1 = tensor(sigmaz(),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz())

fidelity111 = []
fidelity110 = []
fidelity101 = []
fidelity011 = []
fidelity100 = []
fidelity010 = []
fidelity001 = []

eval_op_list = [sz1,sz2,sz3]

#Wlist = [315,210,140,280,35,175,105]
Wlist = [315,210]

Hon = [H0,[H1,H1_Coeff_On]]
Hoff = [H0,[H1,H1_Coeff_Off]]

print("Begining Calcultions")
start = time.time()
tlist = np.linspace(0, 1, 1000)
for i in Wlist:
	omega = i
	result = mesolve(Hon,psi0,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_states = True))	

	for i in range(0,1000):
		fidelity111.append(fidelity(result.states[i],Tdm_111))
		fidelity110.append(fidelity(result.states[i],Tdm_110))
		fidelity101.append(fidelity(result.states[i],Tdm_101))
		fidelity011.append(fidelity(result.states[i],Tdm_011))
		fidelity100.append(fidelity(result.states[i],Tdm_100))
		fidelity001.append(fidelity(result.states[i],Tdm_001))
		fidelity010.append(fidelity(result.states[i],Tdm_010))
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity111.txt','w') as f:
		for j in fidelity111:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity110.txt','w') as f:
		for j in fidelity110:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity101.txt','w') as f:
		for j in fidelity101:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity011.txt','w') as f:
		for j in fidelity011:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity100.txt','w') as f:
		for j in fidelity100:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity001.txt','w') as f:
		for j in fidelity001:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + '_fidelity010.txt','w') as f:
		for j in fidelity010:
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + 'sigmaz_1.txt','w') as f:
		for j in np.real(result.expect[0]):
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + 'sigmaz_2.txt','w') as f:
		for j in np.real(result.expect[1]):
			f.write(str(j) + "\n")
	with open('../Output/RF_24-01-19/RF-freq_explore/RF_SQUID_' + str(omega) + 'sigmaz_3.txt','w') as f:
		for j in np.real(result.expect[2]):
			f.write(str(j) + "\n")

end = time.time()

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")