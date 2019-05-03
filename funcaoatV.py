# coding=utf-8
from __future__ import division
import numpy as np
import math
import sys
from sympy import *
init_printing(use_unicode=True)

#define x como variávei simbólica
x = symbols('x')

def f(x): return (1/(x*(10**-6)))


print(f(50))
