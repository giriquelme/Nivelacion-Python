# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:44:24 2019

@author: rique
"""
import numpy as np
# Primero se definira una matriz de la forma numpy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (a)

#Para ver que valores de la matriz son menores o mayores a un numero establecido:
print (a < 5) #verificar que numeros son menores a 5
print (a > 4) #verificar que numeros son mayores a 4

# Para determinar donde esta la matriz en referencia a un numero establecido
print (a[ a > 6]) 

#Haremos lo mismo con una matriz aleatoria
b = np.random.randint(10, size=10)
print (b)
print (b < 5) 
print (b > 4) 

print (b[ b > 6]) 

