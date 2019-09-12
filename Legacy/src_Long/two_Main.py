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
	
	#return 4*(0.125 * cos((cons.omega1) * t) + 0.125 * cos((cons.omega2) * t) - 0.125 * cos((cons.omega3) * t)
	#+ 0.0625 * cos((cons.omega1 + cons.omega2) * t) + 0.0625 * cos((cons.omega1 - cons.omega2) * t) - 0.0625 * cos((cons.omega1 + cons.omega3) * t)
	#- 0.0625 * cos((cons.omega1 - cons.omega3) * t) - 0.0625 * cos((cons.omega2 + cons.omega3) * t) - 0.0625 * cos((cons.omega2 - cons.omega3) * t)
	#- 0.03125 * cos((cons.omega1 + cons.omega2 + cons.omega3) * t) - 0.03125 * cos((- cons.omega1 + cons.omega2 + cons.omega3) * t) 
	#- 0.03125 * cos((cons.omega1 - cons.omega2 + cons.omega3) * t) - 0.03125 * cos((cons.omega1 + cons.omega2 - cons.omega3) * t))
	
	#return (0.25 * cos((cons.omega1) * t) + 0.25 * cos((cons.omega2) * t) - 0.25 * cos((cons.omega3) * t)
	#+ 0.25 * cos((cons.omega1 + cons.omega2) * t) + 0.25 * cos((cons.omega1 - cons.omega2) * t) - 0.25 * cos((cons.omega1 + cons.omega3) * t)
	#- 0.25 * cos((cons.omega1 - cons.omega3) * t) - 0.25 * cos((cons.omega2 + cons.omega3) * t) - 0.25 * cos((cons.omega2 - cons.omega3) * t)
	#- 0.25 * cos((cons.omega1 + cons.omega2 + cons.omega3) * t) - 0.25 * cos((- cons.omega1 + cons.omega2 + cons.omega3) * t) 
	#- 0.25 * cos((cons.omega1 - cons.omega2 + cons.omega3) * t) - 0.25 * cos((cons.omega1 + cons.omega2 - cons.omega3) * t))
	
	#return -0.5*cos((cons.omega1 - cons.omega3) * t ) - 0.5*cos((cons.omega1 + cons.omega3) * t ) - cos(cons.omega1 * t) - cos(cons.omega3 * t)
	return cos(cons.omega1 * t)
print("============================================")
print("Begining Program, setting up calculations")
time_start = datetime.datetime.now()
print("Identifier :" + str(time_start))
#Define the Variables
N = 2 # Number of states in the system

avg_sz1 = []#Average sigma z value for each QuBit
avg_sz2 = []
avg_sz3 = []

tempfid11 = []
tempfid10 = []
tempfid01 = []
tempfid011 = []
tempfid00 = []
tempfid010 = []
tempfid001 = []
tempfid000 = []

temp_sz1 = []
temp_sz2 = []
temp_sz3 = []

psi_list = []


#Define the Rotation matrix for this simulation

#R = 1/sqrt(2) * (sigmaz() + sigmay())
R =1
a = R * destroy(2) * R

