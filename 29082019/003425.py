# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:52:51 2019

@author: rique
"""

import numpy as np
a = np.array([2, 3, 4, 5, 6])
print (a[1:3]) #arroja los valores en la posicion 1 y 2 ya que no cuenta el final
print (a[1: -2]) #arroja los valores desde la poscion 1 a la -2 que euivale a la posicion 3
print (a[:4]) #muestra todk hasta la posicion 4
print (a[: :2]) #muestra los valores de la mariz saltandose de 2 en 2

b = [1, 2, 3]
print (b[:1]) #otra forma de mostar los valores de la lista

c = np.arange(25).reshape(5, 5) #Crea una matriz de 25 dtos ordenados en 5 filas y 5 columnas
print (c)
red = c[:, 1::2] #Permite mostar solo las columnas que nos interesan
print (red)
yellow= c[4] #PErmite mostrar solo la fila de interés
print (yellow) 
print (c[1::2, ::2])
print (id(a)) 
print (red.flags)
red[-1, -1] = 0 #Cambia el valor de esa poricion po 0
print (red)
