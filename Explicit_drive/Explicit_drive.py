import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
from Functions import *
from Constants import *



R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = basis(2,1)
zero = basis(2,0)

a =  R*sigmap()*R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

q1_before = tensor(sigmap(), qeye(2),qeye(2))
q2_before = tensor(qeye(2),sigmap(),qeye(2))
q3_before = tensor(qeye(2),qeye(2),sigmap())

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(2),qeye(2),qeye(2))


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,5,num=500)
#R = 1/sqrt(2) * (sigmay() + sigmaz())
R=1
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R)

#H2 = EJ *(I - s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
H2 = (I - sz1)*(I - sz2)*(I - sx3)

#Full Hamiltonian
'''
H = [[0.5 * 0.5 * q1,Q1],[0.5 * 0.5 * q1.dag(),Q1_d],[0.5 * 0.5 * q2,Q2],[0.5 * 0.5 * q2.dag(),Q2_d],[0.5 * q3,Q3],[0.5 * q3.dag(),Q3_d],
[0.25 * 0.25 * q1*q2,Q1_Q2],[0.25 * 0.25 * q1*q2.dag(),Q1_Q2d],[0.25 * 0.25 * q1.dag()*q2,Q1d_Q2],[0.25 * 0.25 * q1.dag()*q2.dag(),Q1d_Q2d],
[0.25 * 0.5 * q1*q3,Q1_Q3],[0.25 * 0.5 * q1*q3.dag(),Q1_Q3d],[0.25 * 0.5 * q1.dag()*q3,Q1d_Q3],[0.25 * 0.5 * q1.dag()*q3.dag(),Q1d_Q3d],
[0.25 * 0.5 * q2*q3,Q2_Q3],[0.25 * 0.5 * q2*q3.dag(),Q2_Q3d],[0.25 * 0.5 * q2.dag()*q3,Q2d_Q3],[0.25 * 0.5 * q2.dag()*q3.dag(),Q2d_Q3d],
[0.125 * 0.25 * q1*q2*q3,Q1_Q2_Q3],[0.125 * 0.25 * q1*q2*q3.dag(),Q1_Q2_Q3d],[0.125 * 0.25 * q1*q2.dag()*q3,Q1_Q2d_Q3],[0.125 * 0.25 * q1.dag()*q2*q3,Q1d_Q2_Q3],
[0.125 * 0.25 * q1*q2.dag()*q3.dag(),Q1_Q2d_Q3d],[0.125 * 0.25 * q1.dag()*q2*q3.dag(),Q1d_Q2_Q3d],[0.125 * 0.25 * q1.dag()*q2.dag()*q3,Q1d_Q2d_Q3],[0.125 * 0.25 * q1.dag()*q2.dag()*q3.dag(),Q1d_Q2d_Q3d]]
'''

#RWA
H_RWA = [[-1 * 0.5 * 0.5 * q1,Q1_RWA],[0.5 * 0.5 * q1.dag(),Q1_RWA],[-1 * 0.5 * 0.5 * q2,Q2_RWA],[0.5 * 0.5 * q2.dag(),Q2_RWA],[0.5 * q3,Q3_RWA],[0.5 * q3.dag(),Q3_RWA],
[-1 * 0.25 * 0.25 * q1*q2,Q1_Q2_RWA],[0.25 * 0.25 * q1*q2.dag(),Q1_Q2d_RWA],[0.25 * 0.25 * q1.dag()*q2,Q1_Q2d_RWA],[-1 * 0.25 * 0.25 * q1.dag()*q2.dag(),Q1_Q2_RWA],
[-1 * 0.25 * 0.5 * q1*q3,Q1_Q3_RWA],[-1 * 0.25 * 0.5 * q1*q3.dag(),Q1_Q3d_RWA],[0.25 * 0.5 * q1.dag()*q3,Q1_Q3d_RWA],[0.25 * 0.5 * q1.dag()*q3.dag(),Q1_Q3_RWA],
[-1 * 0.25 * 0.5 * q2*q3,Q2_Q3_RWA],[-1 * 0.25 * 0.5 * q2*q3.dag(),Q2_Q3d_RWA],[0.25 * 0.5 * q2.dag()*q3,Q2_Q3d_RWA],[0.25 * 0.5 * q2.dag()*q3.dag(),Q2_Q3_RWA],
[-1 * 0.125 * 0.25 * q1*q2*q3,Q1_Q2_Q3_RWA],[-1 * 0.125 * 0.25 * q1*q2*q3.dag(),Q1_Q2_Q3d_RWA],[0.125 * 0.25 * q1*q2.dag()*q3,Q1_Q2d_Q3_RWA],[0.125 * 0.25 * q1.dag()*q2*q3,Q1_Q2d_Q3d_RWA],
[0.125 * 0.25 * q1*q2.dag()*q3.dag(),Q1_Q2d_Q3d_RWA],[0.125 * 0.25 * q1.dag()*q2*q3.dag(),Q1_Q2d_Q3_RWA],[-1 * 0.125 * 0.25 * q1.dag()*q2.dag()*q3,Q1_Q2_Q3d_RWA],[-1 * 0.125 * 0.25 * q1.dag()*q2.dag()*q3.dag(),Q1_Q2_Q3_RWA]]

