from math import *
from Constants import *

#Define the 

#Define a complex exponential function
def c_exp(omega,t):
	return (cos(omega * t) + (0 + 1j)*sin(omega*t))
def c_exp_d(omega,t):
	return (cos(omega * t) - (0 + 1j)*sin(omega*t))

#define exponential SINE and COSEIN
def SINE(omega,t):
	return -0.5 * (0 + 1j) * (c_exp(omega , t) - c_exp_d(omega , t))
def COSINE(omega,t):
	return 0.5 * (c_exp(omega , t) + c_exp_d(omega , t))

#Define a function to return the drive

def drive(t):
	return (SINE(omega1d,t) + SINE(omega2d,t) -COSINE(omega3d,t) \
		- 1.5*SINE((omega2d + omega3d) , t) - 1.5*SINE((omega2d - omega3d) , t) \
		- 1.5*SINE((omega1d + omega3d) , t) - 1.5*SINE((omega1d - omega3d) , t) \
		- 1.5*COSINE((omega1d + omega2d) , t) + 1.5*COSINE((omega1d - omega2d) , t) \
		- 1.5*COSINE((omega1d + omega2d + omega3d) , t) - 1.5*COSINE((omega1d + omega2d - omega3d) , t) \
		+ 1.5*COSINE((omega1d - omega2d + omega3d) , t) + 1.5*COSINE((omega1d - omega2d - omega3d) , t))

#Full drive testing
#define all of the RWA terms
def Q1_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5
def Q2_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5
def Q3_RWA(t,*args):
	return EJ  * 0.5

def Q1_Q3_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5
def Q1_Q3d_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5

def Q1_Q2_RWA(t,*args):
	return EJ  * 0.5
def Q1_Q2d_RWA(t,*args):
	return EJ  * 0.5


def Q2_Q3_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5
def Q2_Q3d_RWA(t,*args):
	return EJ * (0 + 1j) * 0.5



def Q1_Q2_Q3_RWA(t,*args):
	return EJ * 0.5
def Q1_Q2_Q3d_RWA(t,*args):
	return EJ  * 0.5
def Q1_Q2d_Q3_RWA(t,*args):
	return EJ  * 0.5
def Q1_Q2d_Q3d_RWA(t,*args):
	return EJ  * 0.5

#define all of the time dependatn parts for the qubit terms in the Hamiltonian
def Q1(t,*args):
	return EJ  * drive(t)
def Q1d(t,*args):
	return EJ  * drive(t)
def Q2(t,*args):
	return EJ  * drive(t)
def Q2d(t,*args):
	return EJ  * drive(t)
def Q3(t,*args):
	return EJ  * drive(t)
def Q3d(t,*args):
	return EJ  * drive(t)


def Q13(t,*args):
	return EJ  * drive(t)
def Q13d(t,*args):
	return EJ  * drive(t)
def Q1d3(t,*args):
	return EJ  * drive(t)
def Q1d3d(t,*args):
	return EJ  * drive(t)

def Q12(t,*args):
	return EJ  * drive(t)
def Q12d(t,*args):
	return EJ  * drive(t)
def Q1d2(t,*args):
	return EJ  * drive(t)
def Q1d2d(t,*args):
	return EJ * drive(t)

def Q23(t,*args):
	return EJ  * drive(t)
def Q23d(t,*args):
	return EJ  * drive(t)
def Q2d3(t,*args):
	return EJ  * drive(t)
def Q2d3d(t,*args):
	return EJ  * drive(t)


def Q123(t,*args):
	return EJ  * drive(t)
def Q123d(t,*args):
	return EJ  * drive(t)
def Q12d3(t,*args):
	return EJ  * drive(t)
def Q12d3d(t,*args):
	return EJ  * drive(t)
def Q1d2d3d(t,*args):
	return EJ  * drive(t)
def Q1d2d3(t,*args):
	return EJ  * drive(t)
def Q1d23d(t,*args):
	return EJ  * drive(t)
def Q1d23(t,*args):
	return EJ  * drive(t)

