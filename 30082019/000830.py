# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:55:03 2019

@author: rique
"""

from matplotlib import pyplot as plt #Esto nos permitira poder graficar los datos
# Creaccion de variables
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [38496, 42000, 46752, 49320, 53200, 56000, 64928, 67317, 68748, 73752, 74664]
plt.plot(x, y)

# Al grafico anterior le faltanan tanto los nombres de los ejes junto con el titulo
plt.xlabel('Edad') #se agrega el eje x
plt.ylabel('Salario medio en USD por edad') # se agrega el eje y
plt.title('Salario medio por edad') #se agrega el titulo
plt.show()
