'''
Author:Aneirin John Baker
Date:11/07/19
Description:Script used to store all of the functions for generating the drive.
'''

from Constants import *
from math import *

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
	return -1*cos((omega2)*t) + sin(omega1*t) + sin((omega1+omega2)*t) + sin((omega1-omega2)*t)
def doubleDrive(t):
	return cos((omega1 + omega2)*t)
def tripleDrive(t):
	return cos((omega1 + omega2 + 0) * t)
	
def pure_single_drive(t,*args):
	return drive(t)
def pure_double_drive(t,*args):
	return doubleDrive(t)
def pure_triple_drive(t,*args):
	return tripleDrive(t)
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


#Functions for the full Hamiltonain

def phie(t,*args):
	#return PId4 + 0.1*drive(t)
	return 0
def phie2(t,*args):
	#return (PId4 + 0.1*drive(t))**2
	return 0
def phie3(t,*args):
	#return (PId4 + 0.1*drive(t))**3
	return 0
def phie4(t,*args):
	#return (PId4 + 0.1*drive(t))**4
	return 0

def cos2(t,*args):
	return cos(PId4 + drive(t))
def cos6(t,*args):
	return cos((PI/12) + drive(t))
def sin2(t,*args):
	return sin(PId4 + drive(t))
def sin6(t,*args):
	return sin((PI/12) + drive(t))






