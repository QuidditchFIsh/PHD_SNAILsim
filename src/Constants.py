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

alpha = 0.3 # Size of smallest Josephson Junction in the SNAIL

# Define functions for the energy of Inductance Capaticance 

def E_J (i): return i * (1e9) * h

def E_L (l): return (phi0 ** 2)/(2 * l)

def E_CQ(C): return (e ** 2) / (2 * C * 1e-15)

def CHI(phi_M): return exp((phi_M ** 2)/2)

def CHIprime(phi_M): return exp((phi_M ** 2)/18)








