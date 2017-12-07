#!/usr/bin/env python
import sys
import inspect
def mypydoc(x):
		p=__import__(x)
		print 'DESCRIPTION:\n----------\n',p.__doc__,'\nFUNCTIONS\n---------\n'
		for y in dir(p):
			z = getattr(p,y)
			if inspect.isfunction(z):
				print(z.__doc__)
mypydoc(sys.argv[1])
