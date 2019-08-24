# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:20:26 2019

@author: rique
"""
# Creamos una lista de numeros positivos y negativos
lista = [-1, -2, -3, 4, 5, 6, 7, 8, 9]

# Queremos sumar solo los numeros negativos
total_negativos = 0
i = 0
while lista[i] < 0: # mientas lista[i] sea negativo se sumara al total de negativos
    total_negativos += lista[i] 
    i += 1
print (total_negativos)
