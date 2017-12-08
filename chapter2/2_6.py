#!/usr/bin/env python
def reverse(x):
	l = len(x)
	new = []
	for i in range(l):
		new.append(x[l-1-i])
	return new
		
