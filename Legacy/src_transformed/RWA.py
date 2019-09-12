import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
import datetime

'''
def w1(t,*args):
	return EJ  * (0 + 1j)
def w1_d(t,*args):
	return EJ  * (0 - 1j)
def w2(t,*args):
	return EJ * (0 + 1j)
def w2_d(t,*args):
	return EJ * (0 - 1j)
def w3(t,*args):
	return EJ
def w3_d(t,*args):
	return EJ

def w2_w3(t,*args):
	return EJ* (0 + 1j)
def w2_w3_d(t,*args):
	return EJ* (0 - 1j)
def w2_w3m(t,*args):
	return EJ* (0 + 1j)
def w2_w3m_d(t,*args):
	return EJ* (0 - 1j)

def w1_w3(t,*args):
	return EJ* (0 + 1j)
def w1_w3_d(t,*args):
	return EJ * (0 - 1j)
def w1_w3m(t,*args):
	return EJ* (0 + 1j)
def w1_w3m_d(t,*args):
	return EJ* (0 - 1j)

def w1_w2(t,*args):
	return EJ 
def w1_w2_d(t,*args):
	return EJ
def w1_w2m(t,*args):
	return EJ
def w1_w2m_d(t,*args):
	return EJ

def w1_w2_w3(t,*args):
	return EJ 
def w1_w2_w3_d(t,*args):
	return EJ
def w1_w2_w3m(t,*args):
	return EJ
def w1_w2_w3m_d(t,*args):
	return EJ
def w1_w2m_w3(t,*args):
	return EJ
def w1_w2m_w3_d(t,*args):
	return EJ
def w1_w2m_w3m(t,*args):
	return EJ
def w1_w2m_w3m_d(t,*args):
	return EJ
'''
'''
########################################################
'''
def w1(t,*args):
	return EJ * (cos(omega1 * t) + (0 + 1j)*sin(omega1 * t)) * (cos(omega1 * t) - (0 + 1j)*sin(omega1 * t)) * (0 + 1j)
def w1_d(t,*args):
	return EJ * (cos(omega1 * t) - (0 + 1j)*sin(omega1 * t)) * (cos(omega1 * t) + (0 + 1j)*sin(omega1 * t)) * (0 - 1j)
def w1_2(t,*args):
	return EJ * (cos(2 * omega1 * t) + (0 + 1j)*sin(2 * omega1 * t)) * (0 - 1j)
def w1_2d(t,*args):
	return EJ * (cos(2 * omega1 * t) - (0 + 1j)*sin(2 * omega1 * t)) * (0 + 1j)
def w2(t,*args):
	return EJ * (cos(omega2 * t) + (0 + 1j)*sin(omega2 * t)) * (cos(omega2 * t) - (0 + 1j)*sin(omega2 * t)) * (0 + 1j)
def w2_d(t,*args):
	return EJ * (cos(omega2 * t) - (0 + 1j)*sin(omega2 * t)) * (cos(omega2 * t) + (0 + 1j)*sin(omega2 * t)) * (0 - 1j)
def w2_2(t,*args):
	return EJ * (cos(2 * omega2 * t) + (0 + 1j)*sin(2 * omega2 * t)) * (0 - 1j)
def w2_2d(t,*args):
	return EJ * (cos(2 * omega2 * t) - (0 + 1j)*sin(2 * omega2 * t)) * (0 + 1j)
def w3(t,*args):
	return EJ * (cos(omega3 * t) + (0 + 1j)*sin(omega3 * t)) * (cos(omega3 * t) - (0 + 1j)*sin(omega3 * t)) 
def w3_d(t,*args):
	return EJ * (cos(omega3 * t) - (0 + 1j)*sin(omega3 * t)) * (cos(omega3 * t) + (0 + 1j)*sin(omega3 * t)) 
def w3_2(t,*args):
	return EJ * (cos(2 * omega3 * t) + (0 + 1j)*sin(2 * omega3 * t))
def w3_2d(t,*args):
	return EJ * (cos(2 * omega3 * t) - (0 + 1j)*sin(2 * omega3 * t))

def w2_w3(t,*args):
	return EJ * (cos((omega2 + omega3) * t) + (0 + 1j)*sin((omega2 + omega3) * t)) * (cos((omega2 + omega3) * t) - (0 + 1j)*sin((omega2 + omega3) * t)) * (0 + 1j)
