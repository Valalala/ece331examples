#!/usr/bin/python
import csv

r=csv.reader(open('d','rb'))
for row in r:
	try:
		print int(row[3])
	except:
		pass
