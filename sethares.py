from pylab import plot, show, title, xlabel, ylabel, subplot, savefig, grid, specgram, suptitle, yscale
from scipy import fft, arange, ifft, io
from numpy import sin, linspace, pi, cos, sin, random, array
#import numpy as np
#from scipy.io.wavfile import read, write
from matplotlib import pyplot

def plotCosAndSin():
	X = linspace(-pi, pi, 256, endpoint=True)
	C, S = cos(X), sin(X)
	plot(X, C)
	plot(X, S)
	show()