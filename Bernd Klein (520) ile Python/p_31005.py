# coding:iso-8859-9 Türkçe
# p_31005.py: Numpy 3 boyutlu cross/çapraz vektörel çarpım örneği.

import numpy as np

x = np.array ([0, 0, 1])
y = np.array ([0, 1, 0])

print ("[0,0,1] ile [0,1,0] cross/çapraz çarpımı:", np.cross (x, y) )
print ("[0,1,0] ile [0,0,1] çapraz çarpımı:", np.cross (y, x) )

print ("\n[0,0,2] ile (0,3,0) cross/çapraz çarpımı:", np.cross ([0,0,2], (0,3,0)) )
print ("(0,3,0) ile [0,0,2] çapraz çarpımı:", np.cross ((0,3,0), [0,0,2]) )

print ("\n(0,1,2) ile (1,3,0) cross/çapraz çarpımı:", np.cross ((0,1,2), (1,3,0)) )
print ("(1,3,0) ile (0,1,2) çapraz çarpımı:", np.cross ((1,3,0), (0,1,2)) )



"""Çıktı:
>python p_31005.py
[0,0,1] ile [0,1,0] cross/çapraz çarpımı: [-1  0  0]
[0,1,0] ile [0,0,1] çapraz çarpımı: [1 0 0]

[0,0,2] ile (0,3,0) cross/çapraz çarpımı: [-6  0  0]
(0,3,0) ile [0,0,2] çapraz çarpımı: [6 0 0]

(0,1,2) ile (1,3,0) cross/çapraz çarpımı: [-6  2 -1]
(1,3,0) ile (0,1,2) çapraz çarpımı: [ 6 -2  1]
"""