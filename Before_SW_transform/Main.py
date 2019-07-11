'''
Author:Aneirin John Baker	
Date: 11/07/19
Description: Main script within this simulation. It will handle all of the solvers and will hold
all of the Hamiltonian variables and the Hamiltonian itself.It will then pass all of the results onto
another script for that to print all of it out.
'''

from Constants import *
from functions import *
from qutip import *
from math import *

#Define all of the variables to use 

R  		= 1/sqrt(2) * (sigmay() + sigmaz())
R3 		= tensor(R,R,R,R,R)


one  	= R*basis(2,1)
zero 	= R*basis(2,0)

a 		= sigmap()

q1 		= tensor(a,qeye(2),qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2),qeye(2))
sm 		= tensor(qeye(2),qeye(2),qeye(2),a,qeye(2))
sp 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2),qeye(2))

