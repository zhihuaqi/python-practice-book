#!/usr/bin/env python
x=[1,2,3]
def product(list):
        r = 1
        for i in list:
                r = r * i
        return r
print ("result: {}".format(product(x)))
