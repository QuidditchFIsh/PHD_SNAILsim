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
import matplotlib.pyplot as plt

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
	return COSINE(_omega1,t)
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
	return cos((_omega1)*t)
def doubleDrive(t):
	return cos((_omega1)*t)
def tripleDrive(t):
	return cos((_omega1+_omega2+_omega3)*t)
	
def pure_single_drive(t,*args):
	return drive(t)
def pure_double_drive(t,*args):
	return doubleDrive(t)
def pure_triple_drive(t,*args):
	return tripleDrive(t)
#Define all functions for the rotating Hamiltonian

#Terms for the interaction term
def Qa_Q1(t,*args):
	return c_exp(omega1 + _omegaA,t)
def Qad_Q1(t,*args):
	return c_exp(_omega1 - _omegaA,t)
def Qa_Q1d(t,*args):
	return c_exp_d(_omega1 - _omegaA,t)
def Qad_Q1d(t,*args):
	return c_exp_d(_omega1 + _omegaA,t)

def Qa_Q2(t,*args):
	return c_exp(_omega2 + _omegaA,t)
def Qad_Q2(t,*args):
	return c_exp(_omega2 - _omegaA,t)
def Qa_Q2d(t,*args):
	return c_exp_d(_omega2 - _omegaA,t)
def Qad_Q2d(t,*args):
	return c_exp_d(_omega2 + _omegaA,t)

def Qa_Q3(t,*args):
	return c_exp(_omega3 + _omegaA,t)
def Qad_Q3(t,*args):
	return c_exp(_omega3 - _omegaA,t)
def Qa_Q3d(t,*args):
	return c_exp_d(_omega3 - _omegaA,t)
def Qad_Q3d(t,*args):
	return c_exp_d(_omega3 + _omegaA,t)

def no_rotation(t,*args):
	return driveexp(t)
def Qa_Qa(t,*args):
	return c_exp(2*_omegaA,t) * driveexp(t)
def Qad_Qad(t,*args):
	return c_exp_d(2*_omegaA,t) * driveexp(t)
def Qa(t,*args):
	return c_exp(_omegaA,t) * driveexp(t)
def Qad(t,*args):
	return c_exp_d(_omegaA,t) * driveexp(t)

def Average(lst):
	return sum(lst)/len(lst)



#Define all of the variables to use 

#R  		= 1/sqrt(2) * (sigmay() + sigmaz())

R 		= 1
#R3 		= tensor(R,R,R,R)
R3 		=1


def simulation(R,R3,ECQ1,ECQ2,ECQ3,EJ,omega1,omega2,omega3,omegaA):
	one  	= R*basis(2,1)
	zero 	= R*basis(2,0)

	a 		= sigmap()

	q1 		= tensor(a,qeye(2),qeye(2),qeye(2))
	q2		= tensor(qeye(2),a,qeye(2),qeye(2))
	q3 		= tensor(qeye(2),qeye(2),a,qeye(2))
	qa 		= tensor(qeye(2),qeye(2),qeye(2),a)

	I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2))

	#These energies should have units of frequency
	#ECQ1	= 1
	#ECQ2	= 1.5
	#ECQ3	= 1
	#coupling between the qubit and squid
	#EJ 		= 2
	#Drive constants in GHz
	#omega1 = 4
	#omega2 = 6
	#omega3 = 17
	#omegaA = 30



	#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
	#First terms in the SQUID potential

	H = [	[ECQ1*qa*q1,Qa_Q1],[ECQ1*qa.dag()*q1,Qad_Q1],[ECQ1*qa*q1.dag(),Qa_Q1d],[ECQ1*qa.dag()*q1.dag(),Qad_Q1d],
			[ECQ2*qa*q2,Qa_Q2],[ECQ2*qa.dag()*q2,Qad_Q2],[ECQ2*qa*q2.dag(),Qa_Q2d],[ECQ2*qa.dag()*q2.dag(),Qad_Q2d],
			[0*qa*q3,Qa_Q3],[0*qa.dag()*q3,Qad_Q3],[0*qa*q3.dag(),Qa_Q3d],[0*qa.dag()*q3.dag(),Qad_Q3d],
			[EJ*qa,Qa],[EJ*qa.dag(),Qad],[EJ * qa.dag()*qa,pure_single_drive]] 


	H_single = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2),[0.25*EJ * qa.dag()*qa,pure_single_drive],[EJ*(qa + qa.dag()),pure_single_drive]]

	H_double = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2),[0.25*EJ * qa.dag()*qa,pure_single_drive],[EJ*(qa + qa.dag()),pure_single_drive]]

	H_triple = [omega1 * q1.dag() * q1 + omega2 * q2.dag() * q2 + omega3 * q3.dag() * q3 + omegaA * qa.dag() * qa + ECQ1*(-qa.dag()*q1.dag() + qa.dag()*q1 + qa*q1.dag() -qa*q1)\
	 + ECQ2*(-qa.dag()*q2.dag() + qa.dag()*q2 + qa*q2.dag() -qa*q2)  + ECQ3*(-qa.dag()*q3.dag() + qa.dag()*q3 + qa*q3.dag() -qa*q3)\
	 ,[EJ * qa.dag()*qa,pure_double_drive],[EJ*(qa + qa.dag()),pure_double_drive],[0.5 * EJ * (qa*qa.dag()*qa + qa.dag()*qa*qa.dag()),pure_triple_drive]]


	tlist = np.linspace(0,500,num=500)

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

	c_ops =[]
	psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
	Tdm = ket2dm(Tdm)
	print('000 single Drive')
	result = mesolve(H_double,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*qa.dag()*qa*R3],options = Options(nsteps = 20000,store_states = True,store_final_state = True))
	return result

_omega1 		= 5
_omega2 		= 13
_omega3 		= 7
_omegaA 		= 87

_R 				= 1
_R3 			= 1

max_oocupation 	= []

T = np.linspace(0,2000,num=500)

output_str 		= 'Output/Toffoli_27-09-19/Max_occupation_omega.dat'
with open(output_str,'w') as file2:
	for i in range(1,2):
		for j in range(1,80):
			_ECQ1 	= 5.5
			_ECQ2 	= 13.5
			_ECQ3 	= 5.5 

			_EJ 	= 19.5
			_omega1 		= j*0.25
			print(str(i) + " " + str(j) + "\n")
			res = simulation(_R,_R3,_ECQ1,_ECQ2,_ECQ3,_EJ,5,13,70,87)
			plt.ylim(0,1)
			plt.plot(T,res.expect[0])
			plt.savefig("Output/Toffoli_27-09-19/ImgW1/ECQ_"+str(i*0.5)+"_EJ_"+str(j*0.5)+".png")
			plt.clf()
			plt.ylim(0,1)
			plt.plot(T,res.expect[1])
			plt.savefig("Output/Toffoli_27-09-19/ImgW2/ECQ_"+str(i*0.5)+"_EJ_"+str(j*0.5)+".png")
			plt.clf()
			plt.ylim(0,1)
			plt.plot(T,res.expect[2])
			plt.savefig("Output/Toffoli_27-09-19/ImgWA/ECQ_"+str(i*0.5)+"_EJ_"+str(j*0.5)+".png")
			plt.clf()

			file2.write(str(i*0.5) + " " + str(j*0.5) + " " + str((max(res.expect[0]))) + " " + str(max(res.expect[1])) + " " + str(Average(res.expect[2])) + "\n")