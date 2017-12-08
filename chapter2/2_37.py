#!/usr/bin/env python
def valuesort(dict):
	list = sorted(dict.keys())
	list1=[]
	for i in list:
		list1.append(dict[i])
	return list1
	
