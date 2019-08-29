# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:36:17 2019

@author: rique
"""

import numpy as np
# Veremos formas de crear una matriz
m1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (m1)

#Otra forma de crear una matriz
m2 = np.arange(1, 20, 5) # Significa que sera una matriz que parta del 1 y termina en el 20 de 5 en 5
print (m2)

m3 = np.linspace(1, 10, 20) # crea una matriz de puntos flotantes desde el 1 al 20
print (m3)

print (m3.reshape(2, 10)) # ordenamos la matriz en dos filas de 10 cifras cada una
print (m3.size) #Indica el tamaño de la matriz
print (m3.dtype) #Sirve para indicar el tipo de datos que componen la matriz
