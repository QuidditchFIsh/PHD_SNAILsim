import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from math import *

times = np.linspace(0.0,20.0,400)

psi0 = tensor(fock(2,0) , fock(10,5))

a = tensor(qeye(2) , destroy(10))

sm = tensor(destroy(2) , qeye(10))

H = 2 * np.pi * a.dag() * a + 2 * np.pi * sm.dag() * sm + 2 * np.pi * 0.25 * (sm * a.dag() + sm.dag() * a)

result = mesolve(H,psi0,times, [np.sqrt(0.1)*a], [a.dag()*a, sm.dag()*sm])

plt.plot(times , result.expect[0])
plt.plot(times , result.expect[1])

plt.xlabel('Time')
plt.ylabel('Expectation Value')

plt.legend(("Cavity Photon Number", "Atom Exctition Probability"))
plt.show()