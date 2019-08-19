# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:36:40 2019

@author: rique
"""

#Calculo de Tasa Metabólica Basal
#el codigo desarrollado permite el calculo de calorias diarias a consumir por una persona, ingresando una serie de datos.

#Se pide al usuario que ingrese sus características fisicas
p = input("ingrese su peso en kg:")
h = input("inrese altura en cm:")
e = input("ingrese su edad:")
s = input("ingrese su genero, 1 si es hombre y 2 si es mujer:") #permite separar según genero

#Luego de ingresar sus datos, las siguientes expresiones permiten calcular su TMB
if s == 1: #calculo de TMB para hombres
    print "su tasa metabólica basal es:"
    print 10*p +  6.25*h - 5*e + 5
else: #Calculo de TMB para mujeres
    print "su tasa metabolica es:"
    print 10*p +  6.25*h - 5*e - 161
    