import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from Constants import *
from math import *
import time
import datetime
import Constants as cons
import os

def H1_rot1(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot3(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot3d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot12_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
'''
def H1_rot1(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot1d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot2(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot2d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot3(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot3d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot12_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot12_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot13_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot13_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))

def H1_rot23_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot23_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))


def H1_rot_123_ppp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_ppm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_pmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_pmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_mpp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_mpm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_mmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
def H1_rot_123_mmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) + cos(omega1 * t + 0.5*PI) + cos(omega2 * t + 0.5*PI)*cos(omega3 * t) + cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))
'''

omega1 	= 20
omega2 	= 15
omega3 	= 8
omegad 	= 20

#R = 1/sqrt(2) * (sigmay() + sigmaz())
R=1

one  = R*basis(2,1)
zero = R*basis(2,0)

a = R * sigmap() * R

q1 = tensor(a, qeye(2),qeye(2))
q2 = tensor(qeye(2),a,qeye(2))
q3 = tensor(qeye(2),qeye(2),a)

EJ = 0.05
H0 = 0*(omega1 * q1.dag()*q1 + omega2 * q2.dag()*q2 + omega3 * q3.dag()*q3)
'''
H = [H0,[EJ*q1,H1_test1],[EJ*q1.dag(),H1_test1d],[EJ*q2,H1_test1],[EJ*q2.dag(),H1_test1d],[EJ*q3,H1_test1],[EJ*q3.dag(),H1_test1d],
[EJ * q1*q2,H1_test1],[EJ * q1*q2.dag(),H1_test1],[EJ * q1.dag()*q2,H1_test1],[EJ * q1.dag()*q2.dag(),H1_test1],
[EJ * q1*q3,H1_test1],[EJ * q1*q3.dag(),H1_test1],[EJ * q1.dag()*q3,H1_test1],[EJ * q1.dag()*q3.dag(),H1_test1],
[EJ * q2*q3,H1_test1],[EJ * q2*q3.dag(),H1_test1],[EJ * q2.dag()*q3,H1_test1],[EJ * q2.dag()*q3.dag(),H1_test1]]
'''

mult1a = 3 * EJ
mult1b =-3 *2 * EJ 
mult2a = EJ
mult2b = -2 * EJ
mult3  = 0.66666 * EJ

'''
mult1a = EJ
mult1b = EJ
mult2a = EJ
mult2b = EJ
mult3  = EJ
'''

H = [H0,[mult1a*q1,H1_rot1],[mult1a*q1.dag(),H1_rot1d],[mult1a*q2,H1_rot2],[mult1a*q2.dag(),H1_rot2d],[mult1b*q3,H1_rot3],[mult1b*q3.dag(),H1_rot3d],
[mult2a * q1*q2,H1_rot12_pp],[mult2a * q1*q2.dag(),H1_rot12_pm],[mult2a * q1.dag()*q2,H1_rot12_mp],[mult2a * q1.dag()*q2.dag(),H1_rot12_mm],
[mult2b * q1*q3,H1_rot13_pp],[mult2b * q1*q3.dag(),H1_rot13_pm],[mult2b * q1.dag()*q3,H1_rot13_mp],[mult2b * q1.dag()*q3.dag(),H1_rot13_mm],
[mult2b * q2*q3,H1_rot23_pp],[mult2b * q2*q3.dag(),H1_rot23_pm],[mult2b * q2.dag()*q3,H1_rot23_mp],[mult2b * q2.dag()*q3.dag(),H1_rot23_mm],
[mult3 * q1*q2*q3,H1_rot_123_ppp],[mult3 * q1*q2*q3.dag(),H1_rot_123_ppm],[mult3 * q1*q2.dag()*q3,H1_rot_123_pmp],[mult3 * q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult3 * q1.dag()*q2*q3,H1_rot_123_mpp],[mult3 * q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult3 * q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult3 * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm],]
'''
mult  = 0.01
mult2 = 0.01
H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[q3,H1_rot3],[q3.dag(),H1_rot3d],
[mult * q1*q2,H1_rot12_pp],[mult * q1*q2.dag(),H1_rot12_pm],[mult * q1.dag()*q2,H1_rot12_mp],[mult * q1.dag()*q2.dag(),H1_rot12_mm],
[mult * q1*q3,H1_rot13_pp],[mult * q1*q3.dag(),H1_rot13_pm],[mult * q1.dag()*q3,H1_rot13_mp],[mult * q1.dag()*q3.dag(),H1_rot13_mm],
[mult * q2*q3,H1_rot23_pp],[mult * q2*q3.dag(),H1_rot23_pm],[mult * q2.dag()*q3,H1_rot23_mp],[mult * q2.dag()*q3.dag(),H1_rot23_mm],
[mult2 * q1*q2*q3,H1_rot_123_ppp],[mult2 * q1*q2*q3.dag(),H1_rot_123_ppm],[mult2 * q1*q2.dag()*q3,H1_rot_123_pmp],[mult2 * q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult2 * q1.dag()*q2*q3,H1_rot_123_mpp],[mult2 * q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult2 * q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult2 * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm]]

H0  = 0 * tensor(a,a,a)

mult  = 0.01
mult2 = 0.01

H = [H0,[q1,H1_rot1],[q1.dag(),H1_rot1d],[q2,H1_rot2],[q2.dag(),H1_rot2d],[q3,H1_rot3],[q3.dag(),H1_rot3d],
[mult * q1*q2,H1_rot12_pp],[mult * q1*q2.dag(),H1_rot12_pm],[mult * q1.dag()*q2,H1_rot12_mp],[mult * q1.dag()*q2.dag(),H1_rot12_mm],
[mult * q1*q3,H1_rot13_pp],[mult * q1*q3.dag(),H1_rot13_pm],[mult * q1.dag()*q3,H1_rot13_mp],[mult * q1.dag()*q3.dag(),H1_rot13_mm],
[mult * q2*q3,H1_rot23_pp],[mult * q2*q3.dag(),H1_rot23_pm],[mult * q2.dag()*q3,H1_rot23_mp],[mult * q2.dag()*q3.dag(),H1_rot23_mm],
[mult2 * q1*q2*q3,H1_rot_123_ppp],[mult2 * q1*q2*q3.dag(),H1_rot_123_ppm],[mult2 * q1*q2.dag()*q3,H1_rot_123_pmp],[mult2 * q1*q2.dag()*q3.dag(),H1_rot_123_pmm],
[mult2 * q1.dag()*q2*q3,H1_rot_123_mpp],[mult2 * q1.dag()*q2*q3.dag(),H1_rot_123_mpm],[mult2 * q1.dag()*q2.dag()*q3,H1_rot_123_mmp],[mult2 * q1.dag()*q2.dag()*q3.dag(),H1_rot_123_mmm],]
'''

tlist = np.linspace(0,2**8,2**9)
R=1
sx1 = tensor(R * sigmax() * R,qeye(2),qeye(2))
sx2 = tensor(qeye(2), R * sigmax() * R,qeye(2))
sx3 = tensor(qeye(2),qeye(2), R * sigmax() * R)

sy1 = tensor(R * sigmay() * R,qeye(2),qeye(2))
sy2 = tensor(qeye(2), R * sigmay() * R,qeye(2))
sy3 = tensor(qeye(2),qeye(2), R * sigmay() * R)

sz1 = tensor(R * sigmaz() * R,qeye(2),qeye(2))
sz2 = tensor(qeye(2), R * sigmaz() * R,qeye(2))
sz3 = tensor(qeye(2),qeye(2), R * sigmaz() * R)

c_ops = [0.001*q1,0.001*q2,0.001*q3,0.002*sz1,0.002*sz2,0.002*sz3]

outputstr = ''

start = time.time()
for i in range(0,3):
	if i == 0:
		psi0 = tensor(zero,zero,zero);Tdm = tensor(zero,zero,zero)
		outputstr = 'Output/Toffoli_25-03-19/fidelity000.dat'
		print('1')
	if i == 1:
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Toffoli_25-03-19/fidelity110.dat'
		print('2')
	if i == 2:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Toffoli_25-03-19/fidelity111.dat'
		print('3')
	'''
	if i == 3:
		psi0 = tensor(zero,one,one);Tdm = tensor(zero,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity011.dat'
	if i == 4:
		psi0 = tensor(one,zero,zero);Tdm = tensor(one,zero,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity100.dat'
	if i == 5:
		psi0 = tensor(one,zero,one);Tdm = tensor(one,zero,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity101.dat'
	if i == 6:
		psi0 = tensor(one,one,zero);Tdm = tensor(one,one,one)
		outputstr = 'Output/Toffoli_13-02-19/fidelity110.dat'
	if i == 7:
		psi0 = tensor(one,one,one);Tdm = tensor(one,one,zero)
		outputstr = 'Output/Toffoli_13-02-19/fidelity111.dat'
	'''

	result = mesolve(H,psi0,tlist,c_ops,[sx1,sy1,sz1,sx2,sy2,sz2,sx3,sy3,sz3],options = Options(nsteps = 8000,store_states = True,store_final_state = True))


	fidelity_dat = []
	for j in range(0,len(tlist)):
	 		fidelity_dat.append(fidelity(result.states[j],Tdm))

	with open(outputstr,'w') as f1:
		for j in fidelity_dat:
			f1.write(str(j) + "\n")


end = time.time()
print('Time Taken for Simulation:')
print(end - start)
'''
outputstr = 'Output/Toffoli_13-02-19/Simulation_Data.dat'

x = np.genfromtxt("Output/Toffoli_13-02-19/fidelity000.dat")
f = np.genfromtxt("Output/Toffoli_13-02-19/fidelity000.dat")
g = np.genfromtxt("Output/Toffoli_13-02-19/fidelity110.dat")


idx = np.argwhere(np.diff(np.sign(f - g))).flatten()
print(idx)
print(max(f[idx]))

with open(outputstr,'w') as file:
	file.write('Simulation Parameters:\n Omega_1=' + str(omega1) +'\n Omega_2=' + str(omega2) + '\n Omega_3=' + str(omega3))
	file.write('Time Taken =' + str(end-start))
	file.write('Max Fidelity = ' + str(max(f[ifx]))) 
'''