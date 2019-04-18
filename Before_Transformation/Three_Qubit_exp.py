import numpy as np
from qutip import *
from math import *
import time
import datetime
from Functions import *
from Constants import *

#H0  = (omegaM * sM.dag() * sM +  omegaP * sP.dag() * sP )
H0 = tensor(a,a,a,a,a) * 0

mult = ((0.5*(sM + sM.dag())).cosm() + (0.5*(sM + sM.dag())).sinm())
mult2 = ((0.5*(sM + sM.dag())).cosm() + (0.5*(sM + sM.dag())).sinm())

#Define the multipliers for the system
EJ = 0.1

mult1_2 	= EJ * 0.5	 
mult3  		= EJ * 1.0

mult12 		= EJ * 0.25
mult13_23	= EJ * 0.5

mult123	 	= EJ * 0.25

H = [H0,
#The Hamiltonian is split into three parts due to the expansion of the sin and cos terms in H_int.
#s * sin(0.5) term
[mult1_2 * sM * sin(0.5) * q1,H1_rot1_sMp],[mult1_2 * sM * sin(0.5) * q1.dag(),H1_rot1d_sMp],[mult1_2 * sM * sin(0.5) * q2,H1_rot2_sMp],[mult1_2 * sM * sin(0.5) * q2.dag(),H1_rot2d_sMp],[mult3 * sM * sin(0.5) * q3,H1_rot3_sMp],[mult3 * sM * sin(0.5) * q3.dag(),H1_rot3d_sMp],
[mult12 * sM * sin(0.5) * q1*q2,H1_rot12_pp_sMp],[mult12 * sM * sin(0.5) * q1*q2.dag(),H1_rot12_pm_sMp],[mult12 * sM * sin(0.5) * q1.dag()*q2,H1_rot12_mp_sMp],[mult12 * sM * sin(0.5) * q1.dag()*q2.dag(),H1_rot12_mm_sMp],
[mult13_23 * sM * sin(0.5) * q1*q3,H1_rot13_pp_sMp],[mult13_23 * sM * sin(0.5) * q1*q3.dag(),H1_rot13_pm_sMp],[mult13_23 * sM * sin(0.5) * q1.dag()*q3,H1_rot13_mp_sMp],[mult13_23 * sM * sin(0.5) * q1.dag()*q3.dag(),H1_rot13_mm_sMp],
[mult13_23 * sM * sin(0.5) * q2*q3,H1_rot23_pp_sMp],[mult13_23 * sM * sin(0.5) * q2*q3.dag(),H1_rot23_pm_sMp],[mult13_23 * sM * sin(0.5) * q2.dag()*q3,H1_rot23_mp_sMp],[mult13_23 * sM * sin(0.5) * q2.dag()*q3.dag(),H1_rot23_mm_sMp],
[mult123 * sM * sin(0.5) * q1*q2*q3,H1_rot_123_ppp_sMp],[mult123 * sM * sin(0.5) * q1*q2*q3.dag(),H1_rot_123_ppm_sMp],[mult123 * sM * sin(0.5) * q1*q2.dag()*q3,H1_rot_123_pmp_sMp],[mult123 * sM * sin(0.5) * q1*q2.dag()*q3.dag(),H1_rot_123_pmm_sMp],
[mult123 * sM * sin(0.5) * q1.dag()*q2*q3,H1_rot_123_mpp_sMp],[mult123 * sM * sin(0.5) * q1.dag()*q2*q3.dag(),H1_rot_123_mpm_sMp],[mult123 * sM * sin(0.5) * q1.dag()*q2.dag()*q3,H1_rot_123_mmp_sMp],[mult123 * sM * sin(0.5) * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm_sMp],
#s.dag() * sin(0.5) term
[mult1_2 * sM.dag() * sin(0.5) * q1,H1_rot1_sMm],[mult1_2 * sM.dag() * sin(0.5) * q1.dag(),H1_rot1d_sMm],[mult1_2 * sM.dag() * sin(0.5) * q2,H1_rot2_sMm],[mult1_2 * sM.dag() * sin(0.5) * q2.dag(),H1_rot2d_sMm],[mult3 * sM.dag() * sin(0.5) * q3,H1_rot3_sMm],[mult3 * sM.dag() * sin(0.5) * q3.dag(),H1_rot3d_sMm],
[mult12 * sM.dag() * sin(0.5) * q1*q2,H1_rot12_pp_sMm],[mult12 * sM.dag() * sin(0.5) * q1*q2.dag(),H1_rot12_pm_sMm],[mult12 * sM.dag() * sin(0.5) * q1.dag()*q2,H1_rot12_mp_sMm],[mult12 * sM.dag() * sin(0.5) * q1.dag()*q2.dag(),H1_rot12_mm_sMm],
[mult13_23 * sM.dag() * sin(0.5) * q1*q3,H1_rot13_pp_sMm],[mult13_23 * sM.dag() * sin(0.5) * q1*q3.dag(),H1_rot13_pm_sMm],[mult13_23 * mult13_23 * sM.dag() * sin(0.5) * q1.dag()*q3,H1_rot13_mp_sMm],[mult13_23 * sM.dag() * sin(0.5) * q1.dag()*q3.dag(),H1_rot13_mm_sMm],
[mult13_23 * sM.dag() * sin(0.5) * q2*q3,H1_rot23_pp_sMm],[mult13_23 * sM.dag() * sin(0.5) * q2*q3.dag(),H1_rot23_pm_sMm],[mult13_23 * mult13_23 * sM.dag() * sin(0.5) * q2.dag()*q3,H1_rot23_mp_sMm],[mult13_23 * sM.dag() * sin(0.5) * q2.dag()*q3.dag(),H1_rot23_mm_sMm],
[mult123 * sM.dag() * sin(0.5) * q1*q2*q3,H1_rot_123_ppp_sMm],[mult123 * sM.dag() * sin(0.5) * q1*q2*q3.dag(),H1_rot_123_ppm_sMm],[mult123 * sM.dag() * sin(0.5) * q1*q2.dag()*q3,H1_rot_123_pmp_sMm],[mult123 * sM.dag() * sin(0.5) * q1*q2.dag()*q3.dag(),H1_rot_123_pmm_sMm],
[mult123 * sM.dag() * sin(0.5) * q1.dag()*q2*q3,H1_rot_123_mpp_sMm],[mult123 * sM.dag() * sin(0.5) * q1.dag()*q2*q3.dag(),H1_rot_123_mpm_sMm],[mult123 * sM.dag() * sin(0.5) * q1.dag()*q2.dag()*q3,H1_rot_123_mmp_sMm],[mult123 * sM.dag() * sin(0.5) * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm_sMm],
#cos(0.5) term
[mult1_2 * cos(0.5) * q1,H1_rot1],[mult1_2 * cos(0.5) * q1.dag(),H1_rot1d],[mult1_2 * cos(0.5) * q2,H1_rot2],[mult1_2 * cos(0.5) * q2.dag(),H1_rot2d],[mult3 * cos(0.5) * q3,H1_rot3],[mult3 * cos(0.5) * q3.dag(),H1_rot3d],
[mult12 * cos(0.5) * q1*q2,H1_rot12_pp],[mult12 * cos(0.5) * q1*q2.dag(),H1_rot12_pm],[mult12 * cos(0.5) * q1.dag()*q2,H1_rot12_mp],[mult12 * cos(0.5) * q1.dag()*q2.dag(),H1_rot12_mm],
[mult13_23 * cos(0.5) * q1*q3,H1_rot13_pp],[mult13_23 * cos(0.5) * q1*q3.dag(),H1_rot13_pm],[mult13_23 * cos(0.5) * q1.dag()*q3,H1_rot13_mp],[mult13_23 * cos(0.5) * q1.dag()*q3.dag(),H1_rot13_mm],
[mult13_23 * cos(0.5) * q2*q3,H1_rot23_pp],[mult13_23 * cos(0.5) * q2*q3.dag(),H1_rot23_pm],[mult13_23 * cos(0.5) * q2.dag()*q3,H1_rot23_mp],[mult13_23 * cos(0.5) * q2.dag()*q3.dag(),H1_rot23_mm],
[mult123 * cos(0.5) * q1*q2*q3,H1_rot_123_ppp],[mult123 * cos(0.5) * q1*q2*q3.dag(),H1_rot_123_ppm],[mult123 * cos(0.5) * q1*q2.dag()*q3,H1_rot_123_pmp],[mult123 * cos(0.5) * q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult123 * cos(0.5) * q1.dag()*q2*q3,H1_rot_123_mpp],[mult123 * cos(0.5) * q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult123 * cos(0.5) * q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult123 * cos(0.5) * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm],
]

