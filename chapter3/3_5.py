#!/usr/bin/env python
import sys
x=sys.argv[1]
import urllib
response = urllib.urlopen(x)
content=response.read()
info=x.split('/')
if info[-1] == "":
		info[-1]= "index.html"
with open(info[-1], 'w') as o:
	o.write(content)

	
