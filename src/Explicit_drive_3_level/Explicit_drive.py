import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
from Functions import *
from Constants import *



R = 1/sqrt(2) * Qobj([[1+0j,0-1j,0],[0+1j,-1+0j,0],[0,0,1]])
#R=1
one  =  R*basis(3,1)
zero =  R*basis(3,0)
two  =  R*basis(3,2)

X = jmat(1,'x')
Y = jmat(1,'y')
Z = jmat(1,'z')

a =  destroy(3) 

q1 = tensor(a, qeye(3),qeye(3))
q2 = tensor(qeye(3),a,qeye(3))
q3 = tensor(qeye(3),qeye(3),a)


q1_before = tensor(destroy(3), qeye(3),qeye(3))
q2_before = tensor(qeye(3),destroy(3),qeye(3))
q3_before = tensor(qeye(3),qeye(3),destroy(3))

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(3),qeye(3),qeye(3))


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,250,num=250)
#R = 1/sqrt(2) * (sigmay() + sigmaz())
R=1
sx1 = tensor(R * X * R,qeye(3),qeye(3))
sx2 = tensor(qeye(3), R * X * R,qeye(3))
sx3 = tensor(qeye(3),qeye(3), R * X * R)

sy1 = tensor(R * Y * R,qeye(3),qeye(3))
sy2 = tensor(qeye(3), R * Y * R,qeye(3))
sy3 = tensor(qeye(3),qeye(3), R * Y * R)

sz1 = tensor(R * Z * R,qeye(3),qeye(3))
sz2 = tensor(qeye(3), R * Z * R,qeye(3))
sz3 = tensor(qeye(3),qeye(3), R * Z * R)

H0 = omega1 * 0.25*q1.dag()*q1 + omega2 * 0.25*q2.dag()*q2 + omega3 * 0.25*q3.dag()*q3 + U1 * 0.0625*q1.dag() * q1.dag() * q1 * q1 + U2 * 0.0625* q2.dag() * q2.dag() * q2 * q2 + U3 * 0.0625* q3.dag() * q3.dag() * q3 * q3

#Full Hamiltonian
H = [H0,\
#interaction part of the Hamiltonian
[-1*0.5*q3,Q3],[-1*0.5*q3.dag(),Q3d],\

[-1*0.5*q2,Q2],[-1*0.5*q2.dag(),Q2d],\

[-1*0.5*q1,Q1],[-1*0.5*q1.dag(),Q1d],\

[two_third*0.25*q2*q3,Q23],[two_third*0.25*q2*q3.dag(),Q23d],[two_third*0.25*q2.dag()*q3,Q2d3],[two_third*0.25*q2.dag()*q3.dag(),Q2d3d],\

[two_third*0.25*q1*q3,Q13],[two_third*0.25*q1*q3.dag(),Q13d],[two_third*0.25*q1.dag()*q3,Q1d3],[two_third*0.25*q1.dag()*q3.dag(),Q1d3d],\

[two_third*0.25*q1*q2,Q12],[two_third*0.25*q1*q2.dag(),Q12d],[two_third*0.25*q1.dag()*q2,Q1d2],[two_third*0.25*q1.dag()*q2.dag(),Q1d2d],\

[two_third*0.125*q1*q2*q3,Q123],[two_third*0.125*q1*q2*q3.dag(),Q123d],\
[two_third*0.125*q1*q2.dag()*q3,Q12d3],[two_third*0.125*q1.dag()*q2*q3,Q1d23],\
[two_third*0.125*q1*q2.dag()*q3.dag(),Q12d3d],[two_third*0.125*q1.dag()*q2*q3.dag(),Q1d23d],\
[two_third*0.125*q1.dag()*q2.dag()*q3,Q1d2d3],[two_third*0.125*q1.dag()*q2.dag()*q3.dag(),Q1d2d3d],\
#Perturbations to the Hamiltonian from off resonant terms in the drive
[two_third*0.25*q1.dag()*q1,Q1],[two_third*0.25*q2.dag()*q2,Q1],[two_third*0.25*q3.dag()*q3,Q1],\
[third*0.125*q1.dag()*q1*q2,Q2],[third*0.125*q1.dag()*q1*q2.dag(),Q2d],[third*0.125*q1*q1.dag()*q2.dag(),Q2d],[third*0.125*q1*q1.dag()*q2,Q2] ,\
[third*0.125*q1.dag()*q1*q3,Q3],[third*0.125*q1.dag()*q1*q3.dag(),Q3d],[third*0.125*q1*q1.dag()*q3.dag(),Q3d],[third*0.125*q1*q1.dag()*q3,Q3] ,\
[third*0.125*q2.dag()*q2*q3,Q3],[third*0.125*q2.dag()*q2*q3.dag(),Q3d],[third*0.125*q2*q2.dag()*q3.dag(),Q3d],[third*0.125*q2*q2.dag()*q3,Q3] ,\
[third*0.125*q1*q2*q2.dag(),Q1],[third*0.125*q1.dag()*q2*q2.dag(),Q1d],[third*0.125*q1.dag()*q2.dag()*q2,Q1] ,[third*0.125*q1*q2.dag()*q2,Q1d],\
[third*0.125*q1*q3*q3.dag(),Q1],[third*0.125*q1.dag()*q3*q3.dag(),Q1d],[third*0.125*q1.dag()*q3.dag()*q3,Q1] ,[third*0.125*q1*q3.dag()*q3,Q1d],\
[third*0.125*q2*q3*q3.dag(),Q2],[third*0.125*q2.dag()*q3*q3.dag(),Q2d],[third*0.125*q2.dag()*q3.dag()*q3,Q2] ,[third*0.125*q2*q3.dag()*q3,Q2d],\
]
c_ops = []

outputstr = ''

#freqs = np.genfromtxt('Frequencies3.dat')
freqs = [[4,10,17]]
for j in freqs:
	omega1   	= j[0]
	omega2   	= j[1]
	omega3   	= j[2]
	f1 			= j[0]
	f2 			= j[1]
	f3 			= j[2]
	for i in range(1,2):
		if i == 0:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_04-09-19/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_04-09-19/occupation_q1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_04-09-19/occupation_q2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_04-09-19/occupation_q3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_04-09-19/sz1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_04-09-19/sz2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_04-09-19/sz3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000 Full Drive')
			result = mesolve(H,psi0,tlist,c_ops,[sy1,sy2,sy3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 1:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_04-09-19/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_04-09-19/occupation_q1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_04-09-19/occupation_q2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_04-09-19/occupation_q3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_04-09-19/sz1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_04-09-19/sz2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_04-09-19/sz3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111 Full Drive')
			result = mesolve(H,psi0,tlist,c_ops,[sy1,sy2,sy3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
	outputstr = 'Output/Toffoli_RWA_04-09-19/'
	fidelity_dat = []

	Qubit_state_1_0 = []
	Qubit_state_1_1 = []
	Qubit_state_1_2 = []

	Qubit_state_2_0 = []
	Qubit_state_2_1 = []
	Qubit_state_2_2 = []

	Qubit_state_3_0 = []
	Qubit_state_3_1 = []
	Qubit_state_3_2 = []

	Expect_sz1 = []
	Expect_sz2 = []
	Expect_sz3 = []

	#print(result.states[0])

	for j in range(0,len(tlist)):
	 		fidelity_dat.append(fidelity(result.states[j],Tdm))
	 		Qubit_state_1_0.append(expect(result.states[j].ptrace(0),zero).real)
	 		Qubit_state_1_1.append(expect(result.states[j].ptrace(0),one).real)
	 		Qubit_state_1_2.append(expect(result.states[j].ptrace(0),two).real)

	 		Qubit_state_2_0.append(expect(result.states[j].ptrace(1),zero).real)
	 		Qubit_state_2_1.append(expect(result.states[j].ptrace(1),one).real)
	 		Qubit_state_2_2.append(expect(result.states[j].ptrace(1),two).real)

	 		Qubit_state_3_0.append(expect(result.states[j].ptrace(2),zero).real)
	 		Qubit_state_3_1.append(expect(result.states[j].ptrace(2),one).real)
	 		Qubit_state_3_2.append(expect(result.states[j].ptrace(2),two).real)

	 		Expect_sz1.append(result.expect[0][j])
			Expect_sz2.append(result.expect[1][j])
			Expect_sz3.append(result.expect[2][j])

	with open(outputstr + 'Qubit_state_1_0.dat','w') as f1:
		for j in Qubit_state_1_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_1_1.dat','w') as f1:
		for j in Qubit_state_1_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_1_2.dat','w') as f1:
		for j in Qubit_state_1_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Qubit_state_2_0.dat','w') as f1:
		for j in Qubit_state_2_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_2_1.dat','w') as f1:
		for j in Qubit_state_2_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_2_2.dat','w') as f1:
		for j in Qubit_state_2_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Qubit_state_3_0.dat','w') as f1:
		for j in Qubit_state_3_0:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_3_1.dat','w') as f1:
		for j in Qubit_state_3_1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Qubit_state_3_2.dat','w') as f1:
		for j in Qubit_state_3_2:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Fidelity.dat','w') as f1:
		for j in fidelity_dat:
			f1.write(str(j) + "\n")

	with open(outputstr + 'Expect_sz1.dat','w') as f1:
		for j in Expect_sz1:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Expect_sz2.dat','w') as f1:
		for j in Expect_sz2:
			f1.write(str(j) + "\n")
	with open(outputstr + 'Expect_sz3.dat','w') as f1:
		for j in Expect_sz3:
			f1.write(str(j) + "\n")