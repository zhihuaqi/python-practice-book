#!/usr/bin/env python
import sys
file1 = sys.argv[1]
file2 = sys.argv[2]
x = int(sys.argv[3])
with open(file1, 'r') as f, open(file2, 'w') as o:
	for l in f:
		new = l.rstrip('\n')
		if len(new) > x:
			n = x+1
			for i in range(n):
				n1 = n - i
				if new[n1] is " ":
					o.write("{}\n".format(new[:n1]))
					break
			o.write("{}\n".format(new[n1+1:]))
		else:
			o.write("{}\n".format(new))
		
