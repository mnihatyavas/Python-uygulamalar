# coding:iso-8859-9 Türkçe
# p_30903.py: Numpy dizi elemanlarını süzgeçleme ve değiştirme örneği.

import numpy as np

A = np.array ([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])

böleme3 = A [A % 3 != 0]
print ("A dizisi:", A)
print ("A dizisinin 3'le bölünemeyen elemanları:", böleme3)


böl5 = A [A % 5 == 0]
print ("A dizisinin 5'le bölünebilen elemanları:", böl5)

böl3ve5 = A [ (A % 3 == 0) & (A % 5 == 0)]
print ("A dizisinin 3 ve 5'le bölünebilen elemanları:", böl3ve5)

böl3isePi = A.astype (np.float)
böl3isePi [böl3isePi % 3 == 0] = 3.14
print ("3'le bölünebilenlerinin pi=3.14 float'laştırıldığı A dizisi:\n", böl3isePi)



"""Çıktı:
>python p_30903.py
A dizisi: [  3   4   6  10  24  89  45  43  46  99 100]
A dizisinin 3'le bölünemeyen elemanları: [  4  10  89  43  46 100]
A dizisinin 5'le bölünebilen elemanları: [ 10  45 100]
A dizisinin 3 ve 5'le bölünebilen elemanları: [45]
3'le bölünebilenlerinin pi=3.14 float'laştırıldığı A dizisi:
 [  3.14   4.     3.14  10.     3.14  89.     3.14  43.    46.     3.14 100.  ]

"""