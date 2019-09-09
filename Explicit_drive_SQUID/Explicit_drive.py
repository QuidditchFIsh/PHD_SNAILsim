import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *
import time
from Functions import *
from Constants import *



R = 1/sqrt(2) * (sigmay() + sigmaz())
R3 = tensor(R,R,R,R)
#R=1

one  = R*basis(2,1)
zero = R*basis(2,0)

a  = sigmap()

q1 = tensor(a, qeye(2),qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2),qeye(2))
q3 = tensor(qeye(2),qeye(2),a,qeye(2))
sm = tensor(qeye(2),qeye(2),qeye(2),a)

I = tensor(qeye(2),qeye(2),qeye(2),qeye(2))

s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())


tlist = np.linspace(0,500,num=500)
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2),qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R,qeye(2))
sx4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2),qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R,qeye(2))
sy4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2),qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R,qeye(2))
sz4 = tensor(qeye(2),qeye(2),qeye(2), R * sigmaz() * R)

H_RWA = EJ*(I + s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
#H_RWA = EJ*(I - s3x - s2z - s1z + s2z*s3x + s1z*s3x + s1z*s2z - s1z*s2z*s3x)*0.25 * 1.57 
'''
H = [(I + q3 + q3.dag() -(0+1j)*(q2.dag()-q2) -(0+1j)*(q1.dag()-q1) +(0+1j)*(q2*q3 + q2*q3.dag() - q2.dag()*q3 - q2.dag()*q3.dag()) \
- s1y*s3x + s1y*s2y + s1y*s2y*s3x)*EJ ,\

[q3,q3_2_w3],[q3.dag(),q3d_2_w3],\

[(1+0j)*q2,q2_2_w2],[-1*(1+0j)*q2.dag(),q2d_2_w2],\

[(1+0j)*q1,q1_2_w1],[-1*(1+0j)*q1.dag(),q1d_2_w1],\

[-1*(1+0j)*q2*q3,q23_2_w2_pw3],[-1*(1+0j)*q2*q3.dag(),q23d_2_w2_mw3],[(1+0j)*q2.dag()*q3,q2d3_2_w2_mw3],[(1+0j)*q2.dag()*q3.dag(),q2d3d_2_w2_pw3],\

[-1*(1+0j)*q1*q3,q13_2_w1_pw3],[-1*(1+0j)*q1*q3.dag(),q13d_2_w1_mw3],[(1+0j)*q1.dag()*q3,q1d3_2_w1_mw3],[(1+0j)*q1.dag()*q3.dag(),q1d3d_2_w1_pw3],\

[-1*q1*q2,q12_2_w1_pw2],[q1*q2.dag(),q12d_2_w1_mw2],[q1.dag()*q2,q1d2_2_w1_mw2],[-1*q1.dag()*q2.dag(),q1d2d_2_w1_pw2],\

[-1*q1*q2*q3,q123_2_w1_pw2_pw3],[-1*q1*q2*q3.dag(),q123d_2_w1_pw2_mw3],\
[q1*q2.dag()*q3,q12d3_2_w1_mw2_pw3],[q1.dag()*q2*q3,q1d23_2_mw1_pw2_pw3],\
[q1*q2.dag()*q3.dag(),q12d3d_2_mw1_pw2_pw3],[q1.dag()*q2*q3.dag(),q1d23d_2_w1_mw2_pw3],\
[-1*q1.dag()*q2.dag()*q3,q1d2d3_2_w1_pw2_mw3],[-1*q1.dag()*q2.dag()*q3.dag(),q1d2d3d_2_w1_pw2_pw3]]
'''
H = [\
#interaction part of the Hamiltonian
[-1*q3,Q3],[-1*q3.dag(),Q3d],\

[0.5*q2,Q2],[0.5*q2.dag(),Q2d],\

[0.5*q1,Q1],[0.5*q1.dag(),Q1d],\

[-1*0.5*q2*q3,Q23],[-1*0.5*q2*q3.dag(),Q23d],[-1*0.5*q2.dag()*q3,Q2d3],[-1*0.5*q2.dag()*q3.dag(),Q2d3d],\

[-1*0.5*q1*q3,Q13],[-1*0.5*q1*q3.dag(),Q13d],[-1*0.5*q1.dag()*q3,Q1d3],[-1*0.5*q1.dag()*q3.dag(),Q1d3d],\

[0.25*q1*q2,Q12],[0.25*q1*q2.dag(),Q12d],[0.25*q1.dag()*q2,Q1d2],[0.25*q1.dag()*q2.dag(),Q1d2d],\

[0.25*q1*q2*q3,Q123],[0.25*q1*q2*q3.dag(),Q123d],\
[0.25*q1*q2.dag()*q3,Q12d3],[0.25*q1.dag()*q2*q3,Q1d23],\
[0.25*q1*q2.dag()*q3.dag(),Q12d3d],[0.25*q1.dag()*q2*q3.dag(),Q1d23d],\
[0.25*q1.dag()*q2.dag()*q3,Q1d2d3],[0.25*q1.dag()*q2.dag()*q3.dag(),Q1d2d3d],\
#The squid part of the Hamiltonian
[1.5* sm * q1,SM_Q1],[-1.5* sm * q1.dag(),SM_Q1d],[1.5* sm * q2,SM_Q2],[-1.5* sm * q2.dag(),SM_Q2d],[1.2* sm * q3,SM_Q3],[-1.2* sm * q3.dag(),SM_Q3d],\
[-1.5* sm.dag() * q1.dag(),SMd_Q1d],[1.5* sm.dag() * q1,SMd_Q1],[-1.5* sm.dag() * q2.dag(),SMd_Q2d],[1.5* sm.dag() * q2,SMd_Q2],[-1.2* sm.dag() * q3.dag(),SMd_Q3d],[1.2* sm.dag() * q3,SMd_Q3],\
#Perturbations to the Hamiltonian
[0.125*q1.dag()*q1,no_rotation],[0.125*q1*q1.dag(),no_rotation],[0.125*q2.dag()*q2,no_rotation],[0.125*q2*q2.dag(),no_rotation],[0.5*q3.dag()*q3,no_rotation],[0.5*q3*q3.dag(),no_rotation],\
[0.02*q1*q1.dag()*q1,Q1],[0.02*q2*q2.dag()*q2,Q2],[-1*0.17*q3*q3.dag()*q3,Q3],\
[0.02*q1.dag()*q1*q1.dag(),Q1d],[0.02*q2.dag()*q2*q2.dag(),Q2d],[-1*0.17*q3.dag()*q3*q3.dag(),Q3d],\
[0.0625*q1.dag()*q1*q2,Q2],[0.0625*q1.dag()*q1*q2.dag(),Q2d],[0.0625*q1*q1.dag()*q2.dag(),Q2d],[0.0625*q1*q1.dag()*q2,Q2],\
[-0.125*q1.dag()*q1*q3,Q3],[-0.125*q1.dag()*q1*q3.dag(),Q3],[-0.125*q1*q1.dag()*q3.dag(),Q3d],[-0.125*q1*q1.dag()*q3,Q3],\
[-0.125*q2.dag()*q2*q3,Q3],[-0.125*q2.dag()*q2*q3.dag(),Q3d],[-0.125*q2*q2.dag()*q3.dag(),Q3d],[-0.125*q2*q2.dag()*q3,Q3],\
[0.0625*q1*q2*q2.dag(),Q1],[0.0625*q1.dag()*q2*q2.dag(),Q1d],[0.0625*q1.dag()*q2.dag()*q2,Q1],[0.0625*q1*q2.dag()*q2,Q1d],\
[0.25*q1*q3*q3.dag(),Q1],[0.25*q1.dag()*q3*q3.dag(),Q1d],[0.25*q1.dag()*q3.dag()*q3,Q1],[0.25*q1*q3.dag()*q3,Q1d],\
[0.25*q2*q3*q3.dag(),Q2],[0.25*q2.dag()*q3*q3.dag(),Q2d],[0.25*q2.dag()*q3.dag()*q3,Q2],[0.25*q2*q3.dag()*q3,Q2d],\
]




c_ops = [0.00001*q1,0.00001*q2,0.00001*q3,sz1*0.00001,sz2*0.00001,sz3*0.00001]
outputstr = ''

omega1   	= 4 * 2 * pi
omega2   	= 10 * 2 * pi
omega3   	= 17 * 2 * pi
for i in range(0,2):
	if i == 0:
		psi0 = tensor(zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_RWA_14-08-19/fidelity000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'			
		outputstr_ocp1 		= 'Output/Toffoli_RWA_14-08-19/occupation_q1_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_RWA_14-08-19/occupation_q2_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_RWA_14-08-19/occupation_q3_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsm 	= 'Output/Toffoli_RWA_14-08-19/occupation_sm_000-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('000 Full Drive')
		result = mesolve(H,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*sm.dag()*sm*R3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
	if i == 1:
		psi0 = tensor(one,one,one,zero);Tdm = tensor(one,one,zero,zero)
		Tdm = ket2dm(Tdm)
		outputstr_fid 		= 'Output/Toffoli_RWA_14-08-19/fidelity111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp1 		= 'Output/Toffoli_RWA_14-08-19/occupation_q1_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp2 		= 'Output/Toffoli_RWA_14-08-19/occupation_q2_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocp3 		= 'Output/Toffoli_RWA_14-08-19/occupation_q3_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		outputstr_ocpsm 	= 'Output/Toffoli_RWA_14-08-19/occupation_sm_111-' + str(omega1) + '_' + str(omega2) +'_' + str(omega3) + '.dat'
		print('111 Full Drive')
		result = mesolve(H,psi0,tlist,c_ops,[R3*q1.dag()*q1*R3,R3*q2.dag()*q2*R3,R3*q3.dag()*q3*R3,R3*sm.dag()*sm*R3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
	fidelity_dat 	= []
	occupation_1 	= []
	occupation_2 	= []
	occupation_3 	= []
	occupation_sm	= []

	for j in range(0,len(tlist)):
	 	fidelity_dat.append(fidelity(result.states[j],Tdm))
		occupation_1.append(result.expect[0][j])
		occupation_2.append(result.expect[1][j])
		occupation_3.append(result.expect[2][j])
		occupation_sm.append(result.expect[3][j])
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
		with open(outputstr_ocpsm,'w') as file5:
			for j in occupation_sm:
				file5.write(str(j) + "\n")