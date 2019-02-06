import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('Error:Creating Directory. ' + directory)

#Set up the equations
def H1_Coeff_On(t,*args):
	'''
	return (0.125 * cos((cons.omega1) * t) + 0.125 * cos((cons.omega2) * t) - 0.125 * cos((cons.omega3) * t)
	+ 0.0625 * cos((cons.omega1 + cons.omega2) * t) + 0.0625 * cos((cons.omega1 - cons.omega2) * t) - 0.0625 * cos((cons.omega1 + cons.omega3) * t)
	- 0.0625 * cos((cons.omega1 - cons.omega3) * t) - 0.0625 * cos((cons.omega2 + cons.omega3) * t) - 0.0625 * cos((cons.omega2 - cons.omega3) * t)
	- 0.03125 * cos((cons.omega1 + cons.omega2 + cons.omega3) * t) - 0.03125 * cos((- cons.omega1 + cons.omega2 + cons.omega3) * t) 
	- 0.03125 * cos((cons.omega1 - cons.omega2 + cons.omega3) * t) - 0.03125 * cos((cons.omega1 + cons.omega2 - cons.omega3) * t))
	
	return (0.75 + 0.25 * cos((cons.omega1) * t) + 0.25 * cos((cons.omega2) * t) + 0.25 * cos((cons.omega3) * t)
	+ 0.25 * cos((cons.omega1 + cons.omega2) * t) + 0.25 * cos((cons.omega1 - cons.omega2) * t) + 0.25 * cos((cons.omega1 + cons.omega3) * t)
	+ 0.25 * cos((cons.omega1 - cons.omega3) * t) + 0.25 * cos((cons.omega2 + cons.omega3) * t) + 0.25 * cos((cons.omega2 - cons.omega3) * t)
	+ 0.25 * cos((cons.omega1 + cons.omega2 + cons.omega3) * t) + 0.25 * cos((- cons.omega1 + cons.omega2 + cons.omega3) * t) 
	+ 0.25 * cos((cons.omega1 - cons.omega2 + cons.omega3) * t) + 0.25 * cos((cons.omega1 + cons.omega2 - cons.omega3) * t))
	'''
	return cos((cons.omega1 - cons.omega2 + cons.omega3) * t )
print("============================================")
print("Begining Program, setting up calculations")
time_start = datetime.datetime.now()
print("Identifier :" + str(time_start))
#Define the Variables
N = 2 # Number of states in the system

avg_sz1 = []#Average sigma z value for each QuBit
avg_sz2 = []
avg_sz3 = []

tempfid111 = []
tempfid110 = []
tempfid101 = []
tempfid011 = []
tempfid100 = []
tempfid010 = []
tempfid001 = []
tempfid000 = []

temp_sz1 = []
temp_sz2 = []
temp_sz3 = []

psi_list = []


