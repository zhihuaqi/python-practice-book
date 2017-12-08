#!/usr/bin/env python
with open('she.txt', 'r') as f, open('r.she.txt', 'w') as o:
	for l in f:
		info=l.rstrip('\n').split(' ')
		new=[]
		x=0
		for i in info:
			x += 1
			if x != len(info):
				new.insert(0, i)
			else:
				y = i[:-1]
				z = i[-1]
				new.insert(0, y)
		l1 = " ".join(new)
		o.write("{}{}\n".format(l1, z))
