# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:14:09 2019

@author: rique
"""


from matplotlib import pyplot as plt #Esto nos permitira poder graficar los datos
# Creaccion de variables
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [38496, 42000, 46752, 49320, 53200, 56000, 64928, 67317, 68748, 73752, 74664]
plt.plot(x, y, color='k', linestyle='--', marker='.' , label='Peru') # se deja la linea asociada a esta variable como linea punteada
y2 = [48496, 52000, 56752, 59320, 63200, 66000, 74928, 77317, 78748, 83752, 84664]
plt.plot(x, y2, color='b',marker='.', label='Chile') 
# En esta parte se hacen modificaciones a las lineas egragandoles distintas propiedades como el color e indicar los puntos
plt.xlabel('Edad') 
plt.ylabel('Salario medio en USD por edad') 
plt.legend(['Peru', 'Chile'])
plt.title('Salario medio por edad')
plt.show()

# Se puede apreciar las diferencias ene los colores de los graficos al cambiar el color
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [38496, 42000, 46752, 49320, 53200, 56000, 64928, 67317, 68748, 73752, 74664]
plt.plot(x, y, color='#444444', linestyle='--', marker='.' , label='Peru') # se deja la linea asociada a esta variable como linea punteada
y2 = [48496, 52000, 56752, 59320, 63200, 66000, 74928, 77317, 78748, 83752, 84664]
plt.plot(x, y2, color='#5a7d9a',marker='.', label='Chile') 
# En esta parte se hacen modificaciones a las lineas egragandoles distintas propiedades como el color e indicar los puntos
plt.xlabel('Edad') 
plt.ylabel('Salario medio en USD por edad') 
plt.legend(['Peru', 'Chile'])
plt.title('Salario medio por edad')
plt.show()