def w2_w3_d(t,*args):
	return EJ * (cos((omega2 + omega3) * t) - (0 + 1j)*sin((omega2 + omega3) * t)) * (cos((omega2 + omega3) * t) + (0 + 1j)*sin((omega2 + omega3) * t)) * (0 - 1j)
def w2_w3m(t,*args):
	return EJ * (cos((omega2 - omega3) * t) + (0 + 1j)*sin((omega2 - omega3) * t)) * (cos((omega2 - omega3) * t) - (0 + 1j)*sin((omega2 - omega3) * t)) * (0 + 1j)
def w2_w3m_d(t,*args):
	return EJ * (cos((omega2 - omega3) * t) - (0 + 1j)*sin((omega2 - omega3) * t)) * (cos((omega2 - omega3) * t) + (0 + 1j)*sin((omega2 - omega3) * t)) * (0 - 1j)

def w1_w3(t,*args):
	return EJ * (cos((omega1 + omega3) * t) + (0 + 1j)*sin((omega1 + omega3) * t)) * (cos((omega1 + omega3) * t) - (0 + 1j)*sin((omega1 + omega3) * t)) * (0 + 1j)
def w1_w3_d(t,*args):
	return EJ * (cos((omega1 + omega3) * t) - (0 + 1j)*sin((omega1 + omega3) * t)) * (cos((omega1 + omega3) * t) + (0 + 1j)*sin((omega1 + omega3) * t)) * (0 - 1j)
def w1_w3m(t,*args):
	return EJ * (cos((omega1 - omega3) * t) + (0 + 1j)*sin((omega1 - omega3) * t)) * (cos((omega1 - omega3) * t) - (0 + 1j)*sin((omega1 - omega3) * t)) * (0 + 1j)
def w1_w3m_d(t,*args):
	return EJ * (cos((omega1 - omega3) * t) - (0 + 1j)*sin((omega1 - omega3) * t)) * (cos((omega1 - omega3) * t) + (0 + 1j)*sin((omega1 - omega3) * t)) * (0 - 1j)

def w1_w2(t,*args):
	return EJ * (cos((omega1 + omega2) * t) + (0 + 1j)*sin((omega1 + omega2) * t)) * (cos((omega1 + omega2) * t) - (0 + 1j)*sin((omega1 + omega2) * t)) 
def w1_w2_d(t,*args):
	return EJ * (cos((omega1 + omega2) * t) - (0 + 1j)*sin((omega1 + omega2) * t)) * (cos((omega1 + omega2) * t) + (0 + 1j)*sin((omega1 + omega2) * t))
def w1_w2m(t,*args):
	return EJ * (cos((omega1 - omega2) * t) + (0 + 1j)*sin((omega1 - omega2) * t)) * (cos((omega1 - omega2) * t) - (0 + 1j)*sin((omega1 - omega2) * t))
def w1_w2m_d(t,*args):
	return EJ * (cos((omega1 - omega2) * t) - (0 + 1j)*sin((omega1 - omega2) * t)) * (cos((omega1 - omega2) * t) + (0 + 1j)*sin((omega1 - omega2) * t))

def w1_w2_w3(t,*args):
	return EJ * (cos((omega1 + omega2 + omega3) * t) + (0 + 1j)*sin((omega1 + omega2 + omega3) * t)) * (cos((omega1 + omega2 + omega3) * t) - (0 + 1j)*sin((omega1 + omega2 + omega3) * t)) 
def w1_w2_w3_d(t,*args):
	return EJ * (cos((omega1 + omega2 + omega3) * t) - (0 + 1j)*sin((omega1 + omega2 + omega3) * t)) * (cos((omega1 + omega2 + omega3) * t) + (0 + 1j)*sin((omega1 + omega2 + omega3) * t))
def w1_w2_w3m(t,*args):
	return EJ * (cos((omega1 + omega2 - omega3) * t) + (0 + 1j)*sin((omega1 + omega2 - omega3) * t)) * (cos((omega1 + omega2 - omega3) * t) - (0 + 1j)*sin((omega1 + omega2 - omega3) * t))
def w1_w2_w3m_d(t,*args):
	return EJ * (cos((omega1 + omega2 - omega3) * t) - (0 + 1j)*sin((omega1 + omega2 - omega3) * t)) * (cos((omega1 + omega2 - omega3) * t) + (0 + 1j)*sin((omega1 + omega2 - omega3) * t))
