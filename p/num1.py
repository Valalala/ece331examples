#!/usr/bin/python
from numpy import *
from numpy.linalg import inv

a=array( [ (1,5,9), (-3,5,-2), (6,8,-7) ], dtype=double)
b=array([-3,4,-8], dtype=double)
print inv(a).dot(b)

