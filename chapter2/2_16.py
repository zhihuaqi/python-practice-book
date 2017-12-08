#!/usr/bin/env python
def extsort(x):
	for i in range(len(x)):
		x[i] = x[i].split('.')
	x.sort(key=lambda x: x[1])
	for i in range(len(x)):
		x[i] = ".".join(x[i])
	return x
#print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
