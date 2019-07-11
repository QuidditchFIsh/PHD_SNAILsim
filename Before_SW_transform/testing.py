######################################################################################
#						TESTING SUITE FOR ALL FUNCTIONS								 #
######################################################################################

from Constants import *
from Functions import *


result = []
with open('test.dat','w') as file:
	for i in range(0,2000):
		t = i*0.01
		#print(drive(t))
		file.write(str(drive(t)) + "\n")