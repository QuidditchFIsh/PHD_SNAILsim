def genlist(f1,f2,f3):
	x = []
	x.append(abs(f1))
	x.append(abs(f2))
	x.append(abs(f3))
	x.append(abs(f1 + f2))
	x.append(abs(f1 - f2))
	x.append(abs(f1 + f3))
	x.append(abs(f1 - f3))
	x.append(abs(f2 + f3))
	x.append(abs(f2 - f3))
	x.append(abs(f1 + f2 + f3))
	x.append(abs(f1 + f2 - f3))
	x.append(abs(f1 - f2 + f3))
	x.append(abs(-f1 + f2 + f3))

	return x

def genlist2(f1,f2):
	x = []
	x.append(abs(f1))
	x.append(abs(f2))
	x.append(abs(f1 + f2))
	x.append(abs(f1 - f2))

	return x


with open('Frequencies2','w') as file:
	for i in range(1,25):
		for j in range(1,25):

				lst = genlist2(i,j)

				if len(lst) == len(set(lst)):
					if 1 not in lst:
						if 2 not in lst:
							if max(lst) < 30:
								diff = 10**20
								file.write(str(lst[2]) +' ' +  str(lst[3]) + '\n')
								lst = sorted(lst)
								for l in range(0,3):
									if lst[l +1] - lst[l] < diff:
										diff = lst[l +1] - lst[l]
				lst = []
'''
with open('Frequencies','w') as file:
	for i in range(1,25):
		for j in range(1,25):
			for k in range(1,25):

				lst = genlist(i,j,k)

				if len(lst) == len(set(lst)):
					if 1 not in lst:
						if 2 not in lst:
							if max(lst) < 30:
								diff = 10**20
								file.write(str(lst) + ' ')
								lst = sorted(lst)
								for l in range(0,12):
									if lst[l +1] - lst[l] < diff:
										diff = lst[l +1] - lst[l]
								file.write(str(diff) + '\n')
				lst = []
'''