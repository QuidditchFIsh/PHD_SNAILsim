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

#R 		= 1/sqrt(2) * (sigmay() + sigmaz())
#R3 		= tensor(R,R,R,R)
R = 1
R3 = 1

one  	=  R*basis(2,1)
zero 	=  R*basis(2,0)

a 		= R*sigmap()*R

q1 		= tensor(a,qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2))
qa 		= tensor(qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2))


#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential
H_triple = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omega3 * q3.dag() * q3 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2) + ECQ3*(-qa.dag()*q3.dag() + qa.dag()*q3 + qa*q3.dag() -qa*q3) \
	 ,[EJ * qa.dag()*qa,pure_triple_drive],[EJ*(qa + qa.dag()),pure_triple_drive]\
	 ,[EJ*(qa.dag()*qa*qa.dag() + qa*qa.dag()*qa),pure_triple_drive]]

tlist = np.linspace(0,5000,num=1000)

#c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]
c_ops =[]
for i in range(0,1):	
	psi0_0 = tensor(zero,zero,zero,zero);Tdm_0 = tensor(zero,zero,zero,zero)
	Tdm_0 = ket2dm(Tdm_0)
	outputstr_fid		= 'Output/Toffoli_03-10-19/Fidelity_000_triple.dat'
	outputstr_ocp1 		= 'Output/Toffoli_03-10-19/occupation_q1_000_triple.dat'
	outputstr_ocp2 		= 'Output/Toffoli_03-10-19/occupation_q2_000_triple.dat'
	outputstr_ocp3 		= 'Output/Toffoli_03-10-19/occupation_q3_000_triple.dat'
	outputstr_ocpsa	 	= 'Output/Toffoli_03-10-19/occupation_qa_000_triple.dat'

	result = mesolve(H_triple,psi0_0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))

	fidelity_dat 	= []
	occupation_1 	= []
	occupation_2 	= []
	occupation_3 	= []
	occupation_sm	= []

	for j in range(0,len(tlist)):
	 	fidelity_dat.append(fidelity(result.states[j],Tdm_0))
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
		with open(outputstr_fid,'w') as file6:
			for j in fidelity_dat:
				file6.write(str(j) + "\n")	