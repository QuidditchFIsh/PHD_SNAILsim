
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
Amplitude = 4

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

H1 += 2 * EJT * phi1 * phi2 * phi3

#Prepareing the rest of the calculations
tlist = np.linspace(0, 50, 50)
tlist1 = np.linspace(50, 100, 50)
#Basis states
psi_list = []
psi_list.append(basis(2,0))
for n in range(2):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)

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

eval_op_list = [sz1,sz2,sz3]

Wlist = np.linspace(40,60,20)
Amp_List = np.linspace(1,10,10)
phiBar_List = np.linspace(0.1,1,19)

sigmaz_avgs = []
phi_bar_temp_list = []
PhiBar_Amplitude_Data = []

Hon = [H0,[H1,H1_Coeff_On]]
Hoff = [H0,[H1,H1_Coeff_Off]]

print("Begining Calcultions")
start = time.time()
for i in Amp_List:
	for j in phiBar_List:
		omega = 54
		Amplitude = i
		phibar1 = j

		phi1 = phibar1 * (q1 + q1d)
		phi2 = phibar1 * (q2 + q2d)
		phi3 = phibar1 * (q3 + q3d)

		H0 = 0
		H1 = 0

		H0 += (omega1 * q1d * q1) + (U1 * q1d * q1d * q1 * q1)
		H0 += (omega2 * q2d * q2) + (U2 * q2d * q2d * q2 * q2)
		H0 += (omega3 * q3d * q3) + (U3 * q3d * q3d * q3 * q3)

		H1 += 0.25  * EJT * (phi1 + phi2 - (2 * phi3))**2

		H1 += 2 * EJT * phi1 * phi2 * phi3

		result = mesolve(Hoff,psi0,tlist,c_op_list,eval_op_list,options = Options(store_final_state=True,nsteps = 8000))

		result1 = mesolve(Hon,result.final_state,tlist1,c_op_list,eval_op_list,options = Options(nsteps = 8000))
		sigmaz_avgs.append(np.average(np.real(result1.expect[0])))
		sigmaz_avgs.append(np.average(np.real(result1.expect[1])))
		sigmaz_avgs.append(np.average(np.real(result1.expect[2])))
		phi_bar_temp_list.append(sigmaz_avgs)
		sigmaz_avgs = []
	PhiBar_Amplitude_Data.append(phi_bar_temp_list)
	phi_bar_temp_list = []
	print(i)
end = time.time()
print("Processing Data")
with open("../Output/RF/RF_QuBit_AmpVSPhiBar_1.txt","w") as f:
	for i in range(0,len(Amp_List)):
		for j in range(0,len(phiBar_List)):
			f.write(str(Amp_List[i]) + " " + str(phiBar_List[j]) + " " + str(PhiBar_Amplitude_Data[i][j][0]) + "\n")
with open("../Output/RF/RF_QuBit_AmpVSPhiBar_2.txt","w") as f:
	for i in range(0,len(Amp_List)):
		for j in range(0,len(phiBar_List)):
			f.write(str(Amp_List[i]) + " " + str(phiBar_List[j]) + " " + str(PhiBar_Amplitude_Data[i][j][1]) + "\n")
with open("../Output/RF/RF_QuBit_AmpVSPhiBar_3.txt","w") as f:
	for i in range(0,len(Amp_List)):
		for j in range(0,len(phiBar_List)):
			f.write(str(Amp_List[i]) + " " + str(phiBar_List[j]) + " " + str(PhiBar_Amplitude_Data[i][j][2]) + "\n")
'''
#Processing the basic averages
with open('../Output/RF/RF_QuBit_1_Expect_SZ.txt','w') as f:
	for i in avg_sz1:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_2_Expect_SZ.txt','w') as f:
	for i in avg_sz2:
		f.write(str(i) + "\n")
with open('../Output/RF/RF_QuBit_3_Expect_SZ.txt','w') as f:
	for i in avg_sz3:
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

f5 = plt.figure(5)
plt.plot(avg_sz1)
plt.plot(avg_sz2)
plt.plot(avg_sz3)
plt.title("Omega vs Sigmaz All")
plt.xlabel("Omega")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/RF/Img/RF_Omega_vs_Expectation_ALL.png')
plt.legend(loc='right',fancybox = True, shadow = True)
'''

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")

