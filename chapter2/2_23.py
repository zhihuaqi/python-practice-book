#!/usr/bin/env python 
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
with open(file1, 'r') as f:
	length = 0
	for l in f:
		new = l.rstrip('\n')
		if len(new) > length:
			length = len(new)
f.close()
with open(file1, 'r') as f, open(file2, 'w') as o:
	for l in f:
		new = l.rstrip('\n')
		x = (length-len(new))/2
		blank = []
		for i in range(x):
			blank.append(" ")
		line = "".join(blank) 
		o.write("{}{}{}\n".format(line, new, line))

