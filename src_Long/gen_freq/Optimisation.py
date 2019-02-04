'''
Short script to optimise the frequencies

Turning into longer script look to maybe port to C++ if this gets slow in finding parameter space.
'''
import numpy as np
from scipy.optimize import minimize

F1 = 13.8
F2 = 13.1
F3 = 3.00

def constraint1(x):
    freqs1 = []

    F11 = x[0]
    F21 = x[1]
    F31 = x[2]

    freqs1.append(F11)
    freqs1.append(F21)
    freqs1.append(F31)

    freqs1.append(float(F11-F21))
    freqs1.append(float(F11-F31))
    freqs1.append(float(F21-F31))

    freqs1.append(float(F11+F21))
    freqs1.append(float(F11+F31))
    freqs1.append(float(F21+F31))

    freqs1.append(float(F11 + F21 + F31))
    freqs1.append(float(F11 + F21 - F31))
    freqs1.append(float(F11 - F21 + F31))
    freqs1.append(float(-F11 + F21 + F31))

    freqs1 = sorted(freqs1)

    diff = 10**20

    for i in range(12):
        if abs(freqs1[i+1] - freqs1[i]) < diff:
            diff = abs(freqs1[i+1] - freqs1[i])
    return diff - 0.6
def constraint2(x):
    freqs2 = []

    F12 = x[0]
    F22 = x[1]
    F32 = x[2]

    freqs2.append(F12)
    freqs2.append(F22)
    freqs2.append(F32)

    freqs2.append(float(F12-F22))
    freqs2.append(float(F12-F32))
    freqs2.append(float(F22-F32))

    freqs2.append(float(F12+F22))
    freqs2.append(float(F12+F32))
    freqs2.append(float(F22+F32))

    freqs2.append(float(F12 + F22 + F32))
    freqs2.append(float(F12 + F22 - F32))
    freqs2.append(float(F12 - F22 + F32))
    freqs2.append(float(-F12 + F22 + F32))

    freqs2 = [abs(i) for i in freqs2]

    return min(freqs2) - 0.5


def difference(x0):

    freqs = []

    F1 = x0[0]
    F2 = x0[1]
    F3 = x0[2]

    freqs.append(F1)
    freqs.append(F2)
    freqs.append(F3)

    freqs.append(float(F1-F2))
    freqs.append(float(F1-F3))
    freqs.append(float(F2-F3))

    freqs.append(float(F1+F2))
    freqs.append(float(F1+F3))
    freqs.append(float(F2+F3))

    freqs.append(float(F1 + F2 + F3))
    freqs.append(float(F1 + F2 - F3))
    freqs.append(float(F1 - F2 + F3))
    freqs.append(float(-F1 + F2 + F3))

    return -1 * min(freqs)
''' Setting the Bounds and Contraints '''
b1 = (2,25)
bnds =[b1,b1,b1]

con1 = {'type': 'ineq', 'fun' : constraint1}
con2 = {'type': 'ineq', 'fun' : constraint2}

cons = [con1,con2]

'''Opening a File for output '''
opt_out = []
opt_out_file = open("Optimization_Output.dat","w")
opt_freq = []
opt_str = []

''' Initalising the loop and the inital conditions'''
x0 = [3,3,3]
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,5):
            x = [x0[0] + i,x0[1] + j , x0[2] + k]
            if(x[1] != x[0] and x[1] != x[2]):
                sol = minimize(difference,x,method='SLSQP',bounds=bnds,constraints=cons)
                opt_out.append([float(round(sol.x[0],5)),float(round(sol.x[1],5)),float(round(sol.x[2],5))])
                opt_freq.append([sol.x,sol.fun * -1])
x = {tuple(i) for i in opt_out}
frequencies = []
Capaticance = []
Josephson_Energy = []
Strength = []

with open('Frequency_Data.txt') as f:
    for line in f:
        line = line.strip().split()
        frequencies.append(float(line[2]))
        Capaticance.append(float(line[1]))
        Josephson_Energy.append(float(line[0]))
        Strength.append(float(line[3]))
#print(Josephson_Energy)

frequencies = np.array(frequencies)
for i in x:
    temp = []
    temp.append((np.abs(frequencies - i[0])).argmin())
    temp.append((np.abs(frequencies - i[1])).argmin())
    temp.append((np.abs(frequencies - i[2])).argmin())

    opt_out_file.write(str(frequencies[int(temp[0])]) + " " + str(Capaticance[int(temp[0])])
                 + " " + str(Josephson_Energy[int(temp[0])]) + " " + 
                 str(frequencies[int(temp[1])]) + " " + str(Capaticance[int(temp[1])])
                 + " " + str(Josephson_Energy[int(temp[1])]) + " " +
                 str(frequencies[int(temp[2])]) + " " + str(Capaticance[int(temp[2])])
                 + " " + str(Josephson_Energy[int(temp[2])]) + " ")