#Define the operators 
q1 = tensor(a,qeye(N))
q3 = tensor(qeye(N),a)
q2 = tensor(qeye(N),qeye(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()

#Define the Target Density Matricies
one  = R * basis(2,1)
zero = R * basis(2,0)
#one  = 1/sqrt(2) * (basis(2,0) + (0 + 1j)*basis(2,1))
#zero = 1/sqrt(2) * (basis(2,0) - (0 + 1j)*basis(2,1))
#one = basis(2,1)
#zero = basis(2,0)

psi0 = tensor(one,one)

Tdm_11 = tensor(one ,one )
Tdm_10 = tensor(one ,zero  )
Tdm_01 = tensor(zero,one   )
Tdm_00 = tensor(zero,zero  )

sz1 = tensor(sigmay(),qeye(N))
sz2 = tensor(qeye(N),sigmay())



#operators to be evaluated and collapse operators
eval_op_list = [q1 * q1.dag(),q3 * q3.dag()]
c_op_list = [0.005*q1,0.005*q2,0.01 * sz1,0.01 * sz2]

tlist = np.linspace(0, 5000, 2000)

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
	cons.omega3 = input[(i*9) + 3]
	cons.omega2 = input[(i*9) + 6]

	cons.ECQ1 = cons.E_CQ(input[(i*9) + 2])
	cons.ECQ2 = cons.E_CQ(input[(i*9) + 5])
	cons.ECQ3 = cons.E_CQ(input[(i*9) + 8])

	cons.EJ1 = cons.E_J(input[(i*9) + 1])
	cons.EJ2 = cons.E_J(input[(i*9) + 4])
	cons.EJ3 = cons.E_J(input[(i*9) + 7])

	#cons.U1 = cons.calc_U(cons.ECQ1,cons.EJ1,cons.EL)
	#cons.U2 = cons.calc_U(cons.ECQ2,cons.EJ2,cons.EL)
	#cons.U3 = cons.calc_U3(cons.ECQ3,cons.EJ3,cons.EL)

	cons.U1 = 0
	cons.U2 = 0
	cons.U3 = 0


	cons.phibar1 = cons.calc_phiBar(cons.ECQ1,cons.EJ1,cons.EL)
	cons.phibar2 = cons.calc_phiBar(cons.ECQ2,cons.EJ2,cons.EL)
	cons.phibar3 = cons.calc_phiBar3(cons.ECQ3,cons.EJ3,cons.EL)
	
	#phi1 = cons.phibar1 * (q1 + q1d)
	#phi2 = cons.phibar2 * (q2 + q2d)
	#phi3 = cons.phibar3 * (q3 + q3d)

	phi1 = (q1 + q1d)
	phi2 = (q2 + q2d)
	phi3 = (q3 + q3d)

 	#Reset all of the hamiltonians 
 	H0 = 0
 	H1 = 0
 	H0 += (cons.omega1 * q1d * q1) + (cons.U1 * q1d * q1d * q1 * q1)
	#H0 += (cons.omega2 * q2d * q2) + (cons.U2 * q2d * q2d * q2 * q2)
	H0 += (cons.omega3 * q3d * q3) + (cons.U3 * q3d * q3d * q3 * q3)

	H1 += 0.05  * cons.EJT * (phi1 + phi3)**2

	#H1 += 1 * cons.EJT * phi1 * phi2 * phi3
	
	H = [H0,[H1,H1_Coeff_On]]
	#print(H0)
	#print(H1)
 	result = mesolve(H,psi0,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_states = True))
 	#Will now need to measure and store the results

 	for j in range(0,len(tlist)):
 		tempfid11.append(fidelity(result.states[j],Tdm_11))
 		tempfid10.append(fidelity(result.states[j],Tdm_10))
 		tempfid01.append(fidelity(result.states[j],Tdm_01))
 		tempfid00.append(fidelity(result.states[j],Tdm_00))

   	for j in range(0,len(tlist)):
  		temp_sz1.append(np.real(result.expect[0][j]))
  		temp_sz2.append(np.real(result.expect[1][j]))
  		#temp_sz3.append(np.real(result.expect[2][j]))

  	strength = cons.phibar1 * cons.phibar2 * cons.phibar3
  	print(str(strength) + ' ' + str(i))

	Folder_Path = '../Output/RF_12-02-19/' + str(time_start)

  	createFolder(Folder_Path + "_" + str(i))

  	with open(Folder_Path +"_" + str(i) + '/Fidelity11.txt','w') as f1:
		for j in tempfid11:
			f1.write(str(j) + "\n")
	f1.close()
  	with open(Folder_Path + "_" + str(i) + '/Fidelity10.txt','w') as f2:
		for j in tempfid10:
			f2.write(str(j) + "\n")
	f2.close()
	with open(Folder_Path  + "_" + str(i) + '/Fidelity01.txt','w') as f3:
		for j in tempfid01:
			f3.write(str(j) + "\n")
	f3.close()
  	with open(Folder_Path  + "_" + str(i) + '/Fidelity00.txt','w') as f4:
		for j in tempfid00:
			f4.write(str(j) + "\n")
	f4.close()
  	with open(Folder_Path  + "_" + str(i) + '/expect_sz1.txt','w') as f8:
		for j in temp_sz1:
			f8.write(str(j) + "\n")
	f8.close()
  	with open(Folder_Path  + "_" + str(i) + '/expect_sz2.txt','w') as f9:
		for j in temp_sz2:
			f9.write(str(j) + "\n")
	f9.close()
	with open(Folder_Path +"_" + str(i) + '/Simulation_Run_Data.dat','w') as f12:
		f12.write(str(cons.omega1) + " w1 \n")
		f12.write(str(cons.omega2) + " w2 \n")
		f12.write(str(cons.omega3) + " w3 \n")
		f12.write(str(cons.omega1 + cons.omega2) + " w1 + w2\n")
		f12.write(str(cons.omega1 - cons.omega2) + " w1 - w2\n")


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
