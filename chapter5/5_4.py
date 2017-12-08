#!/usr/bin/env python
import os
import sys
def findfiles(dir1):
	list_directory = os.listdir(dir1)
	for l in list_directory:
		list1=[dir1, l]
		dir2="/".join(list1)
		if os.path.isfile(dir2):
			yield dir2
		elif os.path.isdir(dir2):
			for f in findfiles(dir2):
				yield f
def compute_py(lines, n):
	for l in lines:
		if l.endswith(".py"):
			n += 1
	return n 

def main(dir1):
	lines=findfiles(dir1)
	num = compute_py(lines, 0)
	print(num)
x=sys.argv[1]
main(x)
