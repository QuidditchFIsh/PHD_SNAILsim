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
omega = 30
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

avg_sz1 = []
avg_sz2 = []
avg_sz3 = []
avg_sz4 = []

fidelity111 = []
fidelity110 = []
fidelity101 = []
fidelity011 = []
fidelity100 = []
fidelity010 = []
fidelity001 = []

eval_op_list = [sz1,sz2,sz3]

Wlist = np.linspace(0,500,500)

Hon = [H0,[H1,H1_Coeff_On]]
Hoff = [H0,[H1,H1_Coeff_Off]]

print("Begining Calcultions")
start = time.time()
for i in Wlist:
	omega = i
	result1 = mesolve(Hon,psi0,tlist1,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_final_state = True))
	#plt.plot(tlist1,np.real(result1.expect[0]))
	#plt.show()
	fidelity111.append(fidelity(result1.final_state,Tdm_111))
	fidelity110.append(fidelity(result1.final_state,Tdm_110))
	fidelity101.append(fidelity(result1.final_state,Tdm_101))
	fidelity011.append(fidelity(result1.final_state,Tdm_011))
	fidelity100.append(fidelity(result1.final_state,Tdm_100))
	fidelity001.append(fidelity(result1.final_state,Tdm_001))
	fidelity010.append(fidelity(result1.final_state,Tdm_010))

	avg_sz1.append(np.average(np.real(result1.expect[0])))
	avg_sz2.append(np.average(np.real(result1.expect[1])))
	avg_sz3.append(np.average(np.real(result1.expect[2])))
end = time.time()
print("Processing Data")
with open('../Output/RF/RF_QuBit_1_Expect_SZ.txt','w') as f:
	for i in avg_sz1:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_2_Expect_SZ.txt','w') as f:
	for i in avg_sz2:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_3_Expect_SZ.txt','w') as f:
	for i in avg_sz3:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_111.txt','w') as f:
	for i in fidelity111:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_110.txt','w') as f:
	for i in fidelity110:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_101.txt','w') as f:
	for i in fidelity101:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_011.txt','w') as f:
	for i in fidelity011:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_100.txt','w') as f:
	for i in fidelity100:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_001.txt','w') as f:
	for i in fidelity001:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_Fidelity_010.txt','w') as f:
	for i in fidelity010:
		f.write(str(i) + "\n")


with open('../Output/RF/RF_QuBit_1_Expect_SZ.txt','r') as f:
	f1 = plt.figure(1)
	plt.plot(Wlist,avg_sz1)
	plt.title("Omega vs Sigmaz 1")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/RF/Img/RF_Omega_vs_Expectation1.png')
with open('../Output/RF/RF_QuBit_2_Expect_SZ.txt','r') as f:
	f2 = plt.figure(2)
	plt.plot(Wlist,avg_sz2)
	plt.title("Omega vs Sigmaz 2")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/RF/Img/RF_Omega_vs_Expectation2.png')
with open('../Output/RF/RF_QuBit_3_Expect_SZ.txt','r') as f:
	f3 = plt.figure(3)
	plt.title("Omega vs Sigmaz 3")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.plot(Wlist,avg_sz3)
	plt.savefig('../Output/RF/Img/RF_Omega_vs_Expectation3.png')
with open('../Output/RF/RF_QuBit_Fidelity_111.txt','r') as f:
	f3 = plt.figure(4)
	plt.title("Omega vs Fidelity 111")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity111)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_111_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_110.txt','r') as f:
	f3 = plt.figure(5)
	plt.title("Omega vs Fidelity 110")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity110)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_110_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_101.txt','r') as f:
	f3 = plt.figure(6)
	plt.title("Omega vs Fidelity 101")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity101)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_101_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_011.txt','r') as f:
	f3 = plt.figure(7)
	plt.title("Omega vs Fidelity 011")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity011)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_011_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_100.txt','r') as f:
	f3 = plt.figure(8)
	plt.title("Omega vs Fidelity 100")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity100)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_100_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_001.txt','r') as f:
	f3 = plt.figure(9)
	plt.title("Omega vs Fidelity 001")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity001)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_001_vs_omega.png')
with open('../Output/RF/RF_QuBit_Fidelity_010.txt','r') as f:
	f3 = plt.figure(10)
	plt.title("Omega vs Fidelity 010")
	plt.xlabel("Omega")
	plt.ylabel("Fidelity")
	plt.plot(Wlist,fidelity010)
	plt.savefig('../Output/RF/Img/RF_QuBit_Fidelity_010_vs_omega.png')


f5 = plt.figure(11)
plt.plot(avg_sz1)
plt.plot(avg_sz2)
plt.plot(avg_sz3)
plt.title("Omega vs Sigmaz All")
plt.xlabel("Omega")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF/Img/RF_Omega_vs_Expectation_ALL.png')
plt.legend(loc='right',fancybox = True, shadow = True)

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")