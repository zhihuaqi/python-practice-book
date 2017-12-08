#!/usr/bin/env python
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
x = int(sys.argv[3])
with open(file1, 'r') as f, open(file2, 'w') as o:
	for l in f:
		new = l.rstrip('\n')
		if len(new) > x:
			o.write("{}\n".format(new[:x]))
		o.write("{}\n".format(new[x:]))
		

