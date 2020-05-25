import numpy as np
from functools import reduce


# Берилген функсианын туундулары
def deriv(f, arg, h, degree, method='central'):
    """ returns `degree` derivative of `f` function
    on `arg` for `h` neighbour
    """
    if degree == 0:
        return f(arg)
    if method == 'central':
        return (deriv(f, arg+h, h, degree-1, method) -
                deriv(f, arg-h, h, degree-1, method))/(2*h)
    elif method == 'forward':
        return (deriv(f, arg+h, h, degree-1, method) -
                deriv(f, arg, h, degree-1, method))/h
    elif method == 'backward':
        return (deriv(f, arg, h, degree-1, method) -
                deriv(f, arg-h, h, degree-1, method))/h


def rnewton(f, h=0.01, initial=0, degree=5, eps=1e-5):
    x = [initial + np.sign(initial)*(1+np.abs(eps))
         if abs(initial) > 1e-3 else 1]
    d = np.abs(x[0]-initial)

    while d > eps:
        proots = np.roots([deriv(f, x[-1], h, deg)/np.math.factorial(deg)
                          for deg in range(degree, -1, -1)])
        proots = proots[np.abs(proots.imag) < 1e-50]
        if len(proots):
            x.append(proots[np.abs(proots).argmin()]+x[-1])
        else:
            break
        d = np.abs(x[-1]-x[-2])
    return [i.real for i in x[1:]]


def cnewton(f, h=0.01, initial=0, degree=5, eps=1e-5):
    x = [initial + np.sign(initial)*(1+np.abs(eps))
         if abs(initial) > 1e-3 else 1]
    d = np.abs(x[0]-initial)

    while d > eps:
        proots = np.roots([deriv(f, x[-1], h, deg)/np.math.factorial(deg)
                          for deg in range(degree, -1, -1)])
        proots = proots[np.abs(proots.imag) > 1e-50]
        if len(proots):
            x.append(proots[np.abs(proots).argmin()]+x[-1])
        else:
            break
        d = np.abs(x[-1]-x[-2])
    return x[1:]


def newton(f, h=0.01, initial=0, degree=5, eps=1e-5):
    x = [initial + np.sign(initial)*(1+np.abs(eps))
         if abs(initial) > 1e-3 else 1]
    d = np.abs(x[0]-initial)

    while d > eps:
        proots = np.roots([deriv(f, x[-1], h, deg)/np.math.factorial(deg)
                          for deg in range(degree, -1, -1)])
        if len(proots):
            x.append(proots[np.abs(proots).argmin()]+x[-1])
        else:
            break
        d = np.abs(x[-1]-x[-2])
    return x[1:]

#
#def nf(x, root):
#    j = reduce(lambda x, y: x*y, [x-i for i in root])
#    return (x**3-10)/j
#
#
def f(x):
    return x**6 -6*x**5+50*x**3-45*x**2 - 108*x +108


if __name__ == '__main__':
    x = 0
#    comp = cnewton(f, 0.01, 100)
    real = rnewton(f, 0.01, x)
    common = newton(f, 0.01, x)
#    print(common[-1])
