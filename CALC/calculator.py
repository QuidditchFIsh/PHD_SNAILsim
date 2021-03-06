
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
EL 		= E_L(L) 

print(EL/h * (1e-9))

