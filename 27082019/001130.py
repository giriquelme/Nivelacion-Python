# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:53:49 2019

@author: rique
"""

# Para hacer operaciones con matrices
m1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
m2 = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])

print (m1 , m2) # muestro las 2 matrices
print (m1 + m2) #se crea una matriz que contiene a ambas matrices anteriores

print (m1 + 50) # Le suma 50 a cada valor de la matriz
m = m1 * m2
print (m) 

#Finalmente se utilizara un coando que permite ordenar la matriz
m4 = np.array([5, 2, 4, 8, 9, 6])
print (np.sort(m4)) #Este comando ordena la matriz en orden de menor a mayor