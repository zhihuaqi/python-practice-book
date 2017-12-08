#!/usr/bin/env python
class A:
        def f(self):
                return self.g()

        def g(self):
                return 'A'

class B(A):
        def g(self):
                return 'B'
