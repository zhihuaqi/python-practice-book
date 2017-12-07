#!/usr/bin/env python
import zipfile
import sys
def zip(x,y):
	file = zipfile.ZipFile(x, 'w')
	for f in y:
		file.write(f)
zip(sys.argv[1], sys.argv[2:])