def w1_w2m_w3(t,*args):
	return EJ * (cos((omega1 - omega2 + omega3) * t) + (0 + 1j)*sin((omega1 - omega2 + omega3) * t)) * (cos((omega1 - omega2 + omega3) * t) - (0 + 1j)*sin((omega1 - omega2 + omega3) * t))
def w1_w2m_w3_d(t,*args):
	return EJ * (cos((omega1 - omega2 + omega3) * t) - (0 + 1j)*sin((omega1 - omega2 + omega3) * t)) * (cos((omega1 - omega2 + omega3) * t) + (0 + 1j)*sin((omega1 - omega2 + omega3) * t))
def w1_w2m_w3m(t,*args):
	return EJ * (cos((omega1 - omega2 - omega3) * t) + (0 + 1j)*sin((omega1 - omega2 - omega3) * t)) * (cos((omega1 - omega2 - omega3) * t) - (0 + 1j)*sin((omega1 - omega2 - omega3) * t))
def w1_w2m_w3m_d(t,*args):
	return EJ * (cos((omega1 - omega2 - omega3) * t) - (0 + 1j)*sin((omega1 - omega2 - omega3) * t)) * (cos((omega1 - omega2 - omega3) * t) + (0 + 1j)*sin((omega1 - omega2 - omega3) * t))
'''
#######################################################
def w1(t,*args):
	return EJ * (cos(omega1 * t) + (0 + 1j)*sin(omega1 * t) 
def w1_d(t,*args):
	return EJ * (cos(omega1 * t) - (0 + 1j)*sin(omega1 * t) 
def w2(t,*args):
	return EJ * (cos(omega2 * t) + (0 + 1j)*sin(omega2 * t) 
def w2_d(t,*args):
	return EJ * (cos(omega2 * t) - (0 + 1j)*sin(omega2 * t) 
def w3(t,*args):
	return EJ * (cos(omega3 * t) + (0 + 1j)*sin(omega3 * t) 
def w3_d(t,*args):
	return EJ * (cos(omega3 * t) - (0 + 1j)*sin(omega3 * t) 

def w2_w3(t,*args):
	return EJ * (cos((omega2 + omega3) * t) + (0 + 1j)*sin((omega2 + omega3) * t)
def w2_w3_d(t,*args):
	return EJ * (cos((omega2 + omega3) * t) - (0 + 1j)*sin((omega2 + omega3) * t)
def w2_w3m(t,*args):
	return EJ * (cos((omega2 - omega3) * t) + (0 + 1j)*sin((omega2 - omega3) * t)
def w2_w3m_d(t,*args):
	return EJ * (cos((omega2 - omega3) * t) - (0 + 1j)*sin((omega2 - omega3) * t)

def w1_w3(t,*args):
	return EJ * (cos((omega1 + omega3) * t) + (0 + 1j)*sin((omega1 + omega3) * t)
def w1_w3_d(t,*args):
	return EJ * (cos((omega1 + omega3) * t) - (0 + 1j)*sin((omega1 + omega3) * t)
def w1_w3m(t,*args):
	return EJ * (cos((omega1 - omega3) * t) + (0 + 1j)*sin((omega1 - omega3) * t)
def w1_w3m_d(t,*args):
	return EJ * (cos((omega1 - omega3) * t) - (0 + 1j)*sin((omega1 - omega3) * t)

def w1_w2(t,*args):
	return EJ * (cos((omega1 + omega2) * t) + (0 + 1j)*sin((omega1 + omega2) * t)
def w1_w2_d(t,*args):
	return EJ * (cos((omega1 + omega2) * t) - (0 + 1j)*sin((omega1 + omega2) * t)
def w1_w2m(t,*args):
	return EJ * (cos((omega1 - omega2) * t) + (0 + 1j)*sin((omega1 - omega2) * t)
def w1_w2m_d(t,*args):
	return EJ * (cos((omega1 - omega2) * t) - (0 + 1j)*sin((omega1 - omega2) * t)

def w1_w2_w3(t,*args):
	return EJ * (cos((omega1 + omega2 + omega3) * t) + (0 + 1j)*sin((omega1 + omega2 + omega3) * t)
def w1_w2_w3_d(t,*args):
	return EJ * (cos((omega1 + omega2 + omega3) * t) - (0 + 1j)*sin((omega1 + omega2 + omega3) * t)
def w1_w2_w3m(t,*args):
	return EJ * (cos((omega1 + omega2 - omega3) * t) + (0 + 1j)*sin((omega1 + omega2 - omega3) * t)
def w1_w2_w3m_d(t,*args):
	return EJ * (cos((omega1 + omega2 - omega3) * t) - (0 + 1j)*sin((omega1 + omega2 - omega3) * t)
def w1_w2m_w3(t,*args):
	return EJ * (cos((omega1 - omega2 + omega3) * t) + (0 + 1j)*sin((omega1 - omega2 + omega3) * t)
def w1_w2m_w3_d(t,*args):
	return EJ * (cos((omega1 - omega2 + omega3) * t) - (0 + 1j)*sin((omega1 - omega2 + omega3) * t)
def w1_w2m_w3m(t,*args):
	return EJ * (cos((omega1 - omega2 - omega3) * t) + (0 + 1j)*sin((omega1 - omega2 - omega3) * t)
def w1_w2m_w3m_d(t,*args):
	return EJ * (cos((omega1 - omega2 - omega3) * t) - (0 + 1j)*sin((omega1 - omega2 - omega3) * t)
'''

