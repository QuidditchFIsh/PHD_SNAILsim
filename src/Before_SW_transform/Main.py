'''
Author:Aneirin John Baker	
Date: 11/07/19
Description: Main script within this simulation. It will handle all of the solvers and will hold
all of the Hamiltonian variables and the Hamiltonian itself.It will then pass all of the results onto
another script for that to print all of it out.
'''

from Constants import *
from Functions import *
from qutip import *
from math import *

#Define all of the variables to use 

R  		= 1/sqrt(2) * (sigmay() + sigmaz())
R3 		= tensor(R,R,R,R,R)


one  	= R*basis(2,1)
zero 	= R*basis(2,0)

a 		= sigmap()

q1 		= tensor(a,qeye(2),qeye(2),qeye(2),qeye(2))
q2		= tensor(qeye(2),a,qeye(2),qeye(2),qeye(2))
q3 		= tensor(qeye(2),qeye(2),a,qeye(2),qeye(2))
sm 		= tensor(qeye(2),qeye(2),qeye(2),a,qeye(2))
sp 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2),a)

I 		= tensor(qeye(2),qeye(2),qeye(2),qeye(2),qeye(2))


#Define variables for the Hamiltonian

pi1 = (1/q1_Bar) * (q1 - q1.dag())
pi2 = (1/q2_Bar) * (q2 - q2.dag())
pi3 = (1/q3_Bar) * (q3 - q3.dag())
pip = (1/sp_Bar) * (sp - sp.dag())
pim = (1/sm_Bar) * (sm - sm.dag())


v1 = q1_Bar * (q1 + q1.dag())
v2 = q2_Bar * (q2 + q2.dag())
v3 = q3_Bar * (q3 + q3.dag())
vp = sp_Bar * (sp + sp.dag())
vm = sm_Bar * (sm + sm.dag())


#Building the Hmiltonian using several different parts (In two level approximation. With antthing else would need to add in more terms)
#First terms in the SQUID potential
H = [[vm.cosm(),no_rotation_cos],[-1*vm.cosm(),no_rotation_sin],\
[sm_Bar * sm,Qsm_cos],[sm_Bar * sm.dag(),Qsmd_cos],\

[sm_Bar**3 * sm.dag()*sm*sm,Qsm_cos],[sm_Bar**3 * sm.dag()*sm*sm.dag(),Qsmd_cos] ,\
[sm_Bar**3 * sm*sm.dag()*sm.dag(),Qsmd_cos],[sm_Bar**3 * sm*sm.dag()*sm,Qsm_cos],\

[sm_Bar**3 * sm.dag()*sm*sm,Qsm_sin],[sm_Bar**3 * sm.dag()*sm*sm.dag(),Qsmd_sin] ,\
[sm_Bar**3 * sm*sm.dag()*sm.dag(),Qsmd_sin],[sm_Bar**3 * sm*sm.dag()*sm,Qsm_sin],\
#Now terms in the interaction terms
[q1*sp,Q1_sp],[q1*sp.dag(),Q1_spd],[q1*sm,Q1_sm],[q1*sm.dag(),Q1_smd],\
[q1.dag()*sp.dag(),Q1d_spd],[q1.dag()*sp,Q1d_sp],[q1.dag()*sm.dag(),Q1d_smd],[q1.dag()*sm,Q1d_sm],\

[q2*sp,Q2_sp],[q2*sp.dag(),Q2_spd],[q2*sm,Q2_sm],[q2*sm.dag(),Q2_smd],\
[q2.dag()*sp.dag(),Q2d_spd],[q2.dag()*sp,Q2d_sp],[q2.dag()*sm.dag(),Q2d_smd],[q2.dag()*sm,Q2d_sm],\

[2*q3*sp,Q3_sp],[2*q3*sp.dag(),Q3_spd],[-2*q3*sm,Q3_sm],[-2*q3*sm.dag(),Q3_smd],\
[2*q3.dag()*sp.dag(),Q3d_spd],[2*q3.dag()*sp,Q3d_sp],[-2*q3.dag()*sm.dag(),Q3d_smd],[-2*q3.dag()*sm,Q3d_sm],\
]





