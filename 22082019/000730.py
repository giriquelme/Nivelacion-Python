# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:17:28 2019

@author: rique
"""

000730


# Creamos una lista 

l = []

for i in range(1, 101): # se crea una losta del 1 al 100
    a = i % 2 # Si la division por 2 resulta 0, significa que el numero es par
    if a == 0:
        l.append(i) # Agregamos cada numero par a la lista
    
print l # Imprimimos una lista de números pares del 1, ... , 100