# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:35:43 2019

@author: rique
"""

a = list(range(10))
print (a)

print (a[2]) #indica el numero que ocupa dicha posicion
a[0] = 10 #permite cambiar el valor asociado
print (a) 

b = np.array(a) #creo una matriz a partir de una lista
print (b)
print (b.dtype)

c = np.array([[1, 2, 3], [10, 20, 30]]) #crea una matriz de 2 dimensiones
print (c) 
print (c.dtype)
print (c.ndim)
print (c.shape) #indica el numero de filas y columnas de la matriz
print (c.T) #cre la matriz traspuesta
print (c.size)
print (c.nbytes)
print (c[0])
print (c[0, 0])
