# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:14:02 2019

@author: rique
"""

lista = [-1, 2, -3, 4, -5, 6]
suma = 0

# El comando Break permite finalizar con un for, esto es decir que si se cumple la condicion establecida,
# se deja de recorrer esa variable
for numero in lista:
    if numero > 4: # si el numero es mayor a 4 se deja de sumar numeros a la suma de variables
        break
    suma += numero
print (suma)
        
