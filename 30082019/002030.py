# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:20:57 2019

@author: rique
"""
from matplotlib import pyplot as plt
print (plt.style.available) # Permite mostrar las caracteristicas de cada variable
x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
y = [38496, 42000, 46752, 49320, 53200, 56000, 64928, 67317, 68748, 73752, 74664]
plt.plot(x, y, color='#444444', linestyle='--', marker='.' , label='Peru') # se deja la linea asociada a esta variable como linea punteada
y2 = [48496, 52000, 56752, 59320, 63200, 66000, 74928, 77317, 78748, 83752, 84664]
plt.plot(x, y2, color='#5a7d9a',marker='.', label='Chile') 
y3 = [37496, 43000, 46852, 49220, 53300, 56300, 65928, 67417, 68745, 73752, 75664]
# Se agrega otra variable muy similar por lo cual en la imagen debiesen verse 3 lineas
plt.plot(x, y3, color='#5a7d9a',marker='.', label='Brasil') 
plt.xlabel('Edad') 
plt.ylabel('Salario medio en USD por edad') 
plt.grid() # Permite agregar una cuadricula al grafico
plt.legend(['Peru', 'Chile', 'Brasil'])
plt.title('Salario medio por edad')

plt.tight_layout()
plt.show()