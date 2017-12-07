#!/usr/bin/env python
import sys
x=sys.argv[1]
import re
info=re.findall(r'\w+', x)
print ('-').join(info)
