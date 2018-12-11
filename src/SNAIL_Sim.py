from Constants import *
import numpy as np
from qutip import *
from math import *
import matplotlib.pyplot as plt

'''
Author : Aneirin J Baker 
Date : 11/12/2018
Description : Numerial siulation of the SNAIL circuit which i have been designing Using QuTIP package. Also will include a simulation of teh RF SUID for comparison
'''

#All of the constants which are needed will be in the constants class 
#Start by defining all of the operators which will be needed there are 10 variabels which will need to be defined. Each of these will have a strength associated with it as well

q1 = tensor(destroy(2) , qeye(2) , qeye(2) , qeye(2) , qeye(2))
q2 = tensor(qeye(2) , destroy(2) , qeye(2) , qeye(2) , qeye(2))
q3 = tensor(qeye(2) , qeye(2) , destroy(2) , qeye(2) , qeye(2))
sP = tensor(qeye(2) , qeye(2) , qeye(2) , destroy(2) , qeye(2))
sM = tensor(qeye(2) , qeye(2) , qeye(2) , qeye(2) , destroy(2))

times = np.linspace(0.0 , 20.0 , 400) #Test parameters will need changing when start real simulations.

############ Will need to put in the expressions for these######
phiBar_1 = 1
phiBar_2 = 1
phiBar_3 = 1
phiBar_P = 1
phiBar_M = 1
################################################################

phi_1 = phiBar_1 *(q1 + q1.dag())
phi_2 = phiBar_2 *(q2 + q2.dag())
phi_3 = phiBar_3 *(q3 + q3.dag())
phi_P = phiBar_P *(sP + sP.dag())
phi_M = phiBar_M *(sM + sM.dag())

#Now define the Hamiltonian using all of the Constants and variables. Will define the Hamiltonian in severl parts

H_0  = 
H_S  = 
H_qS =

H = H_0 + H_S + H_qS

#Using the mesolver solve the schroedinger equations numerically 
#Will also need to find out which expectation values will need to calculate.



#Plot the results 



#Print the results for further analysis
