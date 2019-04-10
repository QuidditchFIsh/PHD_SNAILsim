from math import *
omega1 = 10
omega2 = 23
omegad1 = omega1 + omega2
omegad2 = omega1 - omega2
omegad3 = omega1
omegad4 = omega2
PI = 3.14159256
with open("CNOT_drive.dat","w") as file:
	for i in range(0,20)0ajb:
		t = i * 0.01
		x = 0.25*(cos(omegad1 * t + 0.5*PI) + cos(omegad2*t + 0.5*PI) + 1*cos(omegad3*t + 0.5*0) + 1*cos(omegad4*t+ 0.5*PI))
		file.write(str(x) + "\n")