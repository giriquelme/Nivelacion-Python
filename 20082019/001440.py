# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:43:46 2019

@author: rique
"""

# Tarea propuesta: convertir valores en millas a km

# km = 1.6 * millas
# Se defune la funcion conversion con la relacion propuesta
def conversion(a):
    return a*1.6
a = input("millas:") # Se pide al usuario agrgar el valor que desea convertir

print conversion(a), "km" # Arroja el resultado en km