R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1
one  = basis(2,1)
zero = basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

q1_before = tensor(sigmap(), qeye(2),qeye(2))
q2_before = tensor(qeye(2),sigmap(),qeye(2))
q3_before = tensor(qeye(2),qeye(2),sigmap())

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(2),qeye(2),qeye(2))


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())

'''
s1z = (0 + 1j)*(q1.dag() - q1)
s2z = (0 + 1j)*(q2.dag() - q2)
s3z = (0 + 1j)*(q3.dag() - q3)

s1y = q1*q1.dag() - q1.dag()*q1
s2y = q2*q2.dag() - q2.dag()*q2
s3y = q3*q3.dag() - q3.dag()*q3

s1x = -1 * (q1 + q1.dag())
s2x = -1 * (q2 + q2.dag())
s3x = -1 * (q3 + q3.dag())
'''



tlist = np.linspace(0,1000,num=1000)
#R = 1/sqrt(2) * (sigmay() + sigmaz())
R=1
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R)

EJ = 0.01
#H2 = EJ *(I - s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
H2 = EJ *(I - s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)



H = [[-1 * q1,w1],[-1 * q1.dag(),w1_d],[-1 * q2,w2],[-1 * q2.dag(),w2_d],[-1 * q3,w3],[-1 * q3.dag(),w3_d],
[-1 * q1*q2,w1_w2],[q1*q2.dag(),w1_w2m],[q1.dag()*q2,w1_w2m_d],[-1 * q1.dag()*q2.dag(),w1_w2_d],
[-1 * q1*q3,w1_w3],[-1 * q1*q3.dag(),w1_w3m],[-1 * q1.dag()*q3,w1_w3m_d],[-1 * q1.dag()*q3.dag(),w1_w3_d],
[-1 * q2*q3,w2_w3],[-1 * q2*q3.dag(),w2_w3m],[-1 * q2.dag()*q3,w2_w3m_d],[-1 * q2.dag()*q3.dag(),w2_w3_d],
[-1 * q1*q2*q3,w1_w2_w3],[-1 * q1*q2*q3.dag(),w1_w2_w3m],[q1*q2.dag()*q3,w1_w2m_w3],[q1.dag()*q2*q3,w1_w2m_w3m_d],
[q1*q2.dag()*q3.dag(),w1_w2m_w3m],[q1.dag()*q2*q3.dag(),w1_w2m_w3_d],[-1 * q1.dag()*q2.dag()*q3,w1_w2_w3m_d],[-1 * q1.dag()*q2.dag()*q3.dag(),w1_w2_w3_d],

[-1*q1,w1_2],[-1*q1.dag(),w1_2d],[-1*q2,w2_2],[-1*q2.dag(),w2_2d],[-1*q3,w3_2],[-1*q3.dag(),w3_2d]


]
'''

[-1 * (0+1j)*q1,w1],[(0+1j)*q1,w1_d],[-1 * (0+1j)*q2,w2],[(0+1j)*q2,w2_d],[q3,w3],[q3.dag(),w3_d],



[(0+1j) * q2 * q3,w2_w3],[(0+1j) * q2 * q3.dag(),w2],[(0+1j) * q2.dag() * q3,w3],[-1 * (0+1j) * q2.dag() * q3.dag(),w2_w3_d],[-1 * (0+1j) * q2.dag() * q3,w2_d],[-1 * (0+1j) * q2 * q3.dag(),w3_d],
[(0+1j) * q2 * q3,w2],[(0+1j) * q2 * q3.dag(),w2_w3m],[(0+1j) * q2.dag() * q3.dag(),w3_d],[-1 * (0+1j) * q2.dag() * q3.dag(),w2_d],[-1 * (0+1j) * q2.dag() * q3,w2_w3m_d],[-1 * (0+1j) * q2 * q3,w3],


[(0+1j) * q1 * q3,w1_w3],[(0+1j) * q1 * q3.dag(),w1],[(0+1j) * q1.dag() * q3,w3],[-1 * (0+1j) * q1.dag() * q3.dag(),w1_w3_d],[-1 * (0+1j) * q1.dag() * q3,w1_d],[-1 * (0+1j) * q1 * q3.dag(),w3_d],
[(0+1j) * q1 * q3,w1],[(0+1j) * q1 * q3.dag(),w1_w3m],[(0+1j) * q1.dag() * q3.dag(),w3_d],[-1 * (0+1j) * q1.dag() * q3.dag(),w1_d],[-1 * (0+1j) * q1.dag() * q3,w1_w3m_d],[-1 * (0+1j) * q1 * q3,w3],

[-1 * q1 * q2,w1_w2],[-1 * q1 * q2.dag(),w1],[-1 * q1.dag() * q2,w2],[-1 * q1.dag() * q2.dag(),w1_w2_d],[-1 * q1.dag() * q2,w1_d],[-1 * q1 * q2.dag(),w2_d],
[q1 * q2,w1],[q1 * q2.dag(),w1_w2m],[q1.dag() * q2.dag(),w2_d],[q1.dag() * q2.dag(),w1_d],[q1.dag() * q2,w1_w2m_d],[q1 * q2,w2],



[-1 * q1 * q2 * q3,w1_w2_w3],[-1 * q1 * q2 * q3.dag(),w1_w2],[-1 * q1 * q2.dag() * q3,w1_w3],[-1 * q1.dag() * q2 * q3,w2_w3],
[-1 * q1 * q2.dag() * q3.dag(),w1],[-1 * q1.dag() * q2 * q3.dag(),w2],[-1 * q1.dag() * q2.dag() * q3,w3],[-1 * q1 * q2 * q3.dag(),w3_d],
[-1 * q1 * q2.dag() * q3,w2_d],[-1 * q1.dag() * q2 * q3,w1_d],[-1 * q1 * q2.dag() * q3.dag(),w2_w3_d],[-1 * q1.dag() * q2 * q3.dag(),w1_w3_d],
[-1 * q1.dag() * q2.dag() * q3,w1_w2_d],[-1 * q1.dag() * q2.dag() * q3.dag(),w1_w2_w3_d],



[-1 * q1 * q2 * q3,w1_w2],[-1 * q1 * q2 * q3.dag(),w1_w2_w3m],[-1 * q1 * q2.dag() * q3,w1],[-1 * q1.dag() * q2 * q3,w2],
[-1 * q1 * q2.dag() * q3.dag(),w1_w3m],[-1 * q1.dag() * q2 * q3.dag(),w2_w3m],[-1 * q1.dag() * q2.dag() * q3.dag(),w3_d],[-1 * q1 * q2 * q3,w3],
[-1 * q1 * q2.dag() * q3,w2_w3m_d],[-1 * q1.dag() * q2 * q3,w1_w3m_d],[-1 * q1 * q2.dag() * q3.dag(),w2_d],[-1 * q1.dag() * q2 * q3.dag(),w1_d],
[-1 * q1.dag() * q2.dag() * q3,w1_w2_w3m_d],[-1 * q1.dag() * q2.dag() * q3.dag(),w1_w2_d],


[q1 * q2 * q3,w1_w3],[q1 * q2 * q3.dag(),w1],[q1 * q2.dag() * q3,w1_w2m_w3],[q1.dag() * q2 * q3,w3],
[q1 * q2.dag() * q3.dag(),w1_w2m],[q1.dag() * q2.dag() * q3,w2_w3m_d],[q1.dag() * q2.dag() * q3.dag(),w2_d],[q1 * q2 * q3,w2],
[q1 * q2 * q3.dag(),w2_w3m],[q1.dag() * q2 * q3,w1_w2m_d],[q1 * q2.dag() * q3.dag(),w3_d],[q1.dag() * q2 * q3.dag(),w1_w2m_w3_d],
[q1.dag() * q2.dag() * q3,w1_d],[q1.dag() * q2.dag() * q3.dag(),w1_w3_d],


[q1 * q2 * q3,w1],[q1 * q2 * q3.dag(),w1_w3m],[q1 * q2.dag() * q3,w1_w2m],
[q1 * q2.dag() * q3.dag(),w1_w2m],[q1.dag() * q2 * q3.dag(),w3_d],[q1.dag() * q2.dag() * q3,w2_d],
[q1.dag() * q2.dag() * q3.dag(),w2_w3_d],
[q1 * q2 * q3,w2_w3],[q1 * q2 * q3.dag(),w2],[q1 * q2.dag() * q3,w3],
[q1.dag() * q2 * q3,w1_w2m_w3m_d],[q1.dag() * q2 * q3.dag(),w1_w2m_d],[q1.dag() * q2.dag() * q3,w1_w3m_d],
[q1.dag() * q2.dag() * q3.dag(),w1_d]


H = [[-1 * q1,w1],[-1 * q1.dag(),w1_d],[-1 * q2,w2],[-1 * q2.dag(),w2_d],[-1 * q3,w3],[-1 * q3.dag(),w3_d],
[-1 * q1*q2,w1_w2],[q1*q2.dag(),w1_w2m],[q1.dag()*q2,w1_w2m_d],[-1 * q1.dag()*q2.dag(),w1_w2_d],
[-1 * q1*q3,w1_w3],[-1 * q1*q3.dag(),w1_w3m],[-1 * q1.dag()*q3,w1_w3m_d],[-1 * q1.dag()*q3.dag(),w1_w3_d],
[-1 * q2*q3,w2_w3],[-1 * q2*q3.dag(),w2_w3m],[-1 * q2.dag()*q3,w2_w3m_d],[-1 * q2.dag()*q3.dag(),w2_w3_d],
[-1 * q1*q2*q3,w1_w2_w3],[-1 * q1*q2*q3.dag(),w1_w2_w3m],[q1*q2.dag()*q3,w1_w2m_w3],[q1.dag()*q2*q3,w1_w2m_w3m_d],
[q1*q2.dag()*q3.dag(),w1_w2m_w3m],[q1.dag()*q2*q3.dag(),w1_w2m_w3_d],[-1 * q1.dag()*q2.dag()*q3,w1_w2_w3m_d],[-1 * q1.dag()*q2.dag()*q3.dag(),w1_w2_w3_d]
]
'''
c_ops = [0.00005*q1,0.00005*q2,0.00005*q3,0.0001*sz1,0.0001*sz2,0.0001*sz3]
outputstr = ''

