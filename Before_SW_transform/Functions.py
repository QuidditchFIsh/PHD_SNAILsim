'''
Author:Aneirin John Baker
Date:11/07/19
Description:Script used to store all of the functions for generating the drive.
'''

from Constants import *
from math import *
from qutip import *

from Constants import *
from math import *
from qutip import *

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
	return (-2*SINE(omega1d,t) -2*SINE(omega2d,t) -COSINE(omega3d,t) \
		+2*SINE((omega2d + omega3d) , t) +2*SINE((omega2d - omega3d) , t) \
		+2*SINE((omega1d + omega3d) , t) +2*SINE((omega1d - omega3d) , t) \
		-4*COSINE((omega1d + omega2d) , t) + 4*COSINE((omega1d - omega2d) , t) \
		- 4*COSINE((omega1d + omega2d + omega3d) , t)- 4*COSINE((omega1d + omega2d - omega3d) , t) \
		+ 4*COSINE((omega1d - omega2d + omega3d) , t) +4*COSINE((omega1d - omega2d - omega3d) , t))*EJ

