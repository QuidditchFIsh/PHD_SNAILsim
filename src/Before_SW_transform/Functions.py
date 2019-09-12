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
		+ 4*COSINE((omega1d - omega2d + omega3d) , t) +4*COSINE((omega1d - omega2d - omega3d) , t))* PI * 0.125

#Define all functions for the rotating Hamiltonian

def no_rotation_cos(t,*args):
	return cos(drive(t).real * phiAC) * EJ

def no_rotation_sin(t,*args):
	return sin(drive(t).real * phiAC) * EJ

def Qsm_cos(t,*args):
	return c_exp(wm,t) * cos(drive(t).real * phiAC) * EJ

def Qsmd_cos(t,*args):
	return c_exp_d(wm,t) * cos(drive(t).real * phiAC) * EJ

def Qsm_sin(t,*args):
	return c_exp(wm,t) * sin(drive(t).real * phiAC) * EJ

def Qsmd_sin(t,*args):
	return c_exp_d(wm,t) * sin(drive(t).real * phiAC) * EJ

def Q1_sp(t,*args):
	return c_exp(w1,t) * c_exp(wp,t) * EL
def Q1_spd(t,*args):	
	return c_exp(w1,t) * c_exp_d(wp,t) * EL
def Q1_sm(t,*args):
	return c_exp(w1,t) * c_exp(wm,t) * EL
def Q1_smd(t,*args):
	return c_exp(w1,t) * c_exp_d(wm,t) * EL

def Q1d_sp(t,*args):
	return c_exp_d(w1,t) * c_exp(wp,t) * EL
def Q1d_spd(t,*args):	
	return c_exp_d(w1,t) * c_exp_d(wp,t) * EL
def Q1d_sm(t,*args):
	return c_exp_d(w1,t) * c_exp(wm,t) * EL
def Q1d_smd(t,*args):
	return c_exp_d(w1,t) * c_exp_d(wm,t) * EL

def Q2_sp(t,*args):
	return c_exp(w2,t) * c_exp(wp,t) * EL
def Q2_spd(t,*args):	
	return c_exp(w2,t) * c_exp_d(wp,t) * EL
def Q2_sm(t,*args):
	return c_exp(w2,t) * c_exp(wm,t) * EL
def Q2_smd(t,*args):
	return c_exp(w2,t) * c_exp_d(wm,t) * EL

def Q2d_sp(t,*args):
	return c_exp_d(w2,t) * c_exp(wp,t) * EL
def Q2d_spd(t,*args):	
	return c_exp_d(w2,t) * c_exp_d(wp,t) * EL
def Q2d_sm(t,*args):
	return c_exp_d(w2,t) * c_exp(wm,t) * EL
def Q2d_smd(t,*args):
	return c_exp_d(w2,t) * c_exp_d(wm,t) * EL

def Q3_sp(t,*args):
	return c_exp(w3,t) * c_exp(wp,t) * EL
def Q3_spd(t,*args):	
	return c_exp(w3,t) * c_exp_d(wp,t) * EL
def Q3_sm(t,*args):
	return c_exp(w3,t) * c_exp(wm,t) * EL
def Q3_smd(t,*args):
	return c_exp(w3,t) * c_exp_d(wm,t) * EL

def Q3d_sp(t,*args):
	return c_exp_d(w3,t) * c_exp(wp,t) * EL
def Q3d_spd(t,*args):	
	return c_exp_d(w3,t) * c_exp_d(wp,t) * EL
def Q3d_sm(t,*args):
	return c_exp_d(w3,t) * c_exp(wm,t) * EL
def Q3d_smd(t,*args):
	return c_exp_d(w3,t) * c_exp_d(wm,t) * EL

