import numpy as np

x = np.genfromtxt('Frequencies2')

for i in x:
	for j in i:
		j = float(j)

print(x)