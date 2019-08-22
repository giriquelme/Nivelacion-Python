# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:03:02 2019

@author: rique
"""

000407

# Para crear una lista de números, sin la necesidad de hacerlo 1 por 1 utiizamos el comando range.

lista = range(1, 101)
print (lista)

for i in range(1, 101):
    print (i)

# Otra forma de sumar los elementos de una lista
total2 = 0
for i in range(1, 101):
    total2 += i
print (total2)