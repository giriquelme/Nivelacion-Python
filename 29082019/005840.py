# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:59:20 2019

@author: rique
"""

import numpy as np
a = np.array([3, -1, -2, 4, -6, 8])
print (a)
print (a < 3)
negativos = a < 0 #PErmite arrojar los datos negativos que componen la matriz
print (a[negativos])
a[a < 0] = 0 #se cambian los valores negativos por 0
print (a)

#operadores binarios
print ((a < 3) & (a > 8)) # & permite anañizar dos condiciones a la vez

f = 6
g = 9
print (f + g)
print (f.__add__(g)) #otra forma de escribir la suma
b = np.array([3, -1, -2, 4, -6, 8])
print (b[(b < 3) % (b > 8)])

print (np.nonzero(b[negativos]))
print (b.sort())



