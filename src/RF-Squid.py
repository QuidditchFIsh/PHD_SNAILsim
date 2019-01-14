
'''
Author: Aneirin John Baker
Date : 14/01/2019
Description:Simulation of an RF Squid potential without the Hamiltonain for the RF squid to make things simpler. 
This siulation will be compared to the full simulation afterwards
'''
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time

#Define the time dependant terms in the Hamiltonian as functions to be called
omega = 0
Amplitude = 0

def H1_Coeff(t,*args):
	return Amplitude * cos(omega * t)
def H1_coeff_off(t,*args):
	return 1

#Constants will be defined in the constants class

print("============================================")
print("Begining Program, setting up calculations")

N = 2
q1 = tensor(destroy(N),qeye(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N),qeye(N))
q4 = tensor(qeye(N),qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()
q4d = q4.dag()

phi1 = phibar1 * (q1 + q1d)
phi2 = phibar2 * (q2 + q2d)
phi3 = phibar3 * (q3 + q3d)
phi4 = phibar4 * (q4 + q4d)

H0 = 0
H1 = 0

H0 += (omega1 * q1d * q1) + (U1 * q1d * q1d * q1 * q1)
H0 += (omega2 * q2d * q2) + (U2 * q2d * q2d * q2 * q2)
H0 += (omega3 * q3d * q3) + (U3 * q3d * q3d * q3 * q3)
H0 += (omega4 * q4d * q4) + (U4 * q4d * q4d * q4 * q4)


#Prepareing the rest of the calculations
tlist1 = np.linspace(0, 50, 200)#Time for equlibrium
tlist2 = np.linspace(50, 200, 400)#Time for Evolution of the Time dependant hamiltonian

#Basis states
psi_list = []
psi_list.append(basis(2,0))
for n in range(3):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)

#collapse operator list
c_op_list = [q1,q2,q3,q4]

#operators to be evaulated
sz1 = tensor(sigmaz(),qeye(N),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz(),qeye(N))
sz4 = tensor(qeye(N),qeye(N),qeye(N),sigmaz())

eval_op_list = [sz1,sz2,sz3,sz4]

Hon = [H0,[H1,H1_coeff]]
Hoff = [H0,[H1,H1_coeff_off]]