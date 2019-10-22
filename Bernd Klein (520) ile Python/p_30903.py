# coding:iso-8859-9 T�rk�e
# p_30903.py: Numpy dizi elemanlar�n� s�zge�leme ve de�i�tirme �rne�i.

import numpy as np

A = np.array ([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])

b�leme3 = A [A % 3 != 0]
print ("A dizisi:", A)
print ("A dizisinin 3'le b�l�nemeyen elemanlar�:", b�leme3)


b�l5 = A [A % 5 == 0]
print ("A dizisinin 5'le b�l�nebilen elemanlar�:", b�l5)

b�l3ve5 = A [ (A % 3 == 0) & (A % 5 == 0)]
print ("A dizisinin 3 ve 5'le b�l�nebilen elemanlar�:", b�l3ve5)

b�l3isePi = A.astype (np.float)
b�l3isePi [b�l3isePi % 3 == 0] = 3.14
print ("3'le b�l�nebilenlerinin pi=3.14 float'la�t�r�ld��� A dizisi:\n", b�l3isePi)



"""��kt�:
>python p_30903.py
A dizisi: [  3   4   6  10  24  89  45  43  46  99 100]
A dizisinin 3'le b�l�nemeyen elemanlar�: [  4  10  89  43  46 100]
A dizisinin 5'le b�l�nebilen elemanlar�: [ 10  45 100]
A dizisinin 3 ve 5'le b�l�nebilen elemanlar�: [45]
3'le b�l�nebilenlerinin pi=3.14 float'la�t�r�ld��� A dizisi:
 [  3.14   4.     3.14  10.     3.14  89.     3.14  43.    46.     3.14 100.  ]

"""