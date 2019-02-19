from qutip import *
'''
a = 25.0
b = 13.0 
c = 5.0

print(a)
print(b)
print(c)
print(b + c)
print(b - c)
print(a + c)
print(a - c)
print(a + b)
print(a - b)
print(a + b + c)
print(a + b - c)
print(a - b + c)
print(-a + b + c)
'''

one = basis(2,1)
zero = basis(2,0)

psi0 = tensor(one ,zero ,one  )

print(destroy(2))
print(destroy(2).dag())

print(expect(psi0.ptrace(0),sigmaz()))

b=Bloch()
b.add_states(psi0.ptrace(0))
b.add_states(psi0.ptrace(1))
b.add_states(psi0.ptrace(2))
b.show()