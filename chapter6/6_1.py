#!/usr/bin/env python
def product(x,y):
        if x == 0 or y == 0:
                return 0
        else:
                pro = x + product(x, y-1)
                return pro
