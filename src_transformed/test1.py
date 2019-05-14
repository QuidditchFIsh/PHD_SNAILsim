from math import *

omega1 = 5
for i in range(0,100):
	i1 = i * 0.1
	print(cos(omega1 * i1 + 1.57) * (cos(omega1*i1) + (0+1j)*sin(omega1*i1)))
	print((0.5*1j)*(((cos(omega1*i1) + (0+1j)*sin(omega1*i1))) - ((cos(omega1*i1) - (0+1j)*sin(omega1*i1))))*(cos(omega1*i1) + (0+1j)*sin(omega1*i1)))
	print("===================================")