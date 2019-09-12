from math import *

omega1 = 5;omega2=5;omega3=5

for t in range(0,10):
	print((cos((omega1 - omega2 + omega3) * t) + (0 + 1j)*sin((omega1 - omega2 + omega3) * t)) * (cos((omega1 - omega2 + omega3) * t) - (0 + 1j)*sin((omega1 - omega2 + omega3) * t)))