# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:27:56 2019

@author: rique
"""

# Primero debemos importar la funcion al código
import numpy as np
# Se creara una matriz de 0 utilizando la función importada
a = np.zeros(19)
print (a)

print (a.shape) # Nos indica la cantidad de cifras que componen la matriz

# Crearemos una matriz de 1

b = np.ones(19)
print (b)

b = np.empty(3) # Este omando permite crear una matriz de 0 con la cantidad de cifras que uno le asigne
print (b)

c = np.linspace(5, 20, 4) # Este comando permite la creacion de una matriz, estableciendo el salto entre numeros, el comienzo y el final
print (c)

