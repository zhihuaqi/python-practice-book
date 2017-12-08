#!/usr/bin/env python
def enumerate(list):
	list=[(x,y) for x in range(len(list)) for y in list if list[x] ==y]
	return list
