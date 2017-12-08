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

def printpath(lines):
	for l in lines:
		print l

def main(dir1):
	lines=findfiles(dir1)
	printpath(lines)
x=sys.argv[1]
main(x)
