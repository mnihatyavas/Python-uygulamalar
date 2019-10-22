# coding:iso-8859-9 Türkçe
# p_30904.py: Numpy dizi elemanlarının sıfırsız veya True olanları örneği.

import numpy as np

a = np.array ([
    [0, 2, 3, 0, 1],
    [1, 0, 0, 7, 0],
    [5, 0, 0, 1, 0] ])

print ("a dizisi:\n", a, sep="")

print ("\na dizisindeki sıfır olmayan elemanların YATAY satır ve sütun endeksleri:\n", a.nonzero(), sep="")
print ("\na dizisindeki sıfır olmayan elemanların DİKEY satır ve sütun endeksleri:\n", np.transpose (a.nonzero() ), sep="")

print ("\na dizisindeki sıfır olmayan elemanların listesi:\n", a[a.nonzero()], sep="")
print ("-"*70)
#----------------------------------------------------------------------------------------------------------

B = np.array ([
    [42, 56, 89, 65],
    [99, 88, 42, 12],
    [55, 42, 17, 18] ])

print ("\nB dizisi:\n", B, sep="")
print ("\n(B >= 42) kriterli True/False dizisi:\n", (B >= 42), sep="")
print ("\n(B >= 42) kriterli YATAY True dizi endeksleri:\n", np.nonzero (B >= 42), sep="")
print ("\n(B >= 42) kriterli DİKEY True dizi endeksleri:\n", np.transpose ((B >= 42).nonzero()), sep="")
print ("\n(B >= 42) kriterli dizinin True elemanları listesi:\n", (B >= 42)[(B >= 42).nonzero()], sep="")



"""Çıktı:
>python p_30904.py
a dizisi:
[[0 2 3 0 1]
 [1 0 0 7 0]
 [5 0 0 1 0]]

a dizisindeki sıfır olmayan elemanların YATAY satır ve sütun endeksleri:
(array([0, 0, 0, 1, 1, 2, 2], dtype=int32), array([1, 2, 4, 0, 3, 0, 3], dtype=int32))

a dizisindeki sıfır olmayan elemanların DİKEY satır ve sütun endeksleri:
[[0 1]
 [0 2]
 [0 4]
 [1 0]
 [1 3]
 [2 0]
 [2 3]]

a dizisindeki sıfır olmayan elemanların listesi:
[2 3 1 1 7 5 1]
----------------------------------------------------------------------

B dizisi:
[[42 56 89 65]
 [99 88 42 12]
 [55 42 17 18]]

(B >= 42) kriterli True/False dizisi:
[[ True  True  True  True]
 [ True  True  True False]
 [ True  True False False]]

(B >= 42) kriterli YATAY True dizi endeksleri:
(array([0, 0, 0, 0, 1, 1, 1, 2, 2], dtype=int32), array([0, 1, 2, 3, 0, 1, 2, 0, 1], dtype=int32))

(B >= 42) kriterli DİKEY True dizi endeksleri:
[[0 0]
 [0 1]
 [0 2]
 [0 3]
 [1 0]
 [1 1]
 [1 2]
 [2 0]
 [2 1]]

(B >= 42) kriterli dizinin True elemanları listesi:
[ True  True  True  True  True  True  True  True  True]
"""