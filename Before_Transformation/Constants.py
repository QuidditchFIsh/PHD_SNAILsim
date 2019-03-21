from math import *
import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
import Constants as cons
#Basic definitions
e = 1.60217662e-19 # Charge on the Electron
#e = 1

h = 6.626070040e-34 #  planks constant
#h = 1

PI = 3.14159265359 

hbar = h / (2*PI) # reduced planks constant

L = 100e-9 # Inductace 

phi0 = (hbar) / (2 * e) # Quantum of Flux

R = 1/sqrt(2) * (sigmay() + sigmaz()) #Rotation Matrix

one  = R*basis(2,1)#Basis vetors
zero = R*basis(2,0)

a = R * sigmap() * R # anhilation operator

i = qeye(2) # Identity

#Definitions for the frequencies and their strengths
'''
E_L = 

E_CQ1 = 
E_CQ2 = 
E_CQ3 = 

E_J1 = 
E_J2 = 
E_J3 = 
'''
E_J = 0.1
phiAC = 0.1

omega1 = 20
omega2 = 15
omega3 = 8
omegaP = 0.1
omegaM = 0.1

phi_Bar1 = 0.656
phi_Bar2 = 0.568
phi_Bar3 = 0.414
phi_BarP = 0.5 # placeholder check this value
phi_BarM = 0.5 # placeholder check this value

U1 = 5.8
U2 = 3.27
U3 = 1.04

#Begin by defining all of tge variables to use

q1 = tensor(a,i,i,i,i)
q2 = tensor(i,a,i,i,i)
q3 = tensor(i,i,a,i,i)
sP = tensor(i,i,i,a,i)
sM = tensor(i,i,i,i,a)

phi1 = phi_Bar1 * (q1 + q1.dag())
phi2 = phi_Bar2 * (q2 + q2.dag())
phi3 = phi_Bar3 * (q3 + q3.dag())
phiM = phi_BarP * (sM + sM.dag())
phi1 = phi_BarM * (q1 + q1.dag())

phi_qM = (phi1 + phi2 - 2*phi3)