#freqs = np.genfromtxt('Frequencies3.dat')
freqs = [[4,10,17]]
for j in freqs:
	print(j)
	omega1   	= j[0]
	omega2   	= j[1]
	omega3   	= j[2]
	f1 			= j[0]
	f2 			= j[1]
	f3 			= j[2]
	for i in range(0,2):
		if i == 0:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_26-06-19/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_26-06-19/occupation_q1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_26-06-19/occupation_q2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_26-06-19/occupation_q3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_26-06-19/sz1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_26-06-19/sz2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_26-06-19/sz3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H,psi0,tlist,c_ops,[I,I,I],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 1:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_26-06-19/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_26-06-19/occupation_q1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_26-06-19/occupation_q2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_26-06-19/occupation_q3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_26-06-19/sz1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_26-06-19/sz2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_26-06-19/sz3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H,psi0,tlist,c_ops,[sz1,sz2,sz3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))

		fidelity_dat 	= []
		occupation_1 	= []
		occupation_2 	= []
		occupation_3 	= []
		sigmaz_1 		= []
		sigmaz_2 		= []
		sigmaz_3 		= []

		for j in range(0,len(tlist)):
		 		fidelity_dat.append(fidelity(result.states[j],Tdm))
		 		occupation_1.append(expect(result.states[j],q1_before.dag() * q1_before))
		 		occupation_2.append(expect(result.states[j],q2_before.dag() * q2_before))
		 		occupation_3.append(expect(result.states[j],q3_before.dag() * q3_before))
		 		sigmaz_1.append(result.expect[0][j])
		 		sigmaz_2.append(result.expect[1][j])
		 		sigmaz_3.append(result.expect[2][j])

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
		with open(outputstr_sz1,'w') as file5:
			for j in sigmaz_1:
				file5.write(str(j) + "\n")
		with open(outputstr_sz2,'w') as file6:
			for j in sigmaz_2:
				file6.write(str(j) + "\n")
		with open(outputstr_sz3,'w') as file7:
			for j in sigmaz_3:
				file7.write(str(j) + "\n")
