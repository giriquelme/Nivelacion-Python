# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:08:43 2019

@author: rique
"""

import numpy as np
a = np.arange(25).reshape(5, 5) #se crea una matriz de 5x5
print (a)
np.nan % 6
print (np.sum([1, np.nan, 9]))
a = np.array([1, 2, 3])
print (np.sum(a))
print (a.sum(axis=0) )

b = np.arange(15).reshape(3, 5)
print (b.shape)

print (b.mean(axis=0).shape)

print (b.mean(axis=1).shape)
channel_means = b.mean(axis=1)
print (channel_means)
print (winds.shape)