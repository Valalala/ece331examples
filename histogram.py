#!/usr/bin/python
import string
import fileinput

hist={}

for l in fileinput.input():
    #c=string.split(l)
    c=list(l)
    #print c
    for i in c:
        try:
            hist[i]+=1
        except:
            hist[i]=1

for k in sorted(dict.iterkeys(hist)):
    print k,hist[k]
