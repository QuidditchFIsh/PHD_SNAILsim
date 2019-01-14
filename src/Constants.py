'''
Author : Aneirin John Baker
Date 10/12/2018
Description : File to store all of the physical constants which will be needed in this project ( All to a high degre of accuracy). Alsi will store all of the variables usually used in 
this package such as insuctance, Josephson Energy, capcticance etc
'''

e = 1.60217662e-19 # Charge on the Electron

h = 6.626070040e-34 #  planks constant

PI = 3.14159265359 

hbar = h / (2*PI) # reduced planks constant

L = 100e-9 # Inductace 

phi0 = (hbar) / (2 * e) # Quantum of Flux

phibar1 = 1
phibar2 = 1
phibar3 = 1
phibar4 = 1

omega1 = 1
omega2 = 1
omega3 = 1
omega4 = 1

U1 = 1
U2 = 1
U3 = 1
U4 = 1


# Define functions for the energy of Inductance Capaticance etc

def E_J (i): return i * (1e9) * h

def E_L (l): return (phi0 ** 2)/(2 * l)

def E_CQ(C): return (e ** 2) / (2 * C * 1e-15)








