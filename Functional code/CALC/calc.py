from math import *

EJ1 		= 3.83e-23
EJ2 		= 1.18e-23
EJ3 		= 3.11e-24

ECQ1 		= 3.6e-25
ECQ2 		= 2.7e-25
ECQ3 		= 1.66e-25

phiBar1 	= 0.36
phiBar2 	= 0.48
phiBar3 	= 0.5
phiBarM 	= 1.7

h   	 	= 6.63e-34

omega1	 	= 17 
omega2	 	= 10 
omega3		= 4 
omegaM		= 8.4 * 6.3

v1 	= omega1
v2 	= omega2
v3 	= omega3
v4 	= omega1 + omega2
v5 	= omega1 - omega2
v6 	= omega1 + omega3
v7 	= omega1 - omega3
v8 	= omega2 + omega3
v9 	= omega2 - omega3
v10	= omega1 + omega2 + omega3
v11	= omega1 + omega2 - omega3
v12	= omega1 - omega2 + omega3
v13	= omega1 - omega2 - omega3

v = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]
print(v)

#Calculations begin here
print("ECQ1")
res = ((ECQ1)/(h * phiBar1 * phiBarM))**2
print(res * (1/(omegaM - omega1)) * 10**(-6) )
print(res * (1/(omegaM + omega1)) * 10**(-6))

print("ECQ2")
res = ((ECQ2)/(h * phiBar2 * phiBarM))**2
print(res * (1/(omegaM - omega2)) * 10**(-6))
print(res * (1/(omegaM + omega2)) * 10**(-6))

print("ECQ3")
res = ((ECQ3)/(h * phiBar3 * phiBarM))**2
print(res * (1/(omegaM - omega3)) * 10**(-6))
print(res * (1/(omegaM + omega3)) * 10**(-6))


print("EJ1")
res = ((EJ1 * 0.1 * phiBar3)/(2*h))**2
print(res)
sum1 = 0
for i in v:
	res1 = (1/((omegaM + omega1) - i))
	res2 = (1/((omegaM - omega1) - i))
	#print(i)
	sum1 +=res1 * 10**(-18) * res 
	sum1 +=res2 * 10**(-18) * res

	#print(res1 * 10**(-18) * res)
	#print(res2 * 10**(-18) * res)
	#print("-----------------------")


print("EJ2")
res = ((EJ2 * 0.1 * phiBar3)/(2*h))**2
print(res)
sum2 = 0
for i in v:
	res1 = (1/((omegaM + omega2) - i))
	res2 = (1/((omegaM - omega2) - i))
	#print(i)
	sum2 +=res1 * 10**(-18) * res 
	sum2 +=res2 * 10**(-18) * res

	#print(res1 * 10**(-18) * res)
	#print(res2 * 10**(-18) * res)
	#print("-----------------------")


print("EJ3")
res = ((EJ3 * 0.1 * phiBar3)/(h))**2
print(res)
sum3 = 0
for i in v:
	res1 = (1/((omegaM + omega3) - i))
	res2 = (1/((omegaM - omega3) - i))
	#print(i)
	sum3 +=res1 * 10**(-18) * res 
	sum3 +=res2 * 10**(-18) * res

	#print(res1 * 10**(-18) * res)
	#print(res2 * 10**(-18) * res)
	#print("-----------------------")


print(sum1)
print(sum2)
print(sum3)

sum4 = 0
for i in v:
	sum4 += 0.075/(2*omega1 + i)
	sum4 += 0.075/(2*omega1 - i)
print(sum4)


