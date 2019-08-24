# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:25:23 2019

@author: rique
"""

# Para utilizar el coando while true, debemos cerrar el ciclo con un break

lista = [-1, 2, -3, 4, -5, 6] # se crea una lista con numeros positivos y negativos
total = 0 # Variable que ira sumando los valores
i = 0 # Establecemos una especie de contador
while True:
    total += lista[i]
    i += 1
    if lista[i] == -5: # Si el numero de la lista es -5 se  termina con el aloritmo
        break
print (total) 