import numpy as np
from curtsies import Input
import time
running = True
while running:
	omegas = []
	data = []
	listening = True
	while listening:
		inpt = raw_input("Which Table would you like to look up?\nPress 1 for w_12 or 3 for w3:")
		if(inpt == '1'):
			search = 1
			break
		elif(inpt == '3'):
			search = 3
			break
		else:
			print("Please Press only 1 or 3")
		time.sleep(0.1)
	print("Loading Tables into Memory")
	if search == 1:
		with open("Lookup_tbl_12.dat") as f:
			for line in f:
				(EJ,ECQ,w,phiB) = line.split()
				omegas.append(float(w))
				data.append(float(EJ))
				data.append(float(ECQ))
				data.append(float(phiB))
		print("Loaded Table")
	else:
		with open("Lookup_tbl_3.dat") as f:
			for line in f:
				(EJ,ECQ,w,phiB) = line.split()
				omegas.append(float(w))
				data.append(float(EJ))
				data.append(float(ECQ))
				data.append(float(phiB))
		print("Loaded Table")
	freq = raw_input("Enter the frequency to search for in GHz:")
	for i in range(0,len(omegas)):
		if abs(float(omegas[i])-float(freq)) < 0.2:
			print(str(omegas[i]) + " " + str(data[(i * 3)+ 0])+ " " + str(data[(i * 3)+ 1])+ " " + str(data[(i * 3)+ 2]) + "\n")
	inpt = raw_input("Would you like to search for another Frequency (y/n):")
	if inpt == 'n':
		running = False
