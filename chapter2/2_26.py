#!/usr/bin/env python
def filter(function, x):
	list = [i for i in x if function(i)]
	return list

