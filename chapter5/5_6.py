#!/usr/bin/env python
import os
import sys
import re
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

def get_line_of_code(files):
	for f in files:
		with open(f, 'r') as f1:
			for l in f1:
				yield l

def compute_line(lines):
	empty = re.compile(r'^\s*$')
	comment = re.compile(r'^\s*#.*$')
	n = 0
	for l in lines:
		if empty.match(l) or comment.match(l):
			pass
		else:
			n += 1
	return n

def main(dir1):
	lines=findfiles(dir1)
	files=find_py(lines)
	pylines=get_line_of_code(files)
	num=compute_line(pylines)
	print(num)

x=sys.argv[1]
main(x)
