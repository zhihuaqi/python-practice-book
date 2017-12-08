#!/usr/bin/env python
import sys
file1 = sys.argv[1]
x = sys.argv[2]
with open(file1, 'r') as f:
	for l in f:
		if x in l:
			print l
