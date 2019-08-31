# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:06:30 2019

@author: rique
"""
# En esta parte se ve como cambiar el tipo de lineas en un gráfico
from matplotlib import pyplot as plt #Esto nos permitira poder graficar los datos
# Creaccion de variables
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [38496, 42000, 46752, 49320, 53200, 56000, 64928, 67317, 68748, 73752, 74664]
plt.plot(x, y, 'k--' , label='Peru') # se deja la linea asociada a esta variable como linea punteada

#Si desearamos agregar otra curva al sistema
y2 = [48496, 52000, 56752, 59320, 63200, 66000, 74928, 77317, 78748, 83752, 84664]
plt.plot(x, y2, 'b', label='Chile') 
# Al grafico anterior le faltanan tanto los nombres de los ejes junto con el titulo
plt.xlabel('Edad') #se agrega el eje x
plt.ylabel('Salario medio en USD por edad') # se agrega el eje y
plt.title('Salario medio por edad') #se agrega el titulo
plt.legend(['Peru', 'Chile'])
plt.show()