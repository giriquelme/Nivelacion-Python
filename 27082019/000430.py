# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:47:55 2019

@author: rique
"""
import numpy as np
# Se comenzara creando una lista
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #creacion de un lista del 1 al 10

b = np.array([a_list]) #la convertimos en una matriz
print (b)

z = np.random.randint(100, size=10)
# Se crea una matriz con elementos aleatorios del 1 al 100 con un largo de 10
print (z)

# para imprimir un número de la matriz lo citamos entre corchetes
# quiero imprimir el ultimo numero de lista

print (z[9])
print (z[4: 8])
