#!/usr/bin/env python
def lensort(list):
	list.sort(key=lambda x: len(x))
	print list
