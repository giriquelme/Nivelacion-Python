# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:52:31 2019

@author: rique
"""

#creacion de listas
a = [1, 2, 3, 4]
b = [10, 11, 12, 13]

print (a + b) # funciona como concadenacion, es decir, une la listas

output = []
for item1, item2 in zip(a, b): #Crea una nueva lista con las sumas de las componentes
    output.append(item1 + item2)
print (output)

e = list(range(1000))
print (e)

import numpy as np 
e_array = np.array(e)
print (e_array)
#print (%timeit np.sum(e_array)) Arroja un error a pesar de estar escrito tal cual el video
a = np.array([1, 2, 3, 4])
b = np.array([10, 11, 12, 13])
print (a ,b)
print (a + b)

print (a / b)
print (a.dtype) #indica el numero de bits (32)
print (a.ndim) # indica el numero de dimensiones que componen la lista
print (a.shape)  #relacione l numero de dimensiones con la cantidad de datos de la lista

tupla = (2, 4)
print (type(tupla)) #indica el tipo de variable que es
print (a * 10) #se multiplica a cada valor de la lista

#Numpy permite aplicar cuaquier operacion a las listas creadas
print (np.sin(a)) #Se calcula el seno a cada valo
print (np.exp(a))  