import numpy as np
import time
running = True
while running:
	omegas = []
	data = []

	print("Loading Tables into Memory")
	with open("Lookup_tbl.dat") as f:
		for line in f:
			(EJ,ECQ,w,phiB) = line.split()
			omegas.append(float(w))
			data.append(float(EJ))
			data.append(float(ECQ))
			data.append(float(phiB))
		print("Loaded Table")
	freq = raw_input("Enter the frequency to search for in GHz:")
	for i in range(0,len(omegas)):
		if abs(float(omegas[i])-float(freq)) < 0.01:
			print(str(omegas[i]) + " " + str(data[(i * 3)+ 0])+ " " + str(data[(i * 3)+ 1])+ " " + str(data[(i * 3)+ 2]) + "\n")
	inpt = raw_input("Would you like to search for another Frequency (y/n):")
	if inpt == 'n':
		running = False
