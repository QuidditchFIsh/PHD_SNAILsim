import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def H1_cos(t,*args):
	return cos(omega * t)

omega = 1.57

R = 1/sqrt(2) * (sigmax() + sigmay())
#R=1

a = R * sigmap() * R

q1 = tensor(a, qeye(2))
q2 = tensor(qeye(2),a)

q1d = q1.dag()
q2d = q2.dag()

zero = R * basis(2,0)
one  = R * basis(2,1)

H0  = 0*q1*q1d

H1_1 = 5 * ((q1 + q1d)) +  1* ((q2 + q2d)) + 5*(((q1 + q1d)) * ((q2 + q2d)))

H = [H0,[H1_1,H1_cos]]

psi0 = tensor(zero,zero)

tlist = np.linspace(0,10,1000)

sx1 = tensor(R * sigmax() * R,qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R)

c_ops = [0.01*q1,0.01*q2,0.02*sz1,0.02*sz2]

result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2])

fig, ax = plt.subplots(figsize=(12,6))
ax.plot(tlist, np.real(result.expect[0]), 'r')
ax.plot(tlist, np.real(result.expect[1]), 'b')
ax.plot(tlist, -1 * np.real(result.expect[2]), 'g')
ax.legend(("sx", "sy", "sz"))
ax.set_xlabel('Time')
ax.set_ylabel('expectation value')
fig.savefig('../Output/testing/gates1.png')
#plt.show()#

sphere=Bloch()
sphere.add_points([result.expect[0],result.expect[1],-1 *result.expect[2]], meth='l')
sphere.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
sphere.show()
s = sphere.fig
s.savefig('../Output/testing/bloch1.png')

fig1, ax1 = plt.subplots(figsize=(12,6))
ax1.plot(tlist, np.real(result.expect[3]), 'r')
ax1.plot(tlist, np.real(result.expect[4]), 'b')
ax1.plot(tlist, -1 * np.real(result.expect[5]), 'g')
ax1.legend(("sx", "sy", "sz"))
ax1.set_xlabel('Time')
ax1.set_ylabel('expectation value')
fig1.savefig('../Output/testing/gates2.png')
#plt.show()

sphere1=Bloch()
sphere1.add_points([result.expect[3],result.expect[4],-1 *result.expect[5]], meth='l')
sphere1.vector_color = ['r']
#sphere.add_vectors([np.sin(theta), 0, np.cos(theta)])
sphere1.show()
s1 = sphere1.fig
s1.savefig('../Output/testing/bloch2.png')
#sphere1.show()