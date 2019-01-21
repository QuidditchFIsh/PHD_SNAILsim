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

e = 1.60217662e-19 # Charge on the Electron
#e = 1

h = 6.626070040e-34 #  planks constant
#h = 1

PI = 3.14159265359 

hbar = h / (2*PI) # reduced planks constant

L = 100e-9 # Inductace 

phi0 = (hbar) / (2 * e) # Quantum of Flux

phibar1 = 0.423503325645
phibar2 = 0.575396830011
phibar3 = 0.554480114963
#phibarP = 0
#phibarM = 0

omega1 = 169.64
omega2 = 163.38
omega3 = 175.938

U1 = 3.64
U2 = 6.2
U3 = 5.79

EJT = 63

ECQ1 = E_CQ(16)
ECQ2 = E_CQ(9)
ECQ3 = E_CQ(9)

EJ1 = 72
EJ2 = 36
EJ3 = 39

EJ =10 * h

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


26.9998356504 72.0 16.0 0.423503325646
26.0026322606 36.0 9.0 0.575396830014
28.001435245 39.0 9.0 0.554480114968
0.137657147912

5.59807404012 3.0 31.0 0.668185751905
16.7979786878 55.0 32.0 0.379659153049
28.001435245 39.0 9.0 0.554480114968
0.143306392178

'''
