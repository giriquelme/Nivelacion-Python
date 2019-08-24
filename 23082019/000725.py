# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:09:43 2019

@author: rique
"""
# Para corregir el error anterior es necesario agregar otra condicion al while
lista = range(1, 10)
i = 0
suma = 0
while i < len(lista) and  lista[i] > 0 : # Al agregar la segunda condicion se arregla el problema anterior por lo cual indica que el comando while no es necesariamente solo una condicion

    suma += lista[i]
    i += 1
print (suma)