c_ops = [0.0005*q1,0.0005*q2,0.0005*q3,0.001*sz1,0.001*sz2]
#c_ops = [0.00005*q1]
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
	for i in range(0,2):
		if i == 0:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_14-08-19/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_14-08-19/occupation_q1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_14-08-19/occupation_q2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_14-08-19/occupation_q3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_14-08-19/sz1_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_14-08-19/sz2_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_14-08-19/sz3_000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000 Full Drive')
			result = mesolve(H2,psi0,tlist,c_ops,[sz1],options = Options(store_states = True,store_final_state = True))
		if i == 1:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_14-08-19/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_14-08-19/occupation_q1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_14-08-19/occupation_q2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_14-08-19/occupation_q3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_14-08-19/sz1_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_14-08-19/sz2_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_14-08-19/sz3_111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111 Full Drive')
			result = mesolve(H2,psi0,tlist,c_ops,options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 2:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_14-08-19/fidelity000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_14-08-19/occupation_q1_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_14-08-19/occupation_q2_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_14-08-19/occupation_q3_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_14-08-19/sz1_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_14-08-19/sz2_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_14-08-19/sz3_000-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000 RWA')
			result = mesolve(H_RWA,psi0,tlist,c_ops,options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 3:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			Tdm = ket2dm(Tdm)
			outputstr_fid 	= 'Output/Toffoli_RWA_14-08-19/fidelity111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp1 	= 'Output/Toffoli_RWA_14-08-19/occupation_q1_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp2 	= 'Output/Toffoli_RWA_14-08-19/occupation_q2_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_ocp3 	= 'Output/Toffoli_RWA_14-08-19/occupation_q3_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz1 	= 'Output/Toffoli_RWA_14-08-19/sz1_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz2 	= 'Output/Toffoli_RWA_14-08-19/sz2_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			outputstr_sz3 	= 'Output/Toffoli_RWA_14-08-19/sz3_111-RWA-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111 RWA')
			result = mesolve(H_RWA,psi0,tlist,c_ops,options = Options(nsteps = 8000,store_states = True,store_final_state = True))

		fidelity_dat 	= []
		occupation_1 	= []
		occupation_2 	= []
		occupation_3 	= []
		sigmaz_1 		= []
		sigmaz_2 		= []
		sigmaz_3 		= []

		for j in range(0,len(tlist)):
				
		 		fidelity_dat.append(fidelity(result.states[j],Tdm))
		 		occupation_1.append(expect(result.states[j],q1_before.dag() * q1_before))
		 		occupation_2.append(expect(result.states[j],q2_before.dag() * q2_before))
		 		occupation_3.append(expect(result.states[j],q3_before.dag() * q3_before))
				'''
				fidelity_dat.append(0)
		 		occupation_1.append(0)
		 		occupation_2.append(0)
		 		occupation_3.append(0)

		 		sigmaz_1.append(expect(result.states[j],sz1))
		 		sigmaz_2.append(expect(result.states[j],sz2))
		 		sigmaz_3.append(expect(result.states[j],sz3))
'''
		with open(outputstr_fid,'w') as file1:
			for j in fidelity_dat:
				file1.write(str(j) + "\n")
		with open(outputstr_ocp1,'w') as file2:
			for j in occupation_1:
				file2.write(str(j) + "\n")
		with open(outputstr_ocp2,'w') as file3:
			for j in occupation_2:
				file3.write(str(j) + "\n")
		with open(outputstr_ocp3,'w') as file4:
			for j in occupation_3:
				file4.write(str(j) + "\n")
		with open(outputstr_sz1,'w') as file5:
			for j in sigmaz_1:
				file5.write(str(j) + "\n")
		with open(outputstr_sz2,'w') as file6:
			for j in sigmaz_2:
				file6.write(str(j) + "\n")
		with open(outputstr_sz3,'w') as file7:
			for j in sigmaz_3:
				file7.write(str(j) + "\n")