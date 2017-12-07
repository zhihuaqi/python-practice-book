#!/usr/bin/env python
import sys
import urllib
import re
def links(x):
	r=urllib.urlopen(x)
	f=r.read()
	links = re.findall('http[s]?://\S+"', f)
	for l in links:
		info=l.split('"')
		print(info[0])

links(sys.argv[1])
