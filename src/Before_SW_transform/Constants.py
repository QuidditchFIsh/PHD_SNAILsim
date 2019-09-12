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
h 		= 6.62607004e-34
hbar 	= h / (PI2)
e 		= 1.60217662e-19
phi0 	= hbar/(2*e)


#Constants for the Hamiltonian
phiDC 	= PI / 4
phiAC	= 0.1

L 		= 100e-9
Cq1 	= 1
Cq2		= 1 
Cq3		= 1

#These energies should have units of frequency
ECQ1	= E_CQ(Cq1) * (1/h)
ECQ2	= E_CQ(Cq2) * (1/h)
ECQ3	= E_CQ(Cq3) * (1/h)
EJ1 	= 1 * (1/h)
EJ2 	= 1 * (1/h)
EJ3 	= 1 * (1/h)
EL 		= E_L(L) * (1/h) * 1e-9

#coupling between the qubit and squid
EJ 		= 0.01 
#Drive constants in GHz
omega1d = 4
omega2d = 10
omega3d = 17

#Constants for the Hamiltonian
q1_Bar = 1
q2_Bar = 1
q3_Bar = 1
sp_Bar = 1
sm_Bar = 1.7

w1 = 4
w2 = 10
w3 = 17
wp = 35
wm = 3




