'''
Author: Aneirin John Baker
Date:11/07/19
Description:Script to hold all of the constants for this simulation. Will also hold some functions to calculate the energies associated with 
some of the terms in the Hamiltonian.
'''
#Function to calculate Energies 
def E_J (i): return i * (1e9) * h

def E_L (l): return (phi0 ** 2)/(2 * l)

def E_CQ(C): return (e ** 2) / (2 * C * 1e-15)

#Basic constants
PI 		= 3.14159265359
PI2 	= 2 * PI
PId4 	= PI / 4 
h 		= 6.62607004e-34
hbar 	= h / (PI2)
e 		= 1.60217662e-19
phi0 	= hbar/(2*e)


#Constants for the Hamiltonian
Cq1 	= 1
Cq2		= 1 
Cq3		= 1

#These energies should have units of frequency
ECQ1	= 0.4
ECQ2	= 1
ECQ3	= 1.3
EJ1 	= 13
EJ2 	= 33
EJ3 	= 72.25
ECA 	= ECQ1 + ECQ2 + ECQ3
EC 		= 1
#coupling between the qubit and squid
EJ 		= 1
#Drive constants in GHz
omega1 = 4
omega2 = 10
omega3 = 17
omegaA = 8.5

#Constants for the Hamiltonian
q1_Bar = 0.5
q2_Bar = 0.5
q3_Bar = 0.5
sp_Bar = 0.5

w1 = 4
w2 = 10
w3 = 17
wp = 35

third = 0.333333333333333333333333
sixth = third * 0.5



