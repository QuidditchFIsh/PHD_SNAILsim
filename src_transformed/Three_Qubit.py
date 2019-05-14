import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime



#((cos(omega3 * t) + 2*sin(omega2*t) + 2*sin(omega1 * t) - 2*cos((omega1 + omega2)*t) + 2*cos((omega1 - omega2)*t) + sin((omega1 + omega3)*t) + sin((omega1-omega3)*t) + sin((omega2 + omega3)*t) + sin((omega2 - omega3)*t) - cos((omega1 + omega2 + omega3)*t) - cos((omega1 + omega2 - omega3)*t) + cos((omega1 - omega2 + omega3)*t) + cos((omega1 - omega2 - omega3)*t)))
#((-1*cos(omega3 * t) + 2*cos(omega2*t + 0.5*PI) + 2*cos(omega1 * t + 0.5*PI) + 4*cos((omega1 + omega2)*t) - 4*cos((omega1 - omega2)*t) + 2*cos((omega1 + omega3)*t + 0.5*PI) + 2*cos((omega1-omega2)*t) + 2*cos((omega2 + omega3)*t) + 2*cos((omega2 - omega3)*t) - 4*cos((omega1 + omega2 + omega3)*t) - 4*cos((omega1 + omega2 - omega3)*t) - 4*cos((omega1 - omega2 + omega3)*t) - 4*cos((omega1 - omega2 - omega3)*t)))
# ((cos(omega3 * t) + 2*sin(omega2*t) + 2*sin(omega1 * t) - 2*cos((omega1 + omega2)*t) + 2*cos((omega1 - omega2)*t) + sin((omega1 + omega3)*t) + sin((omega1-omega3)*t) + sin((omega2 + omega3)*t) + sin((omega2 - omega3)*t) - cos((omega1 + omega2 + omega3)*t) - cos((omega1 + omega2 - omega3)*t) + cos((omega1 - omega2 + omega3)*t) + cos((omega1 - omega2 - omega3)*t)))
#(1 + sin(omega1*t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))

def H1_rot1(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) - (0+1j)*sin(omega2*t))
def H1_rot3(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega3 * t) + (0+1j)*sin(omega3*t))
def H1_rot3d(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega3 * t) - (0+1j)*sin(omega3*t))

