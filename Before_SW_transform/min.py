import numpy as np 

file0 = open('/home/nye/PhD/PHD_SNAILsim/Before_SW_transform/Output/Toffoli_10-09-19/fidelity000-4_10_17.dat','r')
file1 = open('/home/nye/PhD/PHD_SNAILsim/Before_SW_transform/Output/Toffoli_10-09-19/fidelity111-4_10_17.dat','r')

f000=[]
f111=[]
for line in file0:
	f000.append(float(line))
for line in file1:
	f111.append(float(line))

minfid = []

for i in range(0,len(f000)):
	minfid.append(min(f000[i],f111[i]))

with open('minFidelity.dat','w') as file2:
	for j in minfid:
		file2.write(str(j) + "\n")

