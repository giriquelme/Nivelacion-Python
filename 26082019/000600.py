# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:23:04 2019

@author: rique
"""

# Si deseamos imprimir el string con su valor asociado, podemos incorporar un for

dic = {"gabriel": 24, "palmy": 52, "juan": 52, "jack": 5}

for nombre, edad in dic.items(): # permite que separemos los items del diccionario 
    print ("nombre:", nombre)
    print ("edad:", edad)
    print (" ") # nos sirve ara separar las variables y valores del diccionario
 