import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import Constants as cons

#Set up the equations
def H1_Coeff_On(t,*args):
	return 0.125 * cos(35 * t) + 0.125 * cos(105 * t) + 0.125 * cos(176 * t)+ 0.0625 * cos(281 * t)+ 0.0625 * cos(71 * t)+ 0.0625 * cos(211 * t)+ 0.0625 * cos(141 * t)+ 0.0625 * cos(140 * t)+ 0.0625 * cos(70 * t)+ 0.03125 * cos(316 * t)+ 0.03125 * cos(36 * t)+ 0.03125 * cos(106 * t)+ 0.03125 * cos(246 * t)

print("============================================")
print("Begining Program, setting up calculations")
#Variables
N = 2 # Number of states in the system

avg_sz1 = []#Average sigma z value for each QuBit
avg_sz2 = []
avg_sz3 = []

fidelity111 = []#Fiedlity variables
fidelity110 = []
fidelity101 = []
fidelity011 = []
fidelity100 = []
fidelity010 = []
fidelity001 = []

H0 = 0#Define the time independant and dependant hamiltonian
H1 = 0

psi_list = []

q1 = tensor(destroy(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()

phi1 = cons.phibar1 * (q1 + q1d)
phi2 = cons.phibar2 * (q2 + q2d)
phi3 = cons.phibar3 * (q3 + q3d)

psi_list.append((basis(2,0)-(0+1j)*basis(2,1)).unit())
for n in range(2):
    psi_list.append((basis(2,0) - (0 + 1j)*basis(2,1)).unit())
psi0 = tensor(psi_list)

sz1 = tensor(sigmaz(),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz())
eval_op_list = [sz1,sz2,sz3]

tlist = np.linspace(0, 50, 2000)


H0 += (cons.omega1 * q1d * q1) + (cons.U1 * q1d * q1d * q1 * q1)
H0 += (cons.omega2 * q2d * q2) + (cons.U2 * q2d * q2d * q2 * q2)
H0 += (cons.omega3 * q3d * q3) + (cons.U3 * q3d * q3d * q3 * q3)

H1 += 0.25  * cons.EJT * (phi1 + phi2 - (2 * phi3))**2

H1 += 0.5 * cons.EJT * phi1 * phi2 * phi3
print

H = [H0,[H1,H1_Coeff_On]]
#import the data

input = []
print("Begining Calcultions")
start = time.time()
with open('gen_freq/Optimization_Output.dat','r') as f:
	for line in f:
		input = line.split()
input = [float(i) for i in input]

Notrials = len(input) / 9

for i in range(0,Notrials):
	#set all the simulation parameters
	cons.omega1 = input[(i*9) + 0]
	cons.omega2 = input[(i*9) + 3]
	cons.omega3 = input[(i*9) + 6]

	cons.ECQ1 = cons.E_CQ(input[(i*9) + 2])
	cons.ECQ2 = cons.E_CQ(input[(i*9) + 5])
	cons.ECQ3 = cons.E_CQ(input[(i*9) + 8])

	cons.EJ1 = cons.E_J(input[(i*9) + 1])
	cons.EJ1 = cons.E_J(input[(i*9) + 4])
	cons.EJ1 = cons.E_J(input[(i*9) + 7])

	cons.U1 = cons.calc_U(cons.ECQ1,cons.EJ1,cons.EL)
	cons.U2 = cons.calc_U(cons.ECQ2,cons.EJ2,cons.EL)
	cons.U3 = cons.calc_U3(cons.ECQ3,cons.EJ3,cons.EL)

	cons.phibar1 = cons.calc_phiBar(cons.ECQ1,cons.EJ1,cons.EL)
	cons.phibar2 = cons.calc_phiBar(cons.ECQ2,cons.EJ2,cons.EL)
	cons.phibar3 = cons.calc_phiBar3(cons.ECQ3,cons.EJ3,cons.EL)
 	#Calculate the ressulting density matrix
 	H0 = 0
 	H1 = 0
 	H0 += (cons.omega1 * q1d * q1) + (cons.U1 * q1d * q1d * q1 * q1)
	H0 += (cons.omega2 * q2d * q2) + (cons.U2 * q2d * q2d * q2 * q2)
	H0 += (cons.omega3 * q3d * q3) + (cons.U3 * q3d * q3d * q3 * q3)

	H1 += 0.25  * cons.EJT * (phi1 + phi2 - (2 * phi3))**2

	H1 += 0.5 * cons.EJT * phi1 * phi2 * phi3

	H = [H0,[H1,H1_Coeff_On]]
 	print(H)
 	print("==============================")
 	#result = mesolve(H,psi0,tlist,c_op_list,eval_op_list,options = Options(nsteps = 8000,store_final_state = True,store_states = True))