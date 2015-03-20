import numpy as np
#import matplotlib.pyplot as pp

#from scipy import fft, arange, ifft, io
#from numpy import sin, linspace, pi, cos, sin, random, array
#import numpy as np
#from scipy.io.wavfile import read, write

def  tonal_dissonance(f1, f2, v1=1, v2=1):
    """ 
    implements Sethares's parameterization of Plomb&Levelt
    dissonance curves from "Local Consonance and the
    relationship between timbre and scale", Jasa 1993.
    inputs:
        f1,f2: frequency of partial in Hz
        v1,v2: amplitude of partial           
    """
    a = 3.5
    b = 5.75
    d_star = 0.24
    s1 = 0.021 # perhaps 0.21 (CMJ)
    s2 = 19 
    s = d_star / (s1*min(f1,f2) + s2) 
    f_diff = abs(f2-f1) 
    diss = v1*v2*(np.exp(-a*s*f_diff) - np.exp(-b*s*f_diff))
    return diss 

def dissonance_curve(f0, n_octaves=1, cent_hop = 10):
	"""
	computes dissonance between a single tone at frequency 
	f0 and a range of frequencies spanning n_octaves over f0 
	sampled every cent_hop cents per semi-tone
	"""
	nfreqs = 1200/cent_hop #number of sampling points in an octave
	freqs = f0*np.exp2(range(0,nfreqs)*cent_hop/1200)
	diss = [0]*nfreqs 
	for i,freq in enumerate(freqs):
		diss[i] = tonal_dissonance(f0,freq)
	return {'frequencies': freqs, 'dissonance': diss}