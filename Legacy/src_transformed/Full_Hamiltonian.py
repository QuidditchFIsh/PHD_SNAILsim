import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants_Full  import *
from math import *
import time
import datetime
import Constants as cons
import os

def H_drive(t,*args):
	return 0.5*(0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))


print("============================================")
print("Begining Program, setting up calculations")

N = 2
q1 = tensor(destroy(N),qeye(N),qeye(N),qeye(N),qeye(N))
q2 = tensor(qeye(N),destroy(N),qeye(N),qeye(N),qeye(N))
q3 = tensor(qeye(N),qeye(N),destroy(N),qeye(N),qeye(N))
sP = tensor(qeye(N),qeye(N),qeye(N),destroy(N),qeye(N))
sM = tensor(qeye(N),qeye(N),qeye(N),qeye(N),destroy(N))

q1d = q1.dag()
q2d = q2.dag()
q3d = q3.dag()
sPd = sP.dag()
sMd = sM.dag()

phi1 = phibar1 * (q1 + q1d)
phi2 = phibar2 * (q2 + q2d)
phi3 = phibar3 * (q3 + q3d)
varphiP = (phi1 + phi2 + 2*phi3)
varphiM = (phi1 + phi2 - 2*phi3)

pi1 = (1/(2 * phibar1)) * (q1 - q1d)
pi2 = (1/(2 * phibar2)) * (q2 - q2d)
pi3 = (1/(2 * phibar3)) * (q3 - q3d)

phiP = phibarP * (sP + sPd)
phiM = phibarM * (sM + sMd)

phiMhalf = 0.5 * phiM
phiMthird = 0.3333333333333333 * phiM

piP = (1/(2 * phibarP)) * (sP - sPd)
piM = (1/(2 * phibarM)) * (sM - sMd)

#Setting up the Hamiltonian .....THis is gonna be long

H0 = 0
H1 = 0
#Will have to check about the cos of the matrix
H0 += (4 * ECQ1 * (1/1**2)) * pi1*pi1 + (4 * ECQ2 * (1/1**2)) * pi2*pi2 + (4 * ECQ3 * (1/1**2)) * pi3*pi3 + EJ1 * phi1.cosm() + EJ2 * phi2.cosm() + EJ3 * phi3.cosm() + (phi0**2 * (1/(2*L)) * ((phi1 * phi1) + (phi2 * phi2) + 0.5 * (phi3 * phi3)))

H0 += EL * (phiP*phiP + phiM*phiM) + EL * (phiP*varphiP + phiM*varphiM) 
H0 += phiP*phiP * (0.5 * (1/CG) * (1/phi0**2)) + phiM * phiM * (0.5 * (1/CG) * (1/phi0**2))

H1 += EJ * phiMhalf.sinm() + EJ * phiMhalf.cosm()


#Prepareing the rest of the calculations
tlist = np.linspace(0, 50, 50)
#Basis states
psi_list = []
psi_list.append(basis(2,0))
for n in range(4):
    psi_list.append(basis(2,0))
psi0 = tensor(psi_list)


#operators to be evaulated
sz1 = tensor(sigmaz(),qeye(N),qeye(N),qeye(N),qeye(N))
sz2 = tensor(qeye(N),sigmaz(),qeye(N),qeye(N),qeye(N))
sz3 = tensor(qeye(N),qeye(N),sigmaz(),qeye(N),qeye(N))

#collapse operator list
c_op_list = [0.01*q1,0.01*q2,0.01*q3,0.01*sz1,0.01*sz2,0.01*sz3]

avg_sz1 = []
avg_sz2 = []
avg_sz3 = []
avg_sz4 = []

eval_op_list = [sz1,sz2,sz3]


H = [H0,[H1,H_drive]]
