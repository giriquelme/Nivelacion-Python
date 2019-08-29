# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:22:16 2019

@author: rique
"""

import numpy as np
ceros = np.zeros((2,3)) #mediante este comando se crea una matriz compuesta de 0, de 2 filas y 3 columnas
print (ceros)

uno = np.ones(20) #permite crear una matriz de 1 de largo 20
print (uno)

comp = np.array([1,3,5], dtype=np.int16) #Este comando permite comprimir las cifras, utilizando menos memoria
print (comp)

print (comp.dtype) 
print (comp.itemsize)

random = np.random.random((3,3)) #Este comando permite imprimir una matriz de valores aleatorios 
print (random)


