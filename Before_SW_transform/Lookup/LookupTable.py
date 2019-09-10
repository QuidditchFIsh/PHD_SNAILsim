from Constants import *
from math import *
#import matplotlib.pyplt as plt

#Calculations of the Freuencies of the Qbits within a specific range

omega   = 0
phi_bar = 0
file	= open("Lookup_tbl.dat","w")

for i in range(10,1200):
	for j in range(100,1200):
		i1 = i * 0.1 # EJ
		j1 = j * 0.1 # ECQ
		omega   =  (1/h)*sqrt(8*E_CQ(j1) * E_J(i1)) # frequencies in natural frequency units (Giga Hertz)
		phi_bar = ((E_CQ(j1))/(E_J(i1)))**0.25 # strength No units
		
		file.write(str(i1) + " " + str(j1) + " " + str(omega) + " " + str(phi_bar) + "\n")

file.close()	