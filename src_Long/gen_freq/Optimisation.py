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
    return abs((x[0]- x[1] + x[2])) - 0.1
def constraint2(x):
    return abs((x[0]- x[1] - x[2])) - 0.1
def constraint3(x):
    x1 = abs(x[0]-x[1])
    x2 = abs(x[0]-x[2])
    x3 = abs(x[1]-x[2])
    return abs(min(x1,x2,x3)) - 0.6

def difference(x0):

    two_body = []
    three_body = []

    F1 = x0[0]
    F2 = x0[1]
    F3 = x0[2]

    two_body.append(float(F1-F2))
    two_body.append(float(F1-F3))
    two_body.append(float(F2-F3))

    two_body.append(float(F1+F2))
    two_body.append(float(F1+F3))
    two_body.append(float(F2+F3))

    three_body.append(float(F1 + F2 + F3))
    three_body.append(float(F1 + F2 - F3))
    three_body.append(float(F1 - F2 + F3))
    three_body.append(float(F1 - F2 - F3))

    min = 1000
    for i in three_body:
        if(abs(i-j) < min):
            min = abs(i-j)
    return -1 * min
''' Setting the Bounds and Contraints '''
b1 = (2,25)
bnds =[b1,b1,b1]

con1 = {'type': 'ineq', 'fun' : constraint1}
con2 = {'type': 'ineq', 'fun' : constraint2}
con3 = {'type': 'ineq', 'fun' : constraint3}

cons = [con1,con2,con3]

'''Opening a File for output '''
opt_out = []
opt_out_file = open("Optimization_Output.dat","w")
opt_freq = []
opt_str = []

''' Initalising the loop and the inital conditions'''
x0 = [3,3,3]
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
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
                 str(frequencies[int(temp[1])]) + " " + str(Capaticance[int(temp[1])])
                 + " " + str(Josephson_Energy[int(temp[1])]) + " ")

