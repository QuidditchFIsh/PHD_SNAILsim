import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime

def H1_rot1(t,*args):
	return (cos(omega1 * t + 0.5*PI) )*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (cos(omega1 * t + 0.5*PI) )*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (cos(omega2*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (cos(omega2*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot3(t,*args):
	return ((-1*cos(omega3 * t))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ))
def H1_rot3d(t,*args):
	return ((-1*cos(omega3 * t))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ))

def H1_rot12_pp(t,*args):
	return ( cos((omega1 + omega2)*t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return (- cos((omega1 - omega2)*t))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return ( - cos((omega1 - omega2)*t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (cos((omega1 + omega2)*t))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return ( cos((omega1 + omega3)*t + 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return ( cos((omega1 - omega3)*t + 0.5*PI))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return ( cos((omega1 - omega3)*t + 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return ( cos((omega1 + omega3)*t + 0.5*PI))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return ( cos((omega2 + omega3)*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return ( cos((omega2 - omega3)*t + 0.5*PI))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return ( cos((omega2 - omega3)*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return ( cos((omega2 + omega3)*t + 0.5*PI))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return (- cos((omega1 + omega2 + omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return (- cos((omega1 + omega2 - omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return (- cos((omega1 - omega2 + omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return (- cos((omega1 - omega2 - omega3)*t)) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return (- cos((-omega1 + omega2 + omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return (- cos((-omega1 + omega2 - omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return (- cos((-omega1 - omega2 + omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return (- cos((-omega1 - omega2 - omega3)*t)) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

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


s1y = (0 + 1j)*(q1.dag() - q1)
s2y = (0 + 1j)*(q2.dag() - q2)
s3y = (0 + 1j)*(q3.dag() - q3)

s1z = q1*q1.dag() - q1.dag()*q1
s2z = q2*q2.dag() - q2.dag()*q2
s3z = q3*q3.dag() - q3.dag()*q3

s1x = (q1 + q1.dag())
s2x = (q2 + q2.dag())
s3x = (q3 + q3.dag())



tlist = np.linspace(0,10,1000)
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

#print(s1y)
#print(sz1)

H2 = 0.25*(I + s3x - s2y - s1y - s2y*s3x - s1y*s3x + s1y*s2y + s1y*s2y*s3x)
#print(H2)


c_ops = [0.1*q1,0.1*q2,0.1*q3,0.2*sz1,0.2*sz2,0.2*sz3]

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
	for i in range(0,2):
		if i == 0:
			psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
			outputstr = 'Output/test/fidelity000-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('000')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H2,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))
		if i == 1:
			psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
			outputstr = 'Output/test/fidelity111-' + str(f1) + '_' + str(f2) +'_' + str(f3) + '.dat'
			print('111')
			print(str(omega1) + " " + str(omega2) + " " + str(omega3))
			result = mesolve(H2,psi0,tlist,c_ops,[],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


		fidelity_dat = []
		for j in range(0,len(tlist)):
		 		fidelity_dat.append(fidelity(result.states[j],Tdm))

		with open(outputstr,'w') as f:
			for j in fidelity_dat:
				f.write(str(j) + "\n")
