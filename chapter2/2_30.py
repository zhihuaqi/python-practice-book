#!/usr/bin/env python
def parse_csv(file):
	with open(file, 'r') as f:
		list=[]
		for l in f:
			info = l.rstrip('\n').split(',')
			list.append(info)
	return list