tlist = np.linspace(0,2**7,2**7)

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.001*sM,0.001*sP,0.002*sz1,0.002*sz2,0.002*sz3]

outputstr = ''


for i in range(0,3):
	if i == 0:
		psi0 = tensor(zero,zero,zero,zero,zero);Tdm = tensor(zero,zero,zero,zero,zero)
		outputstr = 'Output/Toffoli_18-04-19/one/'
		print('1')
	if i == 1:	
		psi0 = tensor(one,one,zero,zero,zero);Tdm = tensor(one,one,one,zero,zero)
		outputstr = 'Output/Toffoli_18-04-19/two/'
		print('1')
	if i == 2:
		psi0 = tensor(one,one,one,zero,zero);Tdm = tensor(one,one,zero,zero,zero)
		outputstr = 'Output/Toffoli_18-04-19/three/'
		print('1')
	'''
	if i == 3:
		psi0 = tensor(zero,one,one);Tdm = tensor(zero,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity011.dat'
	if i == 4:
		psi0 = tensor(one,zero,zero);Tdm = tensor(one,zero,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity100.dat'
	if i == 5:
		psi0 = tensor(one,zero,one);Tdm = tensor(one,zero,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity101.dat'
	if i == 6:
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity110.dat'
	if i == 7:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity111.dat'
	'''

	result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2,sx3,sy3,sz3,sy4],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
	
	fidelity_dat = []

	Qubit_state_1_0 = []
	Qubit_state_1_1 = []

	Qubit_state_2_0 = []
	Qubit_state_2_1 = []

	Qubit_state_3_0 = []
	Qubit_state_3_1 = []

	Qubit_state_4_0 = []
	Qubit_state_4_1 = []

	Qubit_state_5_0 = []
	Qubit_state_5_1 = []


	Expect_sz1 = []
	Expect_sz2 = []
	Expect_sz3 = []
	Expect_sz4 = []

	for j in range(0,len(tlist)):
		fidelity_dat.append(fidelity(result.states[j],Tdm))
		Qubit_state_1_0.append(expect(result.states[j].ptrace(0),zero))
		Qubit_state_1_1.append(expect(result.states[j].ptrace(0),one))		

		Qubit_state_2_0.append(expect(result.states[j].ptrace(1),zero))
		Qubit_state_2_1.append(expect(result.states[j].ptrace(1),one))

		Qubit_state_3_0.append(expect(result.states[j].ptrace(2),zero))
		Qubit_state_3_1.append(expect(result.states[j].ptrace(2),one))

		Qubit_state_4_0.append(expect(result.states[j].ptrace(3),zero))
		Qubit_state_4_1.append(expect(result.states[j].ptrace(3),one))

		Qubit_state_5_0.append(expect(result.states[j].ptrace(4),zero))
		Qubit_state_5_1.append(expect(result.states[j].ptrace(4),one))

		Expect_sz1.append(result.expect[2][j])
		Expect_sz2.append(result.expect[5][j])
		Expect_sz3.append(result.expect[8][j])
		Expect_sz4.append(result.expect[9][j])



        with open(outputstr + 'Qubit_state_1_0.dat','w') as f1:
                for j in Qubit_state_1_0:
                        f1.write(str(j) + "\n")
        with open(outputstr + 'Qubit_state_1_1.dat','w') as f1:
                for j in Qubit_state_1_1:
                        f1.write(str(j) + "\n")

        with open(outputstr + 'Qubit_state_2_0.dat','w') as f1:
                for j in Qubit_state_2_0:
                        f1.write(str(j) + "\n")
        with open(outputstr + 'Qubit_state_2_1.dat','w') as f1:
                for j in Qubit_state_2_1:
                        f1.write(str(j) + "\n")

        with open(outputstr + 'Qubit_state_3_0.dat','w') as f1:
                for j in Qubit_state_3_0:
                        f1.write(str(j) + "\n")
        with open(outputstr + 'Qubit_state_3_1.dat','w') as f1:
                for j in Qubit_state_3_1:
                        f1.write(str(j) + "\n")

        with open(outputstr + 'Qubit_state_4_0.dat','w') as f1:
                for j in Qubit_state_4_0:
                        f1.write(str(j) + "\n")
        with open(outputstr + 'Qubit_state_4_1.dat','w') as f1:
                for j in Qubit_state_4_1:
                        f1.write(str(j) + "\n")

        with open(outputstr + 'Qubit_state_5_0.dat','w') as f1:
                for j in Qubit_state_5_0:
                        f1.write(str(j) + "\n")
        with open(outputstr + 'Qubit_state_5_1.dat','w') as f1:
                for j in Qubit_state_5_1:
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
        with open(outputstr + 'Expect_sz4.dat','w') as f1:
                for j in Expect_sz4:
                        f1.write(str(j) + "\n")