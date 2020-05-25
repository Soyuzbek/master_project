# -*- coding: utf-8 -*-

f = lambda x: x**2 - x - 1

def root(f, arg, h, degree):
    if degree == 0:
        return f(arg)
    return (root(f, arg+h, h, degree-1)-root(f, arg-h, h, degree-1))/(2*h)

print(root(f, 0, 1, 3))