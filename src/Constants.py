'''
Author : Aneirin John Baker
Date 10/12/2018
Description : File to store all of the physical constants which will be needed in this project ( All to a high degre of accuracy). Alsi will store all of the variables usually used in 
this package such as insuctance, Josephson Energy, capcticance etc
'''


# Define functions for the energy of Inductance Capaticance etc

def E_J (i): return i * (1e9) * h

def E_L (l): return (phi0 ** 2)/(2 * l)

def E_CQ(C): return (e ** 2) / (2 * C * 1e-15)

def CHI(phi_M): return exp((phi_M ** 2)/2)

def CHIprime(phi_M): return exp((phi_M ** 2)/18)

#e = 1.60217662e-19 # Charge on the Electron
e = 1

h = 6.626070040e-34 #  planks constant
#h = 1

PI = 3.14159265359 

hbar = h / (2*PI) # reduced planks constant

L = 100e-9 # Inductace 

phi0 = (hbar) / (2 * e) # Quantum of Flux

phibar1 = 0.24
phibar2 = 0.38
phibar3 = 0.55
phibarP = 0.3
phibarM = 0.3

omega1 = 10
omega2 = 16
omega3 = 28

U1 = 0
U2 = 0
U3 = 0

EJT = 63

ECQ1 = E_CQ(130)
ECQ2 = E_CQ(33)
ECQ3 = E_CQ(9)

EJ1 = 91
EJ2 = 54
EJ3 = 39

EJ =10 * h

CG = 1
EL = E_L(L)

