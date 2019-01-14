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

print(qeye(2))
print(identity(2))