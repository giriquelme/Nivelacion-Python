# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:28:56 2019

@author: rique
"""
# Como definir una lista
# Para definir una lista se utilizan lod corchetes.

a = [1, 2, 3, 4, 5]
print (a)

# Para agregar elementos a la lista utilizamos en comando append.
a.append(6)
print (a)

# Para agregar una palabra se agrega como string a la lista
a.append("numeros") 
print (a)

# Para agregar una lista dentro de otra
# Podemos utilizar el comando pop para ir eliminando los ultimos elementos agregados
a.append([7, 8, 9])
print (a)

# Para eliminar elementos en una lista
a.pop()
print (a)

a.pop()
print (a)
# ______________________________________________________________________________________

# Para recuperar un elento de una lista
print (a[0])

# Para cambiar el numero de una lista, falta con definir al numero que ocupa una posicion un nuevo valor

a[2] = 50
print (a)
