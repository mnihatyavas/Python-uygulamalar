# coding:iso-8859-9 Türkçe
# p_30209.py: Dizi kopyalarındaki değişiklik python'da aslını değiştirmezken, numpy.array'de değiştirir örneği.

import numpy as np

liste1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ("Python liste1:", liste1)
liste2 = liste1[2:6]
liste2[0] = 22
liste2[1] = 23
print ("Python liste1 dilimlerindeki değişiklik orijinali DEĞİŞTİRMEZ:", liste1)

dizi1 = np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print ("\nNumpy dizi1:", dizi1)
dizi2 = dizi1[2:6]
dizi2[0] = 22
dizi2[1] = 23
print ("Numpy dizi1 dilimlerindeki değişiklik orijinali de DEĞİŞTİRİR:", dizi1)
print ("Numpy dizi1 ve dizi2 aynı hafızayı mı kullanıyor?", np.may_share_memory (dizi1, dizi2) )

A = np.arange (12)
print ("\nDizi A:", A)
B = A.reshape (3, 4)
print ("Dizi B=A.reshape(3,4):\n", B, sep="")
A[0] = 42
print ("A[0]=42 sonrası dizi B:\n", B, sep="")
print ("Numpy dizi A ve dizi B aynı hafızayı mı kullanıyor?", np.may_share_memory (A, B) )



"""Çıktı:
>python p_30209.py
Python liste1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Python liste1 dilimlerindeki değişiklik orijinali DEĞİŞTİRMEZ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Numpy dizi1: [0 1 2 3 4 5 6 7 8 9]
Numpy dizi1 dilimlerindeki değişiklik orijinali de DEĞİŞTİRİR: [ 0  1 22 23  4  5  6  7  8  9]
Numpy dizi1 ve dizi2 aynı hafızayı mı kullanıyor? True

Dizi A: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Dizi B=A.reshape(3,4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
A[0]=42 sonrası dizi B:
[[42  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Numpy dizi A ve dizi B aynı hafızayı mı kullanıyor? True
"""