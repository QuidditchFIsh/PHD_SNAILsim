from math import *
from Constants import *

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

def drive(t):
	return (SINE(omega1d,t) + SINE(omega2d,t) -COSINE(omega3d,t) \
		- 1.5*SINE((omega2d + omega3d) , t) - 1.5*SINE((omega2d - omega3d) , t) \
		- 1.5*SINE((omega1d + omega3d) , t) - 1.5*SINE((omega1d - omega3d) , t) \
		- 1.5*COSINE((omega1d + omega2d) , t) + 1.5*COSINE((omega1d - omega2d) , t) \
		- 1.5*COSINE((omega1d + omega2d + omega3d) , t) - 1.5*COSINE((omega1d + omega2d - omega3d) , t) \
		+ 1.5*COSINE((omega1d - omega2d + omega3d) , t) + 1.5*COSINE((omega1d - omega2d - omega3d) , t))*EJ


#Interaction Hamiltonian function
def Q1(t,*args):
	return c_exp_d(omega1,t) * drive(t)
def Q1d(t,*args):
	return c_exp(omega1,t) * drive(t)

def Q2(t,*args):
	return c_exp_d(omega2,t) * drive(t)
def Q2d(t,*args):
	return c_exp(omega2,t) * drive(t)

def Q3(t,*args):
	return c_exp_d(omega3,t) * drive(t)
def Q3d(t,*args):
	return c_exp(omega3,t) * drive(t)

def Q23(t,*args):
	return c_exp_d(omega2+omega3,t) * drive(t)
def Q23d(t,*args):	
	return c_exp_d(omega2-omega3,t) * drive(t)
def Q2d3(t,*args):
	return c_exp(omega2-omega3,t) * drive(t)
def Q2d3d(t,*args):
	return c_exp(omega2+omega3,t) * drive(t)

def Q13(t,*args):
	return c_exp_d(omega1+omega3,t) * drive(t)
def Q13d(t,*args):	
	return c_exp_d(omega1-omega3,t) * drive(t)
def Q1d3(t,*args):
	return c_exp(omega1-omega3,t) * drive(t)
def Q1d3d(t,*args):
	return c_exp(omega1+omega3,t) * drive(t)

def Q12(t,*args):
	return c_exp_d(omega1+omega2,t) * drive(t)
def Q12d(t,*args):	
	return c_exp_d(omega1-omega2,t) * drive(t)
def Q1d2(t,*args):
	return c_exp(omega1-omega2,t) * drive(t)
def Q1d2d(t,*args):
	return c_exp(omega1+omega2,t) * drive(t)

def Q123(t,*args):
	return c_exp_d(omega1+omega2+omega3,t) * drive(t)
def Q123d(t,*args):
	return c_exp_d(omega1+omega2-omega3,t) * drive(t)
def Q12d3(t,*args):
	return c_exp_d(omega1-omega2+omega3,t) * drive(t)
def Q12d3d(t,*args):
	return c_exp_d(omega1-omega2-omega3,t) * drive(t)
def Q1d2d3d(t,*args):
	return c_exp(omega1+omega2+omega3,t) * drive(t)
def Q1d2d3(t,*args):
	return c_exp(omega1+omega2-omega3,t) * drive(t)
def Q1d23d(t,*args):
	return c_exp(omega1-omega2+omega3,t) * drive(t)
def Q1d23(t,*args):
	return c_exp(omega1-omega2-omega3,t) * drive(t)

def SM_Q1(t,*args):
	return c_exp(omegaM + omega1,t) * ECQ
def SM_Q1d(t,*args):
	return c_exp(omegaM - omega1,t) * ECQ
def SMd_Q1(t,*args):
	return c_exp_d(omegaM - omega1,t) * ECQ
def SMd_Q1d(t,*args):
	return c_exp_d(omegaM + omega1,t) * ECQ

#Squid functions
def SM_Q2(t,*args):
	return c_exp(omegaM + omega2,t) * ECQ
def SM_Q2d(t,*args):
	return c_exp(omegaM - omega2,t) * ECQ
def SMd_Q2(t,*args):
	return c_exp_d(omegaM - omega2,t) * ECQ
def SMd_Q2d(t,*args):
	return c_exp_d(omegaM + omega2,t) * ECQ

def SM_Q3(t,*args):
	return c_exp(omegaM + omega3,t) * ECQ
def SM_Q3d(t,*args):
	return c_exp(omegaM - omega3,t) * ECQ
def SMd_Q3(t,*args):
	return c_exp_d(omegaM - omega3,t) * ECQ
def SMd_Q3d(t,*args):
	return c_exp_d(omegaM + omega3,t) * ECQ
def SM(t,*args):
	return c_exp(omegaM,t)
def SMd(t,*args):
	return c_exp_d(omegaM,t)

#Function for perturbations to Hsq

def no_rotation(t,*args):
	return drive(t)