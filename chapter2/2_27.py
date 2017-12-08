#!/usr/bin/env python
def triplet(a):
	list = [(x,y,z)for x in range(1,a) for y in range(1,a) for z in range(1,a) if x + y == z and x >= y]
	return list
