f1 = 9
f2 = 6
f3 = 7

print(f1)
print(f2)
print(f3)

print(f1 + f2)
print(f1 - f2)

print(f1 + f3)
print(f1 - f3)

print(f2 + f3)
print(f2 - f3)

print(f1 + f2 + f3)
print(f1 + f2 - f3)
print(f1 - f2 + f3)
print(-f1 + f2 + f3)

x = []
x.append(f1)
x.append(f2)
x.append(f3)
x.append(f1 + f2)
x.append(f1 - f2)
x.append(f1 + f3)
x.append(f1 - f3)
x.append(f2 + f3)
x.append(f2 - f3)
x.append(f1 + f2 + f3)
x.append(f1 + f2 - f3)
x.append(f1 - f2 + f3)
x.append(-f1 + f2 + f3)

x.sort()
print(x)
