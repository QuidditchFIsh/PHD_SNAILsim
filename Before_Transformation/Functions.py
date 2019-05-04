from math import *
from Constants import *
#Functions without the sM or sM.dag() term.
def H1_rot1(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )
def H1_rot1d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )
def H1_rot2(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot2d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot3(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot3d(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot12_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )
def H1_rot12_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )
def H1_rot12_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )

def H1_rot13_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot13_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot13_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )

def H1_rot23_pp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_pm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot23_mp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot23_mm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


def H1_rot_123_ppp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_ppm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_pmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_pmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mpp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mpm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )
def H1_rot_123_mmp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )
def H1_rot_123_mmm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )


###################################Functions with the SM term################################################
def H1_rot1_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot1d_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot2_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot2d_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot3_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot3d_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )

def H1_rot12_pp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot12_pm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot12_mp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot12_mm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )

def H1_rot13_pp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot13_pm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot13_mp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot13_mm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )

def H1_rot23_pp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot23_pm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot23_mp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot23_mm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )


def H1_rot_123_ppp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_ppm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_pmp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_pmm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_mpp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_mpm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_mmp_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )
def H1_rot_123_mmm_sMp(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) )*(cos(omegaM * t) + (0+1j)*sin(omegaM*t) )

#############################################Functions with the sM.dag() term##############################################
def H1_rot1_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot1d_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot2_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot2d_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot3_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot3d_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )

def H1_rot12_pp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot12_pm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot12_mp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot12_mm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )

def H1_rot13_pp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot13_pm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot13_mp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot13_mm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )

def H1_rot23_pp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot23_pm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot23_mp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot23_mm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t)))*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )


def H1_rot_123_ppp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_ppm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_pmp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_pmm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) + (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_mpp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_mpm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) + (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_mmp_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) + (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )
def H1_rot_123_mmm_sMm(t,*args):
	return (0.25*(-1*cos(omega3 * t) + cos(omega2*t + 0.5*PI) - cos(omega1 * t + 0.5*PI) - cos(omega2 * t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega3 * t) - cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI) + cos(omega1*t + 0.5*PI)*cos(omega2*t + 0.5*PI)*cos(omega3*t))) * (cos(omega1 * t) - (0+1j)*sin(omega1*t) )*(cos(omega2 * t) - (0+1j)*sin(omega2*t) )*(cos(omega3 * t) - (0+1j)*sin(omega3*t) ) * (cos(omegaM * t) - (0+1j)*sin(omegaM*t) )

#############################################Functions For rotating with no drive##############################################
def H1_rot_sMq1(t,*args):
	return (cos((omegaM + omega1)*t) + (0 + 1j)*sin((omegaM + omega1)*t))
def H1_rot_sMq2(t,*args):
	return (cos((omegaM + omega1)*t) + (0 + 1j)*sin((omegaM + omega2)*t))
def H1_rot_sMq3(t,*args):
	return (cos((omegaM + omega1)*t) + (0 + 1j)*sin((omegaM + omega3)*t))
def H1_rot_sMq1d(t,*args):
	return (cos((omegaM - omega1)*t) + (0 + 1j)*sin((omegaM - omega1)*t))
def H1_rot_sMq2d(t,*args):
	return (cos((omegaM - omega1)*t) + (0 + 1j)*sin((omegaM - omega2)*t))
def H1_rot_sMq3d(t,*args):
	return (cos((omegaM - omega1)*t) + (0 + 1j)*sin((omegaM - omega3)*t))
def H1_rot_sMdq1(t,*args):
	return (cos((-omegaM + omega1)*t) + (0 + 1j)*sin((-omegaM + omega1)*t))
def H1_rot_sMdq2(t,*args):
	return (cos((-omegaM + omega1)*t) + (0 + 1j)*sin((-omegaM + omega2)*t))
def H1_rot_sMdq3(t,*args):
	return (cos((-omegaM + omega1)*t) + (0 + 1j)*sin((-omegaM + omega3)*t))
def H1_rot_sMdq1d(t,*args):
	return (cos((-omegaM - omega1)*t) + (0 + 1j)*sin((-omegaM - omega1)*t))
def H1_rot_sMdq2d(t,*args):
	return (cos((-omegaM - omega1)*t) + (0 + 1j)*sin((-omegaM - omega2)*t))
def H1_rot_sMdq3d(t,*args):
	return (cos((-omegaM - omega1)*t) + (0 + 1j)*sin((-omegaM - omega3)*t))

