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

R 		= 1/sqrt(2) * (sigmay() + sigmaz())
R3 		= tensor(R,R,R)
#R3 = 1

one  	=  R*basis(2,1)
zero 	=  R*basis(2,0)

a 		= R*sigmap()*R
'''
q1 		= tensor(a,qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2))
qa 		= tensor(qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2))
'''
q1 		= tensor(a,qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2))
qa 		= tensor(qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2))


#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential
'''
H = [	[-ECQ1*qa*q1,Qa_Q1],[ECQ1*qa.dag()*q1,Qad_Q1],[ECQ1*qa*q1.dag(),Qa_Q1d],[-ECQ1*qa.dag()*q1.dag(),Qad_Q1d],
		[-ECQ2*qa*q2,Qa_Q2],[ECQ2*qa.dag()*q2,Qad_Q2],[ECQ2*qa*q2.dag(),Qa_Q2d],[-ECQ2*qa.dag()*q2.dag(),Qad_Q2d],
		[-ECQ3*qa*q3,Qa_Q3],[ECQ3*qa.dag()*q3,Qad_Q3],[ECQ3*qa*q3.dag(),Qa_Q3d],[-ECQ3*qa.dag()*q3.dag(),Qad_Q3d],
		[EJ*qa.dag()*qa,no_rotation],[EJ*qa,Qa],[EJ*qa.dag(),Qad]] 
'''
H_single = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2) \
	 ,[0.25*EJ * qa.dag()*qa,pure_single_drive],[EJ*(qa + qa.dag()),pure_single_drive]\
	 ,[0.125*EJ*(qa.dag()*qa*qa.dag() + qa*qa.dag()*qa),pure_single_drive]]
	 #,[EJ*(qa+qa.dag()).sinm(),pure_single_drive],[EJ*(qa+qa.dag()).cosm(),pure_single_drive]]

H_double = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2)\
	 ,[0.25*EJ * qa.dag()*qa,pure_double_drive],[EJ*(qa + qa.dag()),pure_double_drive]\
	 ,[-0*EJ*(qa.dag()*qa*qa.dag() + qa*qa.dag()*qa),pure_double_drive]]
	 #,[EJ*(qa+qa.dag()).sinm(),pure_single_drive],[EJ*(qa+qa.dag()).cosm(),pure_single_drive]]

tlist = np.linspace(0,500,num=500)

#c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]
c_ops =[]
for i in range(0,1):	
	psi0_0 = tensor(one,one,zero);Tdm_0 = tensor(one,zero,zero)
	psi0_1 = tensor(zero,zero,zero);Tdm_1 = tensor(zero,zero,zero)
	Tdm_0 = ket2dm(Tdm_0);Tdm_1 = ket2dm(Tdm_1)
	outputstr_fid_single 		= 'Output/Toffoli_03-10-19/Fidelity_000-single.dat'
	outputstr_ocp1_single 		= 'Output/Toffoli_03-10-19/occupation_q1_000-single.dat'
	outputstr_ocp2_single 		= 'Output/Toffoli_03-10-19/occupation_q2_000-single.dat'
	outputstr_ocp3_single 		= 'Output/Toffoli_03-10-19/occupation_q3_000-single.dat'
	outputstr_ocpsa_single	 	= 'Output/Toffoli_03-10-19/occupation_qa_000-single.dat'

	outputstr_fid_double 		= 'Output/Toffoli_03-10-19/Fidelity_000-double.dat'
	outputstr_ocp1_double 		= 'Output/Toffoli_03-10-19/occupation_q1_000-double.dat'
	outputstr_ocp2_double 		= 'Output/Toffoli_03-10-19/occupation_q2_000-double.dat'
	outputstr_ocp3_double 		= 'Output/Toffoli_03-10-19/occupation_q3_000-double.dat'
	outputstr_ocpsa_double	 	= 'Output/Toffoli_03-10-19/occupation_qa_000-double.dat'

	result = mesolve(H_single,psi0_0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	result1 = mesolve(H_single,psi0_1,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))

	fidelity_dat_single 	= []
	occupation_1_single 	= []
	occupation_2_single 	= []
	occupation_3_single 	= []
	occupation_sm_single	= []

	fidelity_dat_double 	= []
	occupation_1_double 	= []
	occupation_2_double 	= []
	occupation_3_double 	= []
	occupation_sm_double	= []

	for j in range(0,len(tlist)):
	 	fidelity_dat_single.append(fidelity(result.states[j],Tdm_0))
		occupation_1_single.append(result.expect[0][j])
		occupation_2_single.append(result.expect[1][j])
		#occupation_3_single.append(result.expect[2][j])
		occupation_sm_single.append(result.expect[2][j])

		fidelity_dat_double.append(fidelity(result1.states[j],Tdm_1))
		occupation_1_double.append(result1.expect[0][j])
		occupation_2_double.append(result1.expect[1][j])
		#occupation_3_double.append(result1.expect[2][j])
		occupation_sm_double.append(result1.expect[2][j])

		with open(outputstr_ocp1_single,'w') as file2:
			for j in occupation_1_single:
				file2.write(str(j) + "\n")
		with open(outputstr_ocp2_single,'w') as file3:
			for j in occupation_2_single:
				file3.write(str(j) + "\n")
		'''
		with open(outputstr_ocp3_single,'w') as file4:
			for j in occupation_3_single:
				file4.write(str(j) + "\n")
		'''		
		with open(outputstr_ocpsa_single,'w') as file5:
			for j in occupation_sm_single:
				file5.write(str(j) + "\n")
		with open(outputstr_fid_single,'w') as file6:
			for j in fidelity_dat_single:
				file6.write(str(j) + "\n")	

		with open(outputstr_ocp1_double ,'w') as file7:
			for j in occupation_1_double:
				file7.write(str(j) + "\n")
		with open(outputstr_ocp2_double ,'w') as file8:
			for j in occupation_2_double:
				file8.write(str(j) + "\n")
		'''		
		with open(outputstr_ocp3_double ,'w') as file9:
			for j in occupation_3_double:
				file9.write(str(j) + "\n")
		'''		
		with open(outputstr_ocpsa_double ,'w') as file10:
			for j in occupation_sm_double:
				file10.write(str(j) + "\n")
		with open(outputstr_fid_double,'w') as file11:
			for j in fidelity_dat_double:
				file11.write(str(j) + "\n")	
