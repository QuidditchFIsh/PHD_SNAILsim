'''
Author : Aneirin John Baker
Date 10/12/2018
Description : File to store all of the physical constants which will be needed in this project ( All to a high degre of accuracy). Alsi will store all of the variables usually used in 
this package such as insuctance, Josephson Energy, capcticance etc
'''
from math import *

# Define functions for the energy of Inductance Capaticance etc

def E_J (i): return i * (1e9) * h

def E_L (l): return (phi0 ** 2)/(2 * l)

def E_CQ(C): return (e ** 2) / (2 * C * 1e-15)

def CHI(phi_M): return exp((phi_M ** 2)/2)

def CHIprime(phi_M): return exp((phi_M ** 2)/18)

def calc_U(ECQ,EJ,El): return(ECQ/(2*hbar) * ((EJ)/((EJ) + (4 * El))) * 1e-9)

def calc_phiBar(ECQ,EJ,El): return(((2 * ECQ)/((EJ) + (4 * El)))**0.25)

def calc_U3(ECQ,EJ,El): return(ECQ/(2*hbar) * ((EJ)/((EJ) + (8 * El))) * 1e-9)

def calc_phiBar3(ECQ,EJ,El): return(((2 * ECQ)/((EJ) + (8 * El)))**0.25)

e = 1.60217662e-19 # Charge on the Electron
#e = 1

h = 6.626070040e-34 #  planks constant
#h = 1

PI = 3.14159265359 

hbar = h / (2*PI) # reduced planks constant

L = 100e-9 # Inductace 

phi0 = (hbar) / (2 * e) # Quantum of Flux

phibar1 = 0
phibar2 = 0
phibar3 = 0
#phibarP = 0
#phibarM = 0

omega1 = 0
omega2 = 0
omega3 = 0

U1 = 0
U2 = 0
U3 = 0

EJT = 0.1
ECQ1 = 0
ECQ2 = 0
ECQ3 = 0

EJ1 = 0
EJ2 = 0
EJ3 = 0

#EJ =10 * h

CG = 1
EL = E_L(L)



'''
print((1/(hbar)) * sqrt(8 * ECQ1 *((EJ1 * h * 1e9 ) + (4*EL))) * 1e-9)
print(ECQ1/(2*hbar) * ((EJ1 * h * 1e9 )/((EJ1 * 1e9 * h) + (4 * EL))) * 1e-9)
print(((2 * ECQ1)/((EJ1 * h * 1e9) + (4 * EL)))**0.25)

print((1/(hbar)) * sqrt(8 * ECQ2 *((EJ2 * h * 1e9 ) + (4*EL))) * 1e-9)
print(ECQ2/(2*hbar) * ((EJ2 * h * 1e9 )/((EJ2 * 1e9 * h) + (4 * EL))) * 1e-9)
print(((2 * ECQ2)/((EJ2 * h * 1e9) + (4 * EL)))**0.25)

print((1/(hbar)) * sqrt(8 * ECQ3 *((EJ3 * h * 1e9 ) + (8*EL))) * 1e-9)
print(ECQ3/(2*hbar) * ((EJ3 * h * 1e9 )/((EJ3 * 1e9 * h) + (8 * EL))) * 1e-9)
print(((2 * ECQ3)/((EJ3 * h * 1e9) + (8 * EL)))**0.25)
'''
