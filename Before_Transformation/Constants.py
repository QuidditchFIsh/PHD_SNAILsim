from math import *
from qutip import *
PI = 3.14159265359 

omega1   = 4
omega2   = 10
omega3   = 17

omegaM = 8.45
omegaP = 35

R = 1/sqrt(2) * (sigmay() + sigmaz())

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

#identity 

q1 = tensor(a, qeye(2),qeye(2),qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2),qeye(2),qeye(2))
q3 = tensor(qeye(2),qeye(2),a,qeye(2),qeye(2))
sM = tensor(qeye(2),qeye(2),qeye(2),sigmap(),qeye(2))
sP = tensor(qeye(2),qeye(2),qeye(2),qeye(2),sigmap())

sx1 = tensor(sigmax(),qeye(2),qeye(2),qeye(2),qeye(2))
sx2 = tensor(qeye(2),  sigmax() ,qeye(2),qeye(2),qeye(2))
sx3 = tensor(qeye(2),qeye(2),  sigmax() ,qeye(2),qeye(2))

sy1 = tensor( sigmay() ,qeye(2),qeye(2),qeye(2),qeye(2))
sy2 = tensor(qeye(2),  sigmay() ,qeye(2),qeye(2),qeye(2))
sy3 = tensor(qeye(2),qeye(2),  sigmay() ,qeye(2),qeye(2))
sy4 = tensor(qeye(2),qeye(2),qeye(2),  sigmay() ,qeye(2))

sz1 = tensor( sigmaz() ,qeye(2),qeye(2),qeye(2),qeye(2))
sz2 = tensor(qeye(2),  sigmaz() ,qeye(2),qeye(2),qeye(2))
sz3 = tensor(qeye(2),qeye(2),  sigmaz() ,qeye(2),qeye(2))
sz4 = tensor(qeye(2),qeye(2),qeye(2)	 ,sigmaz(),qeye(2))
