#!/usr/bin/env python
f= open('test1.txt')
x=len(f.readlines())
f.close()
with open('test1.txt', 'r') as f, open('tail.txt', 'w') as o:
	i = 0
	for l in f:
		i += 1 
		if x-i < 10:
			o.write("{}".format(l))
