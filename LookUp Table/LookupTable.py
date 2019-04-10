from Constants import *
from math import *
import numpy as np
#import matplotlib.pyplt as plt

#Calculations of the Freuencies of the Qbits within a specific range

omega12   = 0
phi_bar12 = 0
omega3   = 0
phi_bar3 = 0
file12 = open("Lookup_tbl_12.dat","w")
file3 = open("Lookup_tbl_3.dat","w")

for i in range(1,1000):
	for j in range(1,1000):
		i1 = i * 0.1
		j1 = j * 0.1
		omega12   = (1 / (hbar * 2 * PI)) * sqrt(8 * E_CQ(j1) * (E_J(i1) + (4 * E_L(100e-9)))) * (1e-9)
		phi_bar12 = ((2*E_CQ(j1))/(E_J(i1) + (4 * E_L(100e-9))))**0.25

		omega3   = (1 / (hbar * 2 * PI)) * sqrt(8 * E_CQ(j1) * (E_J(i1) + (8 * E_L(100e-9)))) * (1e-9)
		phi_bar3 = ((2*E_CQ(j1))/(E_J(i1) + (8 * E_L(100e-9))))**0.25
		
		file12.write(str(i1) + " " + str(j1) + " " + str(omega12) + " " + str(phi_bar12) + "\n")
		file3.write(str(i1)  + " " + str(j1) + " " + str(omega3)  + " " + str(phi_bar3)  + "\n")

file12.close()
file3.close()