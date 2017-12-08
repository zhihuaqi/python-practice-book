#!/usr/bin/env python
def map(function, list):
	list = [function(x) for x in list]
	return list
