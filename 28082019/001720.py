# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:11:27 2019

@author: rique
"""

import numpy as np
#data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",",skiprows=1) #Este comando no funciona pues no tengo un archivo de texto con el nombre data
#print (data)
a = np.arange(20) #se crea una mtraiz desde el numero 0 al 20
print (a)

np.random.shuffle(a) #Cambia el orden de los números en forma aleatoria
print (a)

print (np.random.choice(a)) #se escoje un numero aletarorio de la matriz



