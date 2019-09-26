'''
Author:Aneirin John Baker	
Date: 11/07/19
Description: Main script within this simulation. It will handle all of the solvers and will hold
all of the Hamiltonian variables and the Hamiltonian itself.It will then pass all of the results onto
another script for that to print all of it out.
'''

#from Constants import *
#from Functions import *
from qutip import *
from math import *
import numpy as np

#Define a complex exponential function
def c_exp(omega,t):
	return (cos(omega * t) + (0 + 1j)*sin(omega*t))
def c_exp_d(omega,t):
	return (cos(omega * t) - (0 + 1j)*sin(omega*t))

#define exponential SINE and COSEIN
def SINE(omega,t):
	return -(0 + 1j) * (c_exp(omega , t) - c_exp_d(omega , t))
def COSINE(omega,t):
	return (c_exp(omega , t) + c_exp_d(omega , t))

#Define a function to return the drive

def driveexp(t):
	'''
	return (-SINE(omega1,t) -SINE(omega2,t) +COSINE(omega3,t) \
		-SINE((omega2 + omega3) , t) -SINE((omega2 - omega3) , t) \
		-SINE((omega1 + omega3) , t) -SINE((omega1 - omega3) , t) \
		-COSINE((omega1 + omega2) , t) + COSINE((omega1 - omega2) , t) \
		- COSINE((omega1 + omega2 + omega3) , t)- COSINE((omega1 + omega2 - omega3) , t) \
		+ COSINE((omega1 - omega2 + omega3) , t) +COSINE((omega1 - omega2 - omega3) , t)) * PI 
	'''
	return COSINE(omega1,t)
def drive(t):
	'''
	return (-sin(omega1*t) - sin(omega2*t) + cos(omega3*t) \
		- sin((omega2 + omega3) * t) - sin((omega2 - omega3) * t) \
		- sin((omega1 + omega3) * t) - sin((omega1 - omega3) * t) \
		- cos((omega1 + omega2) * t) + cos((omega1 - omega2) * t) \
		- cos((omega1 + omega2 + omega3) * t) - cos((omega1 + omega2 - omega3) * t) \
		+ cos((omega1 - omega2 + omega3) * t) + cos((omega1 - omega2 - omega3) * t))* PI 
	'''
	#return -cos((omega1)*t) +sin(omega2*t) + sin((omega1+omega2)*t) + sin((omega1-omega2)*t)
	return cos((omega1)*t)
def doubleDrive(t):
	return cos((omega1+omega2)*t)
	
def pure_single_drive(t,*args):
	return drive(t)
def pure_double_drive(t,*args):
	return doubleDrive(t)
#Define all functions for the rotating Hamiltonian

#Terms for the interaction term
def Qa_Q1(t,*args):
	return c_exp(omega1 + omegaA,t)
def Qad_Q1(t,*args):
	return c_exp(omega1 - omegaA,t)
def Qa_Q1d(t,*args):
	return c_exp_d(omega1 - omegaA,t)
def Qad_Q1d(t,*args):
	return c_exp_d(omega1 + omegaA,t)

def Qa_Q2(t,*args):
	return c_exp(omega2 + omegaA,t)
def Qad_Q2(t,*args):
	return c_exp(omega2 - omegaA,t)
def Qa_Q2d(t,*args):
	return c_exp_d(omega2 - omegaA,t)
def Qad_Q2d(t,*args):
	return c_exp_d(omega2 + omegaA,t)

def Qa_Q3(t,*args):
	return c_exp(omega3 + omegaA,t)
def Qad_Q3(t,*args):
	return c_exp(omega3 - omegaA,t)
def Qa_Q3d(t,*args):
	return c_exp_d(omega3 - omegaA,t)
def Qad_Q3d(t,*args):
	return c_exp_d(omega3 + omegaA,t)

#Drive-SNAIL term

def no_rotation(t,*args):
	return driveexp(t)
def Qa_Qa(t,*args):
	return c_exp(2*omegaA,t) * driveexp(t)
def Qad_Qad(t,*args):
	return c_exp_d(2*omegaA,t) * driveexp(t)
def Qa(t,*args):
	return c_exp(omegaA,t) * driveexp(t)
def Qad(t,*args):
	return c_exp_d(omegaA,t) * driveexp(t)


#Define all of the variables to use 

#R  		= 1/sqrt(2) * (sigmay() + sigmaz())

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

#These energies should have units of frequency
ECQ1	= 1
ECQ2	= 1.5
ECQ3	= 1
EJ1 	= 32
EJ2 	= 25
EJ3 	= 57.8
ECA 	= ECQ1 + ECQ2 + ECQ3
EC 		= 1
#coupling between the qubit and squid
EJ 		= 2
#Drive constants in GHz
omega1 = 4
omega2 = 6
omega3 = 17
omegaA = 30

#Constants for the Hamiltonian
q1_Bar = 0.35
q2_Bar = 0.632
q3_Bar = 0.5
sp_Bar = 1

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

H = [	[ECQ1*qa*q1,Qa_Q1],[ECQ1*qa.dag()*q1,Qad_Q1],[ECQ1*qa*q1.dag(),Qa_Q1d],[ECQ1*qa.dag()*q1.dag(),Qad_Q1d],
		[ECQ2*qa*q2,Qa_Q2],[ECQ2*qa.dag()*q2,Qad_Q2],[ECQ2*qa*q2.dag(),Qa_Q2d],[ECQ2*qa.dag()*q2.dag(),Qad_Q2d],
		[0*qa*q3,Qa_Q3],[0*qa.dag()*q3,Qad_Q3],[0*qa*q3.dag(),Qa_Q3d],[0*qa.dag()*q3.dag(),Qad_Q3d],
		[EJ*qa,Qa],[EJ*qa.dag(),Qad],[EJ * qa.dag()*qa,pure_single_drive]] 


H_single = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2),[0.25*EJ * qa.dag()*qa,pure_single_drive],[EJ*(qa + qa.dag()),pure_single_drive]]

H_double = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2),[0.25*EJ * qa.dag()*qa,pure_double_drive],[EJ*(qa + qa.dag()),pure_double_drive]]


tlist = np.linspace(0,5000,num=1000)

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

#c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]
c_ops =[]
for i in range(0,2):
	if i == 0:
		psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_23-09-19/fidelity_single'+'.dat'			
		outputstr_ocp1 		= 'Output/Toffoli_23-09-19/occupation_q1_single'+'.dat'
		outputstr_ocp2 		= 'Output/Toffoli_23-09-19/occupation_q2_single' + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_23-09-19/occupation_q3_single' + '.dat'
		outputstr_ocpsa 	= 'Output/Toffoli_23-09-19/occupation_sm_single' + '.dat'
		print('000 single Drive')
		result = mesolve(H_single,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	if i == 1:
		psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_23-09-19/fidelity000_double' + '.dat'
		outputstr_ocp1 		= 'Output/Toffoli_23-09-19/occupation_q1_double' + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_23-09-19/occupation_q2_double' + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_23-09-19/occupation_q3_double' + '.dat'
		outputstr_ocpsa		= 'Output/Toffoli_23-09-19/occupation_sm_double' + '.dat'
		print('111 double Drive')
		result = mesolve(H_double,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
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
		'''
		with open(outputstr_fid,'w') as file1:
			for j in fidelity_dat:
				file1.write(str(j) + "\n")
		'''
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
		