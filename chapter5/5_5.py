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
def find_py(lines):
	for l in lines:
		if l.endswith(".py"):
			yield l

def compute_line_of_code(files):
	for f in files:
		n = 0
		with open(f, 'r') as f1:
			for l in f1:
				n += 1
		yield n

def main(dir1):
	lines=findfiles(dir1)
	files=find_py(lines)
	num=sum(compute_line_of_code(files))
	print(num)

x=sys.argv[1]
main(x)
