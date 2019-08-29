# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 22:54:32 2019

@author: rique
"""

import numpy as np
a = np.random.random((3,3))
print (a)

np.set_printoptions(precision=2, suppress=True) #Este comando permite mostrar solo dos cifras significativas
print (a)

b = np.random.randint(1, 20, 4) #Crea una matriz de 4 elementos aleatorios del 1 al 20
print (b)

print (a.min())
print (a.max())
print (a.mean())
print (a.var())
print (a.std())

print (b.reshape(2,2))


