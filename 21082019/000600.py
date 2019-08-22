# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:37:39 2019

@author: rique
"""

# Cambio de orden en una lista

a = ["industrial", "civil", "ambiental", "electrico"]
print (a)
# Para cambar un valor de la lista a una variable temporal ocupamos el comando temp

temp = a[1]

# Decimos que el valor a[1] lo cambiaremos por l valor de a[3]
a[1] = a[3]
a[3] = temp # Esto permite dejar el valor como un valor temporal
print (a)

# Otra forma de intercambiar lo numeros e hacerlo de forma directa
a[1],  a[3] = a[3], a[1]
print (a)