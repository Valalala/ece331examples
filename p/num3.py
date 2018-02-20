#!/usr/bin/python
from numpy import *
import matplotlib.pyplot as plt

a=random.rand(100000,1)
plt.hist(a,200,normed=True)
plt.grid()
plt.title('Bode plot')
plt.xlabel('Freq, rad/sec')
plt.ylabel('dB')
plt.show()

