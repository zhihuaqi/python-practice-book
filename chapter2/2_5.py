#!/usr/bin/env python
def factorial(x):
	r = 1
	for i in range(x):	
		r = r*(i+1)
	return r

#if __name__ == "__main__":
#	print ("result: {}".format(factorial(4)))
