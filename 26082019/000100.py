# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:03:31 2019

@author: rique
"""

# Creación de un diccionario:
# El diccionario se crea de forma similar a una lista pero entre llaves "{}"

diccionario = {} # Se crea un diccionario vacio
diccionario = {"gabriel": 24, "palmy": 52, "juan": 52, "jack": 5} # Agregamos nombres y sus valores asignados
print (diccionario)

# Otra forma de crear un diccionario

dic2 = {} # se crea el diccionario vacio

# Se agrega 1 por una el string y su valor asosiado

dic2["gabriel"] = 24 
dic2["palmy"] = 52
dic2["juan"] = 52
dic2["jack"] = 5

print (dic2)

# Podemos hacer que el programa imprima el valor asociado indicandole el string

print (dic2["jack"]) # Se espera que se imprima 5 que es el valor asociado  a jack.
