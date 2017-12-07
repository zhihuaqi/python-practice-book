#!/usr/bin/env python
from os import walk
import sys
x=sys.argv[1]

f=[]
for (dirpath, dirnames,filenames) in walk(x):
	f.extend(filenames)
	break
dict1={}
for l in f:
	names=l.split('.')
	n = len(names) - 1
	if names[n] in dict1:
		dict1[names[n]] += 1
	else:
		dict1[names[n]] = 1
for key in dict1:
	print("{} {}".format(dict1[key], key))
