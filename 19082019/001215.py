# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:04:09 2019

@author: rique
"""
#Codigo basico, mediante el comando if permite establecer la relación entre dos números

a = 10 #asignamos el valor de 10 a la variable a
b = 8 #asignamos el valor de 8 a la variable b

#Para comparar dichas variables, se utiliza el comando "if" el cual establece una condición.
#Si no se cumple la condición, se pasa a la siguiente condición, al cumplirse una de las impuestas el programa arroja el "print" relacionado a esta
if a < b:
    print ("a es menor que b")
elif a == b:
    print ("a es igual a b")
else:
    print ("a es mayor que b")