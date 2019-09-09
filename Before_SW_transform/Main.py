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

#Define all of the variables to use 

R  		= 1/sqrt(2) * (sigmay() + sigmaz())
R3 		= tensor(R,R,R,R)


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
pia = (1/sp_Bar) * (qa - aq.dag())


v1 = q1_Bar * (q1 + q1.dag())
v2 = q2_Bar * (q2 + q2.dag())
v3 = q3_Bar * (q3 + q3.dag())
va = sp_Bar * (qa + qa.dag())


#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential

H = [	[8*third*ECQ1*qa*q1,],[-8*third*ECQ1*qa.dag()*q1,],[-8*third*ECQ1*qa*q1.dag(),],[8*third*ECQ1*qa.dag()*q1.dag(),],
		[8*third*ECQ1*qa*q1,],[-8*third*ECQ1*qa.dag()*q1,],[-8*third*ECQ1*qa*q1.dag(),],[8*third*ECQ1*qa.dag()*q1.dag(),],
		[8*third*ECQ1*qa*q1,],[-8*third*ECQ1*qa.dag()*q1,],[-8*third*ECQ1*qa*q1.dag(),],[8*third*ECQ1*qa.dag()*q1.dag(),],
		[-0.25*0.1*qa*qa,],[-0.25*0.1*qa.dag()*qa,],[-0.25*0.1*qa*qa.dag(),],[-0.25*0.1*qa.dag()*qa.dag(),],
		[-0.5*0.1*qa,],[-0.5*0.1*qa.dag(),],

] 