def H1_rot12_pp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return (1 + sin(omega1 * t)) * (1 + sin(omega2 * t)) * (1 + cos(omega3 * t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


R = 1/sqrt(2) * (sigmay() + sigmaz())
#R=1

one  = basis(2,1)
zero = basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

H0  = 0 * tensor(a,a,a)

I = tensor(qeye(2),qeye(2),qeye(2))

#Define the multipliers for the system
EJ = 0.1

mult1_2 	= EJ * 0.5 	 
mult3  		= EJ * 1.0

mult12 		= EJ * 0.5
mult13_23	= EJ * 0.25 

mult123	 	= EJ * 0.25 

H = [H0,
[mult1_2 *  q1,H1_rot1],[mult1_2 *  q1.dag(),H1_rot1d],[mult1_2 *  q2,H1_rot2],[mult1_2 *  q2.dag(),H1_rot2d],[mult3 *  q3,H1_rot3],[mult3 *  q3.dag(),H1_rot3d],
[mult12 *  q1*q2,H1_rot12_pp],[mult12 *  q1*q2.dag(),H1_rot12_pm],[mult12 *  q1.dag()*q2,H1_rot12_mp],[mult12 *  q1.dag()*q2.dag(),H1_rot12_mm],
[mult13_23 *  q1*q3,H1_rot13_pp],[mult13_23 *  q1*q3.dag(),H1_rot13_pm],[mult13_23 * mult13_23 *  q1.dag()*q3,H1_rot13_mp],[mult13_23 *  q1.dag()*q3.dag(),H1_rot13_mm],
[mult13_23 *  q2*q3,H1_rot23_pp],[mult13_23 *  q2*q3.dag(),H1_rot23_pm],[mult13_23 * mult13_23 *  q2.dag()*q3,H1_rot23_mp],[mult13_23 *  q2.dag()*q3.dag(),H1_rot23_mm],
[mult123 *  q1*q2*q3,H1_rot_123_ppp],[mult123 *  q1*q2*q3.dag(),H1_rot_123_ppm],[mult123 *  q1*q2.dag()*q3,H1_rot_123_pmp],[mult123 *  q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult123 *  q1.dag()*q2*q3,H1_rot_123_mpp],[mult123 *  q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult123 *  q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult123 *  q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm]]


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,2000,2000)
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

#print(s1z)
#print(sy1)

H2 = 0.0015*(I + s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
#print(H2)


c_ops = [0.05*q1,0.05*q2,0.05*q3,0.05*sz1,0.05*sz2,0.05*sz3]

outputstr = ''

#freqs = np.genfromtxt('Frequencies3.dat')
freqs = [[4,10,17]]
for j in freqs:
	print(j)
	omega1   = j[0]
	omega2   = j[1]
	omega3   = j[2]
	f1 = j[0]
	f2 = j[1]
	f3 = j[2]
	for k in range(0,2):
		decay = 0.05 * (k + 1)
		c_ops = [decay*q1,decay*q2,decay*q3,decay*sz1,decay*sz2,decay*sz3]

		for i in range(0,2):
			if i == 0:
				psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
				outputstr_fidelity = 'Output/Toffoli_14-05-19/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_1 = 'Output/Toffoli_14-05-19/occupation000_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_2 = 'Output/Toffoli_14-05-19/occupation000_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_3 = 'Output/Toffoli_14-05-19/occupation000_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				print('000 ' + str(decay))
				print(str(omega1) + " " + str(omega2) + " " + str(omega3))
				result = mesolve(H,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
				fidelity000 = []
				for j in range(0,len(tlist)):
			 		fidelity000.append(fidelity(result.states[j],Tdm))
			if i == 1:
				psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
				outputstr_fidelity = 'Output/Toffoli_14-05-19/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_1 = 'Output/Toffoli_14-05-19/occupation111_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_2 = 'Output/Toffoli_14-05-19/occupation111_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_3 = 'Output/Toffoli_14-05-19/occupation111_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				print('111 ' + str(decay))
				print(str(omega1) + " " + str(omega2) + " " + str(omega3))
				result = mesolve(H,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
				fidelity111 = []
				for j in range(0,len(tlist)):
			 		fidelity111.append(fidelity(result.states[j],Tdm))
			if i == 2:
				psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
				outputstr_fidelity = 'Output/Toffoli_14-05-19/Fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_1 = 'Output/Toffoli_14-05-19/Occupation000_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_2 = 'Output/Toffoli_14-05-19/Occupation000_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_3 = 'Output/Toffoli_14-05-19/Occupation000_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				print('000')
				print(str(omega1) + " " + str(omega2) + " " + str(omega3))
				result = mesolve(H2,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
			if i == 3:
				psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
				outputstr_fidelity = 'Output/Toffoli_14-05-19/Fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_1 = 'Output/Toffoli_14-05-19/Occupation111_q1-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_2 = 'Output/Toffoli_14-05-19/Occupation111_q2-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				outputstr_occupation_3 = 'Output/Toffoli_14-05-19/Occupation111_q3-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
				print('111')
				print(str(omega1) + " " + str(omega2) + " " + str(omega3))
				result = mesolve(H2,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


			min_fidelity_dat = []
			occupation1 = []
			occupation2 = []
			occupation3 = []

			
			for j in range(0,len(tlist)):
				#min_fidelity_dat.append(min(fidelity000[j],fidelity111[j]))
			 	#fidelity_dat.append(fidelity(result.states[j],Tdm))
			 	occupation1.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(0)).real)
			 	occupation2.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(1)).real)
			 	occupation3.append(expect(sigmap().dag() * sigmap(),result.states[j].ptrace(2)).real)
			
			with open(outputstr_occupation_1 , 'w') as f:
				for j in occupation1:
					f.write(str(j) + "\n")
			with open(outputstr_occupation_2 , 'w') as f:
				for j in occupation2:
					f.write(str(j) + "\n")
			with open(outputstr_occupation_3 , 'w') as f:
				for j in occupation3:
					f.write(str(j) + "\n")
		for j in range(0,len(tlist)):
				min_fidelity_dat.append(min(fidelity000[j],fidelity111[j]))
		with open('Output/Toffoli_14-05-19/Min_Fidelity.dat','a+') as f:
			for j in range(0,len(tlist)):
				f.write(str(j) + " " + str(decay)+ " " + str(min_fidelity_dat[j]) + "\n")
