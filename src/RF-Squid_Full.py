'''
Author: Aneirin John Baker
Date : 15/01/2019
Description:Simulation of an RF Squid with the Full Hamiltonian to make sure that the perturbations which were calculated
are valid and that the approximations which were made are also valid
'''

import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time

#Define the time dependant terms in the Hamiltonian as functions to be called
omega = 30
Amplitude = 50

def H1_Coeff_On(t,*args):
	return Amplitude * cos(omega * t)
def H1_Coeff_Off(t,*args):
	return 1

#Constants will be defined in the constants class

print("============================================")
print("Begining Program, setting up calculations")

N = 2
q1 = tensor(destroy(N),qeye(N),qeye(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N),qeye(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N),qeye(N),qeye(N))
sP = tensor(qeye(N),qeye(N),qeye(N),destroy(N),qeye(N))
sM = tensor(qeye(N),qeye(N),qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()
sPd = sP.dag()
sMd = sM.dag()

phi1 = phibar1 * (q1 + q1d)
phi2 = phibar2 * (q2 + q2d)
phi3 = phibar3 * (q3 + q3d)
varphiP = (phi1 + phi2 + 2*phi3)
varphiM = (phi1 + phi2 - 2*phi3)

pi1 = (1/(2 * phibar1)) * (q1 - q1d)
pi2 = (1/(2 * phibar2)) * (q2 - q2d)
pi3 = (1/(2 * phibar3)) * (q3 - q3d)

phiP = phibarP * (sP + sPd)
phiM = phibarM * (sM + sMd)

phiMhalf = 0.5 * phiM
phiMthird = 0.3333333333333333 * phiM

piP = (1/(2 * phibarP)) * (sP - sPd)
piM = (1/(2 * phibarM)) * (sM - sMd)

#Setting up the Hamiltonian .....THis is gonna be long

H0 = 0
H1 = 0
#Will have to check about the cos of the matrix
H0 += (4 * ECQ1 * (1/1**2)) * pi1*pi1 + (4 * ECQ2 * (1/1**2)) * pi2*pi2 + (4 * ECQ3 * (1/1**2)) * pi3*pi3 + EJ1 * phi1.cosm() + EJ2 * phi2.cosm() + EJ3 * phi3.cosm() + (phi0**2 * (1/(2*L)) * ((phi1 * phi1) + (phi2 * phi2) + 0.5 * (phi3 * phi3)))

H0 += EL * (phiP*phiP + phiM*phiM) + EL * (phiP*varphiP + phiM*varphiM) 
H0 += phiP*phiP * (0.5 * (1/CG) * (1/phi0**2)) + phiM * phiM * (0.5 * (1/CG) * (1/phi0**2))

H1 += EJ * phiMhalf.sinm() + EJ * phiMhalf.cosm()

print(H0)

#Prepareing the rest of the calculations
tlist = np.linspace(0, 50, 50)
tlist1 = np.linspace(100, 200, 400)
#Basis states
psi_list = []
psi_list.append(basis(2,0))
for n in range(4):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)

#collapse operator list
c_op_list = [q1,q2,q3]

#operators to be evaulated
sz1 = tensor(sigmaz(),qeye(N),qeye(N),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N),qeye(N),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz(),qeye(N),qeye(N))

avg_sz1 = []
avg_sz2 = []
avg_sz3 = []
avg_sz4 = []

eval_op_list = [sz1,sz2,sz3]

Wlist = np.linspace(1,20,20)

Hon = [H0,[H1,H1_Coeff_On]]
Hoff = [H0,[H1,H1_Coeff_Off]]

print("Begining Calcultions")
start = time.time()
for i in Wlist:
	omega = i
	result = mesolve(Hoff,psi0,tlist,c_op_list,eval_op_list,options = Options(store_final_state=True,nsteps = 8000))

	result1 = mesolve(Hon,result.final_state,tlist1,c_op_list,eval_op_list,options = Options(nsteps = 8000))

	avg_sz1.append(np.average(np.real(result1.expect[0])))
	avg_sz2.append(np.average(np.real(result1.expect[1])))
	avg_sz3.append(np.average(np.real(result1.expect[2])))
end = time.time()
print("Processing Data")
with open('../Output/RF_full/RF_full_QuBit_1_Expect_SZ.txt','w') as f:
	for i in avg_sz1:
		f.write(str(i) + "\n")
with open('../Output/RF_full/RF_full_QuBit_2_Expect_SZ.txt','w') as f:
	for i in avg_sz2:
		f.write(str(i) + "\n")
with open('../Output/RF_full/RF_full_QuBit_3_Expect_SZ.txt','w') as f:
	for i in avg_sz3:
		f.write(str(i) + "\n")

with open('../Output/RF_full/RF_full_QuBit_1_Expect_SZ.txt','r') as f:
	f1 = plt.figure(1)
	plt.plot(Wlist,avg_sz1)
	plt.title("Omega vs Sigmaz 1")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/RF_full/Img/RF_full_Omega_vs_Expectation1.png')
with open('../Output/RF_full/RF_full_QuBit_2_Expect_SZ.txt','r') as f:
	f2 = plt.figure(2)
	plt.plot(Wlist,avg_sz2)
	plt.title("Omega vs Sigmaz 2")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/RF_full/Img/RF_full_Omega_vs_Expectation2.png')
with open('../Output/RF_full/RF_full_QuBit_3_Expect_SZ.txt','r') as f:
	f3 = plt.figure(3)
	plt.title("Omega vs Sigmaz 3")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.plot(Wlist,avg_sz3)
	plt.savefig('../Output/RF_full/Img/RF_full_Omega_vs_Expectation3.png')

f5 = plt.figure(5)
plt.plot(avg_sz1)
plt.plot(avg_sz2)
plt.plot(avg_sz3)
plt.title("Omega vs Sigmaz All")
plt.xlabel("Omega")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF_full/Img/RF_full_Omega_vs_Expectation_ALL.png')
plt.legend(loc='right',fancybox = True, shadow = True)

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")