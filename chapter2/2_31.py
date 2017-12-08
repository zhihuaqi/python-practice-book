#!/usr/bin/env python
def parse(file, a, b):
	with open(file, 'r') as f:
		list=[]
		for l in f:
			if l.startswith(b):
				l1 = l
			else:
				info = l.rstrip('\n').split(a)
				list.append(info)
	return list
