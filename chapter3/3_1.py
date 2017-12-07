#!/usr/bin/env python
from os import walk
import sys
mypath=sys.argv[1]

def report(x):
        f=[]
        for (dirpath, dirnames,filenames) in walk(x):
                f.extend(filenames)
                break
        print f

report(mypath)
