#!/usr/bin/env python
import urllib
import json
import sys
def myip(x):
	f=urllib.urlopen(x).read()
	data = json.loads(f)
	print data['origin']
myip(sys.argv[1])
