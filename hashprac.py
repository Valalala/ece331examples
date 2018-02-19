#!/usr/bin/python
import os
#print os.environ
#print os.environ[2]
#print os.environ.keys()
for k in os.environ.keys():
    print k, os.environ[k]

