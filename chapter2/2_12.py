#!/usr/bin/env python
def group(list, s):
	l = len(list)
	n = l/s + 1
	n1 = l%s
	new = []
	if n1 ==0:
		for i in range(n-1):
			new.append([])
	else:
		for i in range(n):
			new.append([])
	for i in range(l):
		r1 = i/s
		r2 = i%s
		new[r1].append(list[i])
	return new
		
		

	
