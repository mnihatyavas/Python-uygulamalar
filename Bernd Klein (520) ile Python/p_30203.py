# coding:iso-8859-9 Türkçe
# p_30203.py: numpy.arange kapsamı ve numpy.array dizisi özellikleri örneği.

import numpy as np

a1 = np.arange (20)
a2 = np.array (20)

print ("np.arange (20):", a1)
print ("type(a1):", type (a1) )
print ("np.ndim(a1):", np.ndim (a1) )

print ("\nnp.array (20):", a2)
print ("type(a2):", type (a2) )
print ("np.ndim(a2):", np.ndim (a2) )
#-------------------------------------------------------------------------------------------

tamsayıDizi = np.array ([1, 1, 2, 3, 5, 8, 13, 21, -1, 0])
kayanDizi = np.array ([3.4, 6.9, 99.8, 12.8, -1, 0])

print ("\ntamsayıDizi:", tamsayıDizi)
print ("kayanDizi:", kayanDizi)
print ("tamsayıDizi.dtype:", tamsayıDizi.dtype)
print ("kayanDizi.dtype:", kayanDizi.dtype)
print ("np.ndim(tamsayıDizi):", np.ndim (tamsayıDizi) )
print ("np.ndim(kayanDizi):", np.ndim (kayanDizi) )



"""Çıktı:
>python p_30203.py
np.arange (20): [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
type(a1): <class 'numpy.ndarray'>
np.ndim(a1): 1

np.array (20): 20
type(a2): <class 'numpy.ndarray'>
np.ndim(a2): 0

tamsayıDizi: [ 1  1  2  3  5  8 13 21 -1  0]
kayanDizi: [ 3.4  6.9 99.8 12.8 -1.   0. ]
tamsayıDizi.dtype: int32
kayanDizi.dtype: float64
np.ndim(tamsayıDizi): 1
np.ndim(kayanDizi): 1
"""