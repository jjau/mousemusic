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
