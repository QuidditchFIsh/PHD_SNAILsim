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
	return -(0 + 1j) * (c_exp(omega , t) - c_exp_d(omega , t))
def COSINE(omega,t):
	return (c_exp(omega , t) + c_exp_d(omega , t))

#Define a function to return the drive

def drive(t):
	return (-2*SINE(omega1,t) -2*SINE(omega2,t) -COSINE(omega3,t) \
		+2*SINE((omega2 + omega3) , t) +2*SINE((omega2 - omega3) , t) \
		+2*SINE((omega1 + omega3) , t) +2*SINE((omega1 - omega3) , t) \
		-4*COSINE((omega1 + omega2) , t) + 4*COSINE((omega1 - omega2) , t) \
		- 4*COSINE((omega1 + omega2 + omega3) , t)- 4*COSINE((omega1 + omega2 - omega3) , t) \
		+ 4*COSINE((omega1 - omega2 + omega3) , t) +4*COSINE((omega1 - omega2 - omega3) , t))*EJ
#Full drive testing


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



#RWA test functions
#Functions for QuBit 1
def q1_2_w1(t,*args):
	return c_exp_d(2*omega1,t)*EJ
def q1d_2_w1(t,*args):
	return c_exp(2*omega1,t)*EJ

#Functions for QuBit 2
def q2_2_w2(t,*args):
	return c_exp_d(2*omega2,t)*EJ
def q2d_2_w2(t,*args):
	return c_exp(2*omega2,t)*EJ

#Functions for QuBit 3
def q3_2_w3(t,*args):
	return c_exp_d(2*omega3,t)*EJ
def q3d_2_w3(t,*args):
	return c_exp(2*omega3,t)*EJ

#Functions for QuBits 1 2
def q12_2_w1_pw2(t,*args):
	return c_exp_d(2*(omega1+omega2),t)*EJ
def q1d2d_2_w1_pw2(t,*args):
	return c_exp(2*(omega1+omega2),t)*EJ
def q12d_2_w1_mw2(t,*args):
	return c_exp_d(2*(omega1-omega2),t)*EJ
def q1d2_2_w1_mw2(t,*args):
	return c_exp(2*(omega1-omega2),t)*EJ

#Functions for QuBits 1 3
def q13_2_w1_pw3(t,*args):
	return c_exp_d(2*(omega1+omega3),t)*EJ
def q1d3d_2_w1_pw3(t,*args):
	return c_exp(2*(omega1+omega3),t)*EJ
def q13d_2_w1_mw3(t,*args):
	return c_exp_d(2*(omega1-omega3),t)*EJ
def q1d3_2_w1_mw3(t,*args):
	return c_exp(2*(omega1-omega3),t)*EJ

#Functions for QuBits 2 3
def q23_2_w2_pw3(t,*args):
	return c_exp_d(2*(omega2+omega3),t)*EJ
def q2d3d_2_w2_pw3(t,*args):
	return c_exp(2*(omega2+omega3),t)*EJ
def q23d_2_w2_mw3(t,*args):
	return c_exp_d(2*(omega2-omega3),t)*EJ
def q2d3_2_w2_mw3(t,*args):
	return c_exp(2*(omega2-omega3),t)*EJ

#Functions for QuBits 1 2 3
def q123_2_w1_pw2_pw3(t,*args):
	return c_exp_d(2*(omega1+omega2+omega3),t)*EJ
def q123d_2_w1_pw2_mw3(t,*args):
	return c_exp_d(2*(omega1+omega2-omega3),t)*EJ
def q12d3_2_w1_mw2_pw3(t,*args):
	return c_exp_d(2*(omega1-omega2+omega3),t)*EJ
def q1d23_2_mw1_pw2_pw3(t,*args):
	return c_exp_d(2*(-omega1+omega2+omega3),t)*EJ
def q12d3d_2_mw1_pw2_pw3(t,*args):
	return c_exp(2*(-omega1+omega2+omega3),t)*EJ
def q1d23d_2_w1_mw2_pw3(t,*args):
	return c_exp(2*(omega1-omega2+omega3),t)*EJ
def q1d2d3_2_w1_pw2_mw3(t,*args):
	return c_exp(2*(omega1+omega2-omega3),t)*EJ
def q1d2d3d_2_w1_pw2_pw3(t,*args):
	return c_exp(2*(omega1+omega2+omega3),t)*EJ	
