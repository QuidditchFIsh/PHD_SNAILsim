from qutip import *
from scipy import *
from pylab import* 
#sigmay problem 
psi0 = (basis(2,0) + basis(2,1)).unit() 
rho0 = psi0*psi0.dag() 
H0 = 0*sigmax() 
H1 = sigmax() 
print(psi0) 
print(H0*psi0) 
H2 = sigmaz() 
def H1_coeff(t,args): 
	return t-1 
def H2_coeff(t,args): 
	return -t 
h_t = [H0,[H1, H1_coeff], [H2, H2_coeff]] 
ntraj = 500 
tlist = linspace(0, 3, 100) 
medata = mesolve(h_t, rho0, tlist, [], [sigmay()], args = {}) 
mcdata = mcsolve(h_t, psi0, tlist, [], [sigmay()], ntraj = ntraj, args = {}) 
fig,axes = subplots(1,1,figsize=(12,6)) 
axes.plot(mcdata.expect[0], color="green", alpha =0.6, label = "mcsolve") 
axes.plot(medata.expect[0], color="blue", alpha =0.6, label = "mesolve") 
axes.set_xlabel(r'$\frac{t}{t_f}$') 
axes.set_ylabel('Expectation value') 
axes.legend(("mcsolve", "mesolve")) 
show()