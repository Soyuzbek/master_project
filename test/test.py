# -*- coding: utf-8 -*-
import unittest
import numpy as np
from unittest import TestCase
from our import deriv, f


class TryTesting(TestCase):
    def setUp(self):
        self.f = f
        self.first = lambda x: 2*(np.exp(x**2)*x+np.cos(2*x))
        self.second = lambda x: 2*np.exp(x**2)*(2*x**2+1)-4*np.sin(2*x)
        self.third = lambda x: 4*np.exp(x**2)*x*(2*x**2+3)-8*np.cos(2*x)
        self.fourth = lambda x: 4*(np.exp(x**2)*(4*x**4+12*x**2+3) +
                                         4*np.sin(2*x))
        self.fifth = lambda x: 8*(np.exp(x**2)*x*(4*x**2+20*x**2+15) +
                                        4*np.cos(2*x))

    def test_deriv(self):
        x = 0
        h = 1e-5
        numeric = deriv(self.f, x, h, 3, 'central')
#        analytic = self.first(x)
        analytic = self.third(x)
        places = 1
        self.assertAlmostEqual(analytic, numeric, places)


if __name__ == '__main__':
    unittest.main()
