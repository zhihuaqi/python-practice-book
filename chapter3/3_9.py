#!/usr/bin/env python
import sys
import re
def phone(x):
	match=re.search(r'^(\d{3}-\d{3}-\d{4})$', x)
	if match:
		print("true")
	else:
		print("false")
phone(sys.argv[1])
