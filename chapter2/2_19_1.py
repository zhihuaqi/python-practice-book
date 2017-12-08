#!/usr/bin/env python
with open('test1.txt', 'r') as f, open('head.txt', 'w') as o:
		i = 0
		for l in f:
			i += 1
			if i < 11:
				o.write("{}".format(l))
		
			
				
