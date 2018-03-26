#!/usr/bin/python
# Walter Rasmussen - Spring 2018
# Fetches web page and prints to file.

import sys
import requests
import re

# Check args. 
if (len(sys.argv) != 2):
	print "fix your args"
	sys.exit()

# Fetchs contents of url given in arg. 
url = sys.argv[1]

m = re.match( "([0-1]?[0-9]|2[0-4]):([0-5][0-9]|60):([0-5][0-9]|60)", url)

print(m)
