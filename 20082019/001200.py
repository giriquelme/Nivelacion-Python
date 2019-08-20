# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:30:18 2019

@author: rique
"""
# Para este item utilizaremos un codigo ya escrito, el cual se adecuo para trabajarlo como una funcion.
# Se pide al usuario que ingrese sus características fisicas
p = input("ingrese su peso en kg:")
h = input("inrese altura en cm:")
e = input("ingrese su edad:")
s = input("ingrese su genero, 1 si es hombre y 2 si es mujer:") #permite separar según genero

# Se define la funcion TMB como una funcion de 4 variables
def TMB(p, h, e, s):
    if s==1: # Se agrega la condicion para trabajar de una u otra forma
        return 10*p +  6.25*h - 5*e + 5
    else:
        return 10*p +  6.25*h - 5*e - 161
a = TMB(p, h, e, s) # Se le asigna a la variable el resultado de la función para luego ser impresa
print "Su tasa metabolica basal es:" 
print (a)
