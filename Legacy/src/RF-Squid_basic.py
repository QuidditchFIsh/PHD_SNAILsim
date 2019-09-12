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
Amplitude = 2

def H1_Coeff_On(t,*args):
	return 0.125 * cos(35 * t) + 0.125 * cos(105 * t) + 0.125 * cos(176 * t)+ 0.0625 * cos(281 * t)+ 0.0625 * cos(71 * t)+ 0.0625 * cos(211 * t)+ 0.0625 * cos(141 * t)+ 0.0625 * cos(140 * t)+ 0.0625 * cos(70 * t)+ 0.03125 * cos(316 * t)+ 0.03125 * cos(36 * t)+ 0.03125 * cos(106 * t)+ 0.03125 * cos(246 * t)
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
psi_list.append((basis(2,0)-(0+1j)*basis(2,1)).unit())
for n in range(2):
    psi_list.append((basis(2,0) - (0 + 1j)*basis(2,1)).unit())
psi0 = tensor(psi_list)

#Define the Target Density Matricies
one  = (basis(2,0)+(0+1j)*basis(2,1)).unit()
zero = (basis(2,0)-(0+1j)*basis(2,1)).unit()

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


Hon = [H0,[H1,H1_Coeff_On]]
Hoff = [H0,[H1,H1_Coeff_Off]]

print("Begining Calcultions")
start = time.time()
#for i in Wlist:
tlist = np.linspace(0, 1, 500)
result1 = mesolve(Hon,psi0,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_final_state = True,store_states = True))
#plt.plot(tlist1,np.real(result1.expect[0]))
#plt.show()

for j in result1.states:

	fidelity111.append(fidelity(j,Tdm_111))
	fidelity110.append(fidelity(j,Tdm_110))
	fidelity101.append(fidelity(j,Tdm_101))
	fidelity011.append(fidelity(j,Tdm_011))
	fidelity100.append(fidelity(j,Tdm_100))
	fidelity001.append(fidelity(j,Tdm_001))
	fidelity010.append(fidelity(j,Tdm_010))
avg_sz1.append(np.real(result1.expect[0]))
avg_sz2.append(np.real(result1.expect[1]))
avg_sz3.append(np.real(result1.expect[2]))

end = time.time()

print("Processing Data")
with open('../Output/RF_28-01-19/RF_QuBit_1_Expect_SZ.txt','w') as f:
	for i in result1.expect[0]:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_2_Expect_SZ.txt','w') as f:
	for i in result1.expect[1]:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_3_Expect_SZ.txt','w') as f:
	for i in result1.expect[2]:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_111.txt','w') as f:
	for i in fidelity111:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_110.txt','w') as f:
	for i in fidelity110:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_101.txt','w') as f:
	for i in fidelity101:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_011.txt','w') as f:
	for i in fidelity011:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_100.txt','w') as f:
	for i in fidelity100:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_001.txt','w') as f:
	for i in fidelity001:
		f.write(str(i) + "\n")
with open('../Output/RF_28-01-19/RF_QuBit_Fidelity_010.txt','w') as f:
	for i in fidelity010:
		f.write(str(i) + "\n")



f1 = plt.figure(1)
plt.plot(tlist,result1.expect[0])
plt.title("Time vs Sigmaz 1")
plt.xlabel("Time")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF_28-01-19/Img/RF_Omega_vs_Expectation1.png')	

f2 = plt.figure(2)
plt.plot(tlist,result1.expect[1])
plt.title("Time vs Sigmaz 2")
plt.xlabel("Time")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF_28-01-19/Img/RF_Omega_vs_Expectation2.png')

f3 = plt.figure(3)
plt.title("Time vs Sigmaz 3")
plt.xlabel("Time")
plt.ylabel("<sigmaz>")
plt.plot(tlist,result1.expect[2])
plt.savefig('../Output/RF_28-01-19/Img/RF_Omega_vs_Expectation3.png')

f3 = plt.figure(4)
plt.title("Time vs Fidelity 111")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity111)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_111_vs_omega.png')

f3 = plt.figure(5)
plt.title("Time vs Fidelity 110")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity110)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_110_vs_omega.png')

f3 = plt.figure(6)
plt.title("Time vs Fidelity 101")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity101)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_101_vs_omega.png')

f3 = plt.figure(7)
plt.title("Time vs Fidelity 011")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity011)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_011_vs_omega.png')

f3 = plt.figure(8)
plt.title("Time vs Fidelity 100")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity100)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_100_vs_omega.png')

f3 = plt.figure(9)
plt.title("Time vs Fidelity 001")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity001)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_001_vs_omega.png')

f3 = plt.figure(10)
plt.title("Time vs Fidelity 010")
plt.xlabel("Time")
plt.ylabel("Fidelity")
plt.plot(tlist,fidelity010)
plt.savefig('../Output/RF_28-01-19/Img/RF_QuBit_Fidelity_010_vs_omega.png')


f5 = plt.figure(11)
plt.plot(avg_sz1)
plt.plot(avg_sz2)
plt.plot(avg_sz3)
plt.title("Time vs Sigmaz All")
plt.xlabel("Time")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF_28-01-19/Img/RF_Omega_vs_Expectation_ALL.png')
plt.legend(loc='right',fancybox = True, shadow = True)
'''
print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")
'''