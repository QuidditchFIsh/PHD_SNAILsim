'''
Author: Aneirin John Baker
Date : 08/01/2019
Description:Simulation of the un transformed hamiltonian to see if there is any difference in transforming the hamitonian. Will take out the mediator parameters as they 
should not play a roll in the final system as they will be sufficently detuned from the quBits
'''


import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *

N=2
q1 = tensor(destroy(N),qeye(N))
q1d = q1.dag()
phi1 = (q1 + q1d)

q2 = tensor(qeye(N),destroy(N))
q2d = q2.dag()
phi2 = (q2 + q2d)

H0 =  q1d * q1

x = phi1 * phi1