import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time

Wlist = np.linspace(1,500,500)
tlist = np.linspace(0, 1, 1000)

for i in [315,210,140,280,35,175,105]:
	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity111.txt','r')
	data1 = f.read().splitlines()
	data1 = [float(j) for j in data1]
	plt.plot(tlist,data1)
	plt.title("Fidelity111_" + str(i) + " vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity111.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity110.txt','r')
	data2 = f.read().splitlines()
	data2 = [float(j) for j in data2]
	plt.plot(tlist,data2)
	plt.title("Fidelity110_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity110.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity101.txt','r')
	data3 = f.read().splitlines()
	data3 = [float(j) for j in data3]
	plt.plot(tlist,data3)
	plt.title("Fidelity101_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity101.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity011.txt','r')
	data4 = f.read().splitlines()
	data4 = [float(j) for j in data4]
	plt.plot(tlist,data4)
	plt.title("Fidelity011_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity011.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity001.txt','r')
	data5 = f.read().splitlines()
	data5 = [float(j) for j in data5]
	plt.plot(tlist,data5)
	plt.title("Fidelity001_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity001.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity010.txt','r')
	data6 = f.read().splitlines()
	data6 = [float(j) for j in data6]
	plt.plot(tlist,data6)
	plt.title("Fidelity010_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity010.png')
	plt.clf()
	f.close()

	f = open('../Output/RF_25-01-19/RF-freq_explore/RF_SQUID_' + str(i) + '_fidelity100.txt','r')
	data7 = f.read().splitlines()
	data7 = [float(j) for j in data7]
	plt.plot(tlist,data7)
	plt.title("Fidelity100_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelity100.png')
	plt.clf()
	f.close()

	plt.plot(tlist,data1)
	plt.plot(tlist,data2)
	plt.plot(tlist,data3)
	plt.plot(tlist,data4)
	plt.plot(tlist,data5)
	plt.plot(tlist,data6)
	plt.plot(tlist,data7)
	plt.title("Fidelity100_" + str(i) + "  vs Time")
	plt.xlabel("Time")
	plt.ylabel("Fidelity")
	plt.savefig('../Output/RF_25-01-19/Img/RF_SQUID_' + str(i) + '_fidelityALL.png')
	plt.clf()
	f.close()

