# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:27:28 2019

@author: rique
"""

import numpy as np
a = np.array([10, 1, 20])
b = np.array([2, 3, 20])
print (a > b) # se comparan los valores de ambas matrices en igual posicon
print (np.nonzero(a > b))
print (a, b)

subset = a[[0, 2]]
print (subset)
print (a.flags.owndata)
print (subset.flags.owndata)

print (a is subset)