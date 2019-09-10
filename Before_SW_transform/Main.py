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

R  		= 1/sqrt(2) * (sigmay() + sigmaz())
R 		= 1
#R3 		= tensor(R,R,R,R)
R3 		=1



one  	= R*basis(2,1)
zero 	= R*basis(2,0)

a 		= sigmap()

q1 		= tensor(a,qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2))
qa 		= tensor(qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2))


#Define variables for the Hamiltonian

pi1 = (1/q1_Bar) * (q1 - q1.dag())
pi2 = (1/q2_Bar) * (q2 - q2.dag())
pi3 = (1/q3_Bar) * (q3 - q3.dag())
pia = (1/sp_Bar) * (qa - qa.dag())


v1 = q1_Bar * (q1 + q1.dag())
v2 = q2_Bar * (q2 + q2.dag())
v3 = q3_Bar * (q3 + q3.dag())
va = sp_Bar * (qa + qa.dag())


#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential

H = [	[8*third*ECQ1*qa*q1,Qa_Q1],[-8*third*ECQ1*qa.dag()*q1,Qad_Q1],[-8*third*ECQ1*qa*q1.dag(),Qa_Q1d],[8*third*ECQ1*qa.dag()*q1.dag(),Qad_Q1d],
		[8*third*ECQ2*qa*q2,Qa_Q2],[-8*third*ECQ2*qa.dag()*q2,Qad_Q2],[-8*third*ECQ2*qa*q2.dag(),Qa_Q2d],[8*third*ECQ2*qa.dag()*q2.dag(),Qad_Q2d],
		[8*third*ECQ3*qa*q3,Qa_Q3],[-8*third*ECQ3*qa.dag()*q3,Qad_Q2],[-8*third*ECQ3*qa*q3.dag(),Qa_Q2d],[8*third*ECQ3*qa.dag()*q3.dag(),Qad_Q2d],
		[-0.25*0.1*EJ*qa*qa,Qa_Qa],[-0.25*0.1*EJ*qa.dag()*qa,no_rotation],[-0.25*0.1*EJ*qa*qa.dag(),no_rotation],[-0.25*0.1*EJ*qa.dag()*qa.dag(),Qad_Qad],
		[-0.5*0.1*EJ*qa,Qa],[-0.5*0.1*EJ*qa.dag(),Qad],

] 

H0 = ECQ1 * pi1 * pi1 + ECQ2 * pi2 * pi2 + ECQ3 * pi3 * pi3 - EJ1 * v1.cosm() - EJ2 * v2.cosm() - EJ3 * v3.cosm() - ECA * pia * pia + 0.1*sixth * ECQ1 * pia * pi1 + \
	+ 0.25*EJ*va*va + 0.0625*EJ*va*va*va*va + 0.028*EJ*va*va
H_cos_22 = [0.25*va*va,[-0.5*va,phie],[0.25,phie2]]
H_cos_24 = [0.0625*va*va*va*va,[-0.25*va*va*va,phie],[0.375*va*va,phie2],[-0.25*va,phie3],[0.0625,phie4]]
H_cos_62 = [0.028*va*va,[-0.056*va,phie],[0.028,phie2]]
#H_Bare = [ H0 ,0.25*va*va,[-0.5*va,phie],[0.25,phie2],0.0625*va*va*va*va,[-0.25*va*va*va,phie],[0.375*va*va,phie2],[-0.25*va,phie3],[0.0625,phie4],0.028*va*va,[-0.056*va,phie],[0.028,phie2]]
H_Bare = [ H0 ,[-0.5*EJ*va,phie],[-0.25*EJ*va*va*va,phie],[0.375*EJ*va*va,phie2],[-0.25*EJ*va,phie3],[-0.056*EJ*va,phie]]
#Now build mesolver varibales

tlist = np.linspace(0,60,num=500)

sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2),qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R,qeye(2))
sx4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2),qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R,qeye(2))
sy4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2),qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R,qeye(2))
sz4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmaz() * R)

c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]

for i in range(2,3):
	if i == 0:
		psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_10-09-19/fidelity000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'			
		outputstr_ocp1 		= 'Output/Toffoli_10-09-19/occupation_q1_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_10-09-19/occupation_q2_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_10-09-19/occupation_q3_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsa 	= 'Output/Toffoli_10-09-19/occupation_sm_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('000 Full Drive')
		result = mesolve(H,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	if i == 1:
		psi0 = tensor(one,one,one,zero);Tdm = tensor(one,one,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_10-09-19/fidelity111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp1 		= 'Output/Toffoli_10-09-19/occupation_q1_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_10-09-19/occupation_q2_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_10-09-19/occupation_q3_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsa		= 'Output/Toffoli_10-09-19/occupation_sm_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('111 Full Drive')
		result = mesolve(H_Bare,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	if i == 2:
		psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_10-09-19/fidelity000-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'			
		outputstr_ocp1 		= 'Output/Toffoli_10-09-19/occupation_q1_000-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_10-09-19/occupation_q2_000-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_10-09-19/occupation_q3_000-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsa 	= 'Output/Toffoli_10-09-19/occupation_sm_000-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('000 Full Drive')
		result = mesolve(H0,psi0,tlist,c_ops,[q1.dag()*q1,q2.dag()*q2,q3.dag()*q3,qa.dag()*qa],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	if i == 3:
		psi0 = tensor(one,one,one,zero);Tdm = tensor(one,one,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_10-09-19/fidelity111-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp1 		= 'Output/Toffoli_10-09-19/occupation_q1_111-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_10-09-19/occupation_q2_111-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_10-09-19/occupation_q3_111-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsa		= 'Output/Toffoli_10-09-19/occupation_sm_111-Bare-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('111 Full Drive')
		result = mesolve(H_Bare,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))

	fidelity_dat 	= []
	occupation_1 	= []
	occupation_2 	= []
	occupation_3 	= []
	occupation_sm	= []

	for j in range(0,len(tlist)):
		fidelity_dat.append(fidelity(result.states[j],Tdm))
		occupation_1.append(result.expect[0][j])
		occupation_2.append(result.expect[1][j])
		occupation_3.append(result.expect[2][j])
		occupation_sm.append(result.expect[3][j])
		with open(outputstr_fid,'w') as file1:
			for j in fidelity_dat:
				file1.write(str(j) + "\n")
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