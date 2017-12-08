#!/usr/bin/env python
with open('she.txt', 'r') as f, open('t.she.txt', 'w') as o:
	new = []
	for l in f:
		new.insert(0,l)
	for i in new:
		o.write("{}".format(i))
		
	
		