#Define the operators 
q1 = tensor(destroy(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()

#Define the Target Density Matricies
one  = basis(2,1)
zero = basis(2,0)

psi0 = tensor(zero,one,zero)

Tdm_111 = tensor(one ,one ,one  )
Tdm_110 = tensor(one ,one ,zero )
Tdm_101 = tensor(one ,zero,one  )
Tdm_011 = tensor(zero,one ,one  )
Tdm_100 = tensor(one ,zero,zero )
Tdm_001 = tensor(zero,zero,one  )
Tdm_010 = tensor(zero,one ,zero )
Tdm_000 = tensor(zero,zero,zero )

sz1 = tensor(sigmaz(),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz())


#operators to be evaluated and collapse operators
eval_op_list = [q1 * q1.dag(),q2 * q2.dag(),q3 * q3.dag()]
c_op_list = [0.05*q1,0.05*q2,0.05*q3]

tlist = np.linspace(0, 300, 1000)

#import the data

input = []
print("Begining Calcultions")
start = time.time()
with open('gen_freq/Optimization_Output.dat','r') as f:
	for line in f:
		input = line.split()
input = [float(i) for i in input]

Notrials = len(input) / 9

for i in range(0,Notrials):#Ignore the odd for loop and the input stuff this is just how i get the parameters into the simulation (from the optimization routines)
	#set all the simulation parameters
	cons.omega1 = input[(i*9) + 0]
	cons.omega2 = input[(i*9) + 3]
	cons.omega3 = input[(i*9) + 6]

	cons.ECQ1 = cons.E_CQ(input[(i*9) + 2])
	cons.ECQ2 = cons.E_CQ(input[(i*9) + 5])
	cons.ECQ3 = cons.E_CQ(input[(i*9) + 8])

	cons.EJ1 = cons.E_J(input[(i*9) + 1])
	cons.EJ2 = cons.E_J(input[(i*9) + 4])
	cons.EJ3 = cons.E_J(input[(i*9) + 7])

	cons.U1 = cons.calc_U(cons.ECQ1,cons.EJ1,cons.EL)
	cons.U2 = cons.calc_U(cons.ECQ2,cons.EJ2,cons.EL)
	cons.U3 = cons.calc_U3(cons.ECQ3,cons.EJ3,cons.EL)

	#cons.U1 = 0
	#cons.U2 = 0
	#cons.U3 = 0


	cons.phibar1 = cons.calc_phiBar(cons.ECQ1,cons.EJ1,cons.EL)
	cons.phibar2 = cons.calc_phiBar(cons.ECQ2,cons.EJ2,cons.EL)
	cons.phibar3 = cons.calc_phiBar3(cons.ECQ3,cons.EJ3,cons.EL)
	
	phi1 = cons.phibar1 * (q1 + q1d)
	phi2 = cons.phibar2 * (q2 + q2d)
	phi3 = cons.phibar3 * (q3 + q3d)
 	#Reset all of the hamiltonians 
 	H0 = 0
 	H1 = 0
 	H0 += (cons.omega1 * q1d * q1) + (cons.U1 * q1d * q1d * q1 * q1)
	H0 += (cons.omega2 * q2d * q2) + (cons.U2 * q2d * q2d * q2 * q2)
	H0 += (cons.omega3 * q3d * q3) + (cons.U3 * q3d * q3d * q3 * q3)

	H1 += 1  * cons.EJT * (phi1 + phi2 + (phi3))**2

	H1 += 1 * cons.EJT * phi1 * phi2 * phi3
	
	H = [H0,[H1,H1_Coeff_On]]
	#print(H0)
	#print(H1)
 	result = mesolve(H,psi0,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_states = True))
 	#Will now need to measure and store the results

 	for j in range(0,len(tlist)):
 		tempfid111.append(fidelity(result.states[j],Tdm_111))
 		tempfid110.append(fidelity(result.states[j],Tdm_110))
 		tempfid101.append(fidelity(result.states[j],Tdm_101))
 		tempfid011.append(fidelity(result.states[j],Tdm_011))
 		tempfid100.append(fidelity(result.states[j],Tdm_100))
  		tempfid010.append(fidelity(result.states[j],Tdm_010))
  		tempfid001.append(fidelity(result.states[j],Tdm_001))
   		tempfid000.append(fidelity(result.states[j],Tdm_000))
   	for j in range(0,len(tlist)):
  		temp_sz1.append(np.real(result.expect[0][j]))
  		temp_sz2.append(np.real(result.expect[1][j]))
  		temp_sz3.append(np.real(result.expect[2][j]))

  	strength = cons.phibar1 * cons.phibar2 * cons.phibar3
  	print(str(strength) + ' ' + str(i))

	Folder_Path = '../Output/RF_05-02-19/' + str(time_start)

  	createFolder(Folder_Path + "_" + str(i))

  	with open(Folder_Path + "_" + str(i) + '/Fidelity111.txt','w') as f1:
		for j in tempfid111:
			f1.write(str(j) + "\n")
	f1.close()
  	with open(Folder_Path + "_" + str(i) + '/Fidelity110.txt','w') as f2:
		for j in tempfid110:
			f2.write(str(j) + "\n")
	f2.close()
	with open(Folder_Path  + "_" + str(i) + '/Fidelity101.txt','w') as f3:
		for j in tempfid101:
			f3.write(str(j) + "\n")
	f3.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity011.txt','w') as f4:
		for j in tempfid011:
			f4.write(str(j) + "\n")
	f4.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity100.txt','w') as f5:
		for j in tempfid100:
			f5.write(str(j) + "\n")
	f5.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity010.txt','w') as f6:
		for j in tempfid010:
			f6.write(str(j) + "\n")
	f6.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity001.txt','w') as f7:
		for j in tempfid001:
			f7.write(str(j) + "\n")
	f7.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity000.txt','w') as f11:
		for j in tempfid000:
			f11.write(str(j) + "\n")
	f11.close()
  	with open(Folder_Path  + "_" + str(i) + '/expect_sz1.txt','w') as f8:
		for j in temp_sz1:
			f8.write(str(j) + "\n")
	f8.close()
  	with open(Folder_Path  + "_" + str(i) + '/expect_sz2.txt','w') as f9:
		for j in temp_sz2:
			f9.write(str(j) + "\n")
	f9.close()
  	with open(Folder_Path  + "_" + str(i) + '/expect_sz3.txt','w') as f10:
		for j in temp_sz3:
			f10.write(str(j) + "\n")
	f10.close()
	with open(Folder_Path +"_" + str(i) + '/Simulation_Run_Data.dat','w') as f12:
		f12.write(str(cons.omega1) + " w1 \n")
		f12.write(str(cons.omega2) + " w2 \n")
		f12.write(str(cons.omega3) + " w3 \n")
		f12.write(str(cons.omega1 + cons.omega2) + " w1 + w2\n")
		f12.write(str(cons.omega1 - cons.omega2) + " w1 - w2\n")
		f12.write(str(cons.omega1 + cons.omega3) + " w1 + w3\n")
		f12.write(str(cons.omega1 - cons.omega3) + " w1 - w3\n")
		f12.write(str(cons.omega2 + cons.omega3) + " w2 + w3\n")
		f12.write(str(cons.omega2 - cons.omega3) + " w2 - w3\n")
		f12.write(str(cons.omega1 + cons.omega2 + cons.omega3) + " w1 + w2 + w3\n")
		f12.write(str(cons.omega1 + cons.omega2 - cons.omega3) + " w1 + w2 - w3\n")
		f12.write(str(cons.omega1 - cons.omega2 + cons.omega3) + " w1 - w2 + w3\n")
		f12.write(str(-cons.omega1 + cons.omega2 + cons.omega3) + "-w1 + w2 + w3\n \n")

		f12.write("w1=" + str(cons.omega1) + "\n")
		f12.write("w2=" + str(cons.omega2) + "\n")
		f12.write("w3=" + str(cons.omega3) + "\n")
		f12.write("U1=" + str(cons.U1) + "\n")
		f12.write("U2=" + str(cons.U2) + "\n")
		f12.write("U3=" + str(cons.U3) + "\n")

	tempfid111 = []
	tempfid110 = []
	tempfid101 = []
	tempfid011 = []
	tempfid100 = []
	tempfid010 = []
	tempfid001 = []
	tempfid000 = []

	temp_sz1 = []
	temp_sz2 = []
	temp_sz3 = []

end = time.time()

print("============================================")
print("Time Ellapsed:" + str(end-start))
print("============================================")
