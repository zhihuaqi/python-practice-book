#!/usr/bin/env python
import os
import sys
x=sys.argv[1]
f=[]
for (dirpath, dirnames,filenames) in os.walk(x):
	f.extend(filenames)
	break
for l in f:
	path="{}/{}".format(x,l)
	stat=os.stat(path)
	print("{}\t{}\t{}".format(l, stat.st_size, stat.st_mtime))
	
