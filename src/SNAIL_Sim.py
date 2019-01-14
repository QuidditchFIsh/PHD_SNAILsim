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

qM = q1 + q2 - q3
qP = q1 + q2 + q4

times = np.linspace(0.0 , 20.0 , 400) #Test parameters will need changing when start real simulations.


phiBar_1 = ((2 * E_CQ(1))/(E_J(1) + 4 * E_L(1))) ** 0.25
phiBar_2 = ((2 * E_CQ(1))/(E_J(1) + 4 * E_L(1))) ** 0.25
phiBar_3 = ((2 * E_CQ(1))/(E_J(1) + 8 * E_L(1))) ** 0.25
phiBar_P = ((2 * E_CQ(1))/(E_J(1) + 4 * E_L(1))) ** 0.25
phiBar_M = ((2 * E_CQ(1))/(E_J(1) + 4 * E_L(1))) ** 0.25


phi_1 = phiBar_1 * (q1 + q1.dag())
phi_2 = phiBar_2 * (q2 + q2.dag())
phi_3 = phiBar_3 * (q3 + q3.dag())
phi_P = phiBar_P * (sP + sP.dag())
phi_M = phiBar_M * (sM + sM.dag())

##################These need to be complex##################
phi_1 = (-1 * hbar)/(2 * phiBar_1) * (q1 - q1.dag())
phi_2 = (-1 * hbar)/(2 * phiBar_2) * (q2 - q2.dag())
phi_3 = (-1 * hbar)/(2 * phiBar_3) * (q3 - q3.dag())
phi_P = (-1 * hbar)/(2 * phiBar_P) * (sP - sP.dag())
phi_M = (-1 * hbar)/(2 * phiBar_M) * (sM - sM.dag())
#########################################################

#Defining the frequencies which are needed for the simulation
omega_1 = (1 / hbar) * sqrt(8 * E_CQ(1) * (E_J(1) + 4 * E_L(1)))
omega_2 = (1 / hbar) * sqrt(8 * E_CQ(1) * (E_J(1) + 4 * E_L(1)))
omega_3 = (1 / hbar) * sqrt(8 * E_CQ(1) * (E_J(1) + 8 * E_L(1)))

U_1 = ((E_CQ(1))/(2 * hbar)) * ((E_J(1))/(E_J(1) + 4 * E_L(1)))
U_2 = ((E_CQ(1))/(2 * hbar)) * ((E_J(1))/(E_J(1) + 4 * E_L(1)))
U_3 = ((E_CQ(1))/(2 * hbar)) * ((E_J(1))/(E_J(1) + 8 * E_L(1)))

omega_P = (4 / hbar) * sqrt(E_CP * E_L(1))
omega_M = (4 / hbar) * sqrt(E_CM * E_L(1))
####################Will need to define E_CM and E_CP##########

#Also will need to inlcude the driving term will need to ask how to peform that


#Now define the Hamiltonian using all of the Constants and variables. Will define the Hamiltonian in severl parts
#This simulation will be for both the squid and snail.
H_0      = (hbar * omega_1 * q1.dag() * q1 - hbar * U_1 * q1.dag() * q1.dag() * q1 * q1)
 + (hbar * omega_2 * q2.dag() * q2 - hbar * U_2 * q2.dag() * q2.dag() * q2 * q2) + (hbar * omega_3 * q3.dag() * q3 - hbar * U_3 * q3.dag() * q3.dag() * q3 * q3)
H_Snail  = hbar * omega_M * sM.dag() * sM # Not sure about this check it with the theory Write down all the lagrangians which you are using
H_qSnail = -3 * E_J(1) * XX * CHIprime(1) * qM + ((1/6) * alpha * E_J(1) * CHIprime(1) + 3 * E_J(1) * XX * CHIprime(1)) * qM * qM + qM * qM * qM * (1/54) * 3 * E_J(1) * XX * CHIprime(1)
H_Squid  = hbar * omega_P * sP.dag() * sP + hbar * omega_M * sM.dag() * sM
H_qSquid = - E_J(1) * CHI(1) * (qM * XX - qM * qM * XX + qM * qM * qM * XX)


<<<<<<< HEAD
############ Will need to put in the expressions for these######
H_0  = 
H_S  = 
H_qS =
################################################################
H = H_0 + H_S + H_qS
=======
H_snail_full = H_0 + H_Snail + H_qSnail
H_Squid_full = H_0 + H_Squid + H_qSquid 

>>>>>>> fb1fe3e737322c139bd8b571779cbbb2e4adae91

#Using the mesolver solve the schroedinger equations numerically 
#Will also need to find out which expectation values will need to calculate.



#Plot the results 



#Print the results for further analysis
