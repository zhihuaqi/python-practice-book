#!/usr/bin/env python
def zip(list1, list2):
	list=[(x,y) for x in list1 for y in list2 if list1.index(x) == list2.index(y)]
	return list
