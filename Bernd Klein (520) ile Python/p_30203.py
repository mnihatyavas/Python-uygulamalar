# coding:iso-8859-9 T�rk�e
# p_30203.py: numpy.arange kapsam� ve numpy.array dizisi �zellikleri �rne�i.

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

tamsay�Dizi = np.array ([1, 1, 2, 3, 5, 8, 13, 21, -1, 0])
kayanDizi = np.array ([3.4, 6.9, 99.8, 12.8, -1, 0])

print ("\ntamsay�Dizi:", tamsay�Dizi)
print ("kayanDizi:", kayanDizi)
print ("tamsay�Dizi.dtype:", tamsay�Dizi.dtype)
print ("kayanDizi.dtype:", kayanDizi.dtype)
print ("np.ndim(tamsay�Dizi):", np.ndim (tamsay�Dizi) )
print ("np.ndim(kayanDizi):", np.ndim (kayanDizi) )



"""��kt�:
>python p_30203.py
np.arange (20): [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
type(a1): <class 'numpy.ndarray'>
np.ndim(a1): 1

np.array (20): 20
type(a2): <class 'numpy.ndarray'>
np.ndim(a2): 0

tamsay�Dizi: [ 1  1  2  3  5  8 13 21 -1  0]
kayanDizi: [ 3.4  6.9 99.8 12.8 -1.   0. ]
tamsay�Dizi.dtype: int32
kayanDizi.dtype: float64
np.ndim(tamsay�Dizi): 1
np.ndim(kayanDizi): 1
"""