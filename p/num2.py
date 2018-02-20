#!/usr/bin/python
from numpy import *
import matplotlib.pyplot as plt

def dB(val):
	return 20*log10(val)

def H(val):
	imag=array(val)*1j
	return 8000*(imag)/(1e6+5e3*imag+imag**2)

w=logspace(1,5)
plt.semilogx(w,dB(abs(H(w))))
plt.grid()
plt.title('Bode plot')
plt.xlabel('Freq, rad/sec')
plt.ylabel('dB')
plt.show()

