# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:38:46 2019

@author: rique
"""

import numpy as np
# Operador % indica si la operacion division es exacta o no

print (1 % 2) # Resto de 1
print (4 & 2) # Resto de 0

# Se creara una matriz de 4x4 y como elementos seran los numero del 0,15
a = np.arange(16).reshape(4, 4)
print (a)

print (a & 3)
print (a & 3 == 0)
print (a[a % 3 == 0])

output = np.empty_like(a)
print (output)
output = np.empty_like(a, dtype= 'float')
print (output)
print (output.fill(np.nan))
mask = a % 3 == 0
output[mask] = a[mask]
print (output)
print (np.where(a % 3 == 3, a, np.nan))
print (a[mask])