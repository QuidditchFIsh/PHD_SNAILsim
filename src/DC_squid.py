'''
Author: Aneirin John Baker
Date : 08/01/2019
Description:First large simulation using QuTip will be following the hamiltonian 
In the main paper as a guide for this. Will then adapt this for the Hamiltonain 
which i have found
'''

import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time

omega = 5
def H1_coeff(t, *args):
	return 1*cos(omega * t)
	#return 0.5
	
def H1_coeff_off(t,*args):
	return 1
print("============================================")
print("Begining Program, setting up calculations")
#
#Setting up the Calculation
#
solver = "me" #use the ode solver for QuTip
#solver = "mc" # Using the monto carlo solver

#This system will be large starting with the smaller one. The small system will
#be the system with a hilbert space of size 2^5 where as the larger on will be 
#3^5 where we check that the excited states of the system are not being populated

N = 2 # Number of states in each sysetm 

q1 = tensor(destroy(N),qeye(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N),qeye(N))
q4 = tensor(qeye(N),qeye(N),qeye(N),destroy(N))


#sP = tensor(qeye(N),qeye(N),qeye(N),qeye(N),destroy(N),qeye(N)) 
#sM = tensor(qeye(N),qeye(N),qeye(N),qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()
q4d = q4.dag()

#sPd = sP.dag()
#sMd = sM.dag()

phi1 = (q1 + q1d)
phi2 = (q2 + q2d)
phi3 = (q3 + q3d)
phi4 = (q4 + q4d)

#Begin construction of the Hamiltonian
H0 = 0

#Begin with H_0q

omega1 = 5
omega2 = 10
omega3 = 15
omega4 = 20

H0 += omega1 * q1d * q1 
H0 += omega2 * q2d * q2 
H0 += omega3 * q3d * q3 
H0 += omega4 * q4d * q4 

#Now the squid part of the Hamiltonian

#H0 +=  omegaP * sPd * sP + omegaM * sMd * sM

# Now the interaction parts of the Hamiltonian


H1 = (1/16) * phi1 * phi2 * phi3 * phi4 
H1 = (-1/8) * (phi1 + phi4 - phi2 - phi3)**2

# Now need to add the driving fields into this so to activate the interactions.



#PRepare the rest of the claculation
tlist = np.linspace(0, 100, 400)
tlist1 = np.linspace(100,200,400)

Wlist = np.linspace(1,50,50)

psi_list = []
psi_list.append(basis(2,0))
for n in range(3):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)

c_op_list = [q1,q2,q3,q4]

#operators to be evaulated
sz1 = tensor(sigmaz(),qeye(N),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz(),qeye(N))
sz4 = tensor(qeye(N),qeye(N),qeye(N),sigmaz())

eval_op_list = [sz1,sz2,sz3,sz4]

H = [H0,[H1,H1_coeff]]
Hoff = [H0,[H1,H1_coeff_off]]

avg_sz1 = []
avg_sz2 = []
avg_sz3 = []
avg_sz4 = []
print("Begining Calcultions")
start = time.time()
for i in Wlist:
	omega = i
	result = mesolve(H0,psi0,tlist,c_op_list,eval_op_list,options = Options(store_final_state=True,nsteps = 8000))

	result1 = mesolve(H,result.final_state,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000))

	avg_sz1.append(np.average(np.real(result1.expect[0])))
	avg_sz2.append(np.average(np.real(result1.expect[1])))
	avg_sz3.append(np.average(np.real(result1.expect[2])))
	avg_sz4.append(np.average(np.real(result1.expect[3])))
end = time.time()
print("Processing Data")
with open('../Output/QuBit_1_Expect_SZ.txt','w') as f:
	for i in avg_sz1:
		f.write(str(i) + "\n")
with open('../Output/QuBit_2_Expect_SZ.txt','w') as f:
	for i in avg_sz2:
		f.write(str(i) + "\n")
with open('../Output/QuBit_3_Expect_SZ.txt','w') as f:
	for i in avg_sz3:
		f.write(str(i) + "\n")
with open('../Output/QuBit_4_Expect_SZ.txt','w') as f:
	for i in avg_sz4:
		f.write(str(i) + "\n")

with open('../Output/QuBit_1_Expect_SZ.txt','r') as f:
	f1 = plt.figure(1)
	plt.plot(Wlist,avg_sz1)
	plt.title("Omega vs Sigmaz 1")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/Img/Omega_vs_Expectation1.png')
with open('../Output/QuBit_2_Expect_SZ.txt','r') as f:
	f2 = plt.figure(2)
	plt.plot(Wlist,avg_sz2)
	plt.title("Omega vs Sigmaz 2")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.savefig('../Output/Img/Omega_vs_Expectation2.png')
with open('../Output/QuBit_3_Expect_SZ.txt','r') as f:
	f3 = plt.figure(3)
	plt.title("Omega vs Sigmaz 3")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.plot(Wlist,avg_sz3)
	plt.savefig('../Output/Img/Omega_vs_Expectation3.png')
with open('../Output/QuBit_4_Expect_SZ.txt','r') as f:
	f4 = plt.figure(4)
	plt.title("Omega vs Sigmaz 4")
	plt.xlabel("Omega")
	plt.ylabel("<sigmaz>")
	plt.plot(Wlist,avg_sz4)
	plt.savefig('../Output/Img/Omega_vs_Expectation4.png')

f5 = plt.figure(5)
plt.plot(avg_sz1)
plt.plot(avg_sz2)
plt.plot(avg_sz3)
plt.plot(avg_sz4)
plt.title("Omega vs Sigmaz All")
plt.xlabel("Omega")
plt.ylabel("<sigmaz>")
plt.savefig('../Output/Img/Omega_vs_Expectation_ALL.png')
plt.legend(loc='right',fancybox = True, shadow = True)

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")


'''
with open('../Output/QuBit_1_Expect_SZ.txt','w') as f:
	for i in result1.expect[0]:
		f.write(str(i) + "\n")
with open('../Output/QuBit_2_Expect_SZ.txt','w') as f:
	for i in result1.expect[1]:
		f.write(str(i) + "\n")
with open('../Output/QuBit_3_Expect_SZ.txt','w') as f:
	for i in result1.expect[2]:
		f.write(str(i) + "\n")
with open('../Output/QuBit_4_Expect_SZ.txt','w') as f:
	for i in result1.expect[3]:
		f.write(str(i) + "\n")

plt.plot(tlist,np.real(result.expect[1]))
plt.plot(tlist1,np.real(result1.expect[1]))
plt.plot(tlist,np.real(result.expect[2]))
plt.plot(tlist1,np.real(result1.expect[2]))
plt.plot(tlist,np.real(result.expect[3]))
plt.plot(tlist1,np.real(result1.expect[3]))
plt.plot(tlist,np.real(result.expect[0]))
plt.plot(tlist1,np.real(result1.expect[0]))
plt.savefig('/home/nye/PhD/QuTIP/Output/Img/expectation_Values.png')
print(np.average(np.real(result1.expect[0])))
print(np.average(np.real(result1.expect[1])))
print(np.average(np.real(result1.expect[2])))
print(np.average(np.real(result1.expect[3])))
'''