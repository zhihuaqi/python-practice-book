#!/usr/bin/env python
import tablib
import sys
def csv2xls(x,y):
	with open(x, 'r') as f:
		n = 1
		data = tablib.Dataset()
		for l in f:
			info = l.split(',')
			data.append([info[0], info[1], info[2], info[3]])
			n = n + 1
	with open(y, 'wb') as o:
		o.write(data.xls)
csv2xls(sys.argv[1], sys.argv[2])
