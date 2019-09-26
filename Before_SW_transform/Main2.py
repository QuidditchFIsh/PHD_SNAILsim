'''
Author:Aneirin John Baker	
Date: 11/07/19
Description: Main script within this simulation. It will handle all of the solvers and will hold
all of the Hamiltonian variables and the Hamiltonian itself.It will then pass all of the results onto
another script for that to print all of it out.
'''

from Constants import *
from Functions import *
from qutip import *
from math import *
import numpy as np

#Define all of the variables to use 



one  	= basis(2,1)
zero 	= basis(2,0)

a 		= sigmap()

q1 		= tensor(a,qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2))
qa 		= tensor(qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2))



#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential

H = [	[-ECQ1*qa*q1,Qa_Q1],[ECQ1*qa.dag()*q1,Qad_Q1],[ECQ1*qa*q1.dag(),Qa_Q1d],[-ECQ1*qa.dag()*q1.dag(),Qad_Q1d],
		[-ECQ2*qa*q2,Qa_Q2],[ECQ2*qa.dag()*q2,Qad_Q2],[ECQ2*qa*q2.dag(),Qa_Q2d],[-ECQ2*qa.dag()*q2.dag(),Qad_Q2d],
		[-ECQ3*qa*q3,Qa_Q3],[ECQ3*qa.dag()*q3,Qad_Q3],[ECQ3*qa*q3.dag(),Qa_Q3d],[-ECQ3*qa.dag()*q3.dag(),Qad_Q3d],
		[EJ*qa.dag()*qa,no_rotation],[EJ*qa,Qa],[EJ*qa.dag(),Qad]] 

tlist = np.linspace(0,3000,num=3000)

#c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]
c_ops =[]
for i in range(0,1):	
	psi0 = tensor(zero,zero,zero,zero)
	omegad=4.0
	outputstr_ocp1 		= 'Output/Toffoli_18-09-19/occupation_q1_000-' + str(omegad) + '.dat'
	outputstr_ocp2 		= 'Output/Toffoli_18-09-19/occupation_q2_000-' + str(omegad) + '.dat'
	outputstr_ocp3 		= 'Output/Toffoli_18-09-19/occupation_q3_000-' + str(omegad) + '.dat'
	outputstr_ocpsa 	= 'Output/Toffoli_18-09-19/occupation_sm_000-' + str(omegad) + '.dat'
	print(omegad)
	result = mesolve(H,psi0,tlist,c_ops,[q1.dag()*q1,q2.dag()*q2,q3.dag()*q3,qa.dag()*qa],options = Options(nsteps = 20000,store_states = True,store_final_state = True))

	fidelity_dat 	= []
	occupation_1 	= []
	occupation_2 	= []
	occupation_3 	= []
	occupation_sm	= []

	for j in range(0,len(tlist)):
		occupation_1.append(result.expect[0][j])
		occupation_2.append(result.expect[1][j])
		occupation_3.append(result.expect[2][j])
		occupation_sm.append(result.expect[3][j])

		with open(outputstr_ocp1,'w') as file2:
			for j in occupation_1:
				file2.write(str(j) + "\n")
		with open(outputstr_ocp2,'w') as file3:
			for j in occupation_2:
				file3.write(str(j) + "\n")
		with open(outputstr_ocp3,'w') as file4:
			for j in occupation_3:
				file4.write(str(j) + "\n")
		with open(outputstr_ocpsa,'w') as file5:
			for j in occupation_sm:
				file5.write(str(j) + "\n")
		