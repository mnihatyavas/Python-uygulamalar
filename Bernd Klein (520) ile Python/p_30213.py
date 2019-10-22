# coding:iso-8859-9 Türkçe
# p_30213.py: numpy.array'de kopyadaki değişikliğin aslında yansıması, satır ve/veya kolon tersten [::-1, ::-1] örneği.

import numpy as np

a = np.array ([3, 8, 12, 18, 7, 11, 30])
print ("Dizi a: ", a, "\nŞekli: ", a.shape, "\nBoyutu: ", np.ndim (a), sep="")

print ("\nÇiftli elemanları:", a[0::2])
print ("Tekli elemanları:", a[1::2])

print ("\nTersten dizi:", a[::-1])

b = a[1:len(a)-1]
b[0] = 200
print ("\nKopya a[1:len(a)-1] ve b[0]=200 dizisi: ", b, "\nOtomatik değişen a dizisi: ", a, sep="")
print ("-"*40)
#-------------------------------------------------------------------------------------------------

m = np.array ([ [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]] )
print ("Matris m:\n", m, "\nŞekli: ", m.shape, "\nBoyutu: ", np.ndim (m), sep="")

print ("\nSatır düzeni tersten:\n", m[::-1], sep="")

print ("\nSatır elemanları sırası (veya sütun düzeni) tersten:\n", m[::, ::-1], sep="")

print ("\nSatır düzeni ve satır elemanları sırası (veya sütun düzeni) tersten:\n", m[::-1, ::-1], sep="")
print ("-"*40)
#-------------------------------------------------------------------------------------------------

print ("\nİlk satır kesik:\n", m[1:], sep="")

print ("\nİlk sütun kesik:\n", m[:,1:], sep="")

print ("\nİlk satır ve ilk sütun kesik:\n", m[1:, 1:], sep="")



"""Çıktı:
>python p_30213.py
Dizi a: [ 3  8 12 18  7 11 30]
Şekli: (7,)
Boyutu: 1

Çiftli elemanları: [ 3 12  7 30]
Tekli elemanları: [ 8 18 11]

Tersten dizi: [30 11  7 18 12  8  3]

Kopya a[1:len(a)-1] ve b[0]=200 dizisi: [200  12  18   7  11]
Otomatik değişen a dizisi: [  3 200  12  18   7  11  30]
----------------------------------------
Matris m:
[[11 12 13 14]
 [21 22 23 24]
 [31 32 33 34]]
Şekli: (3, 4)
Boyutu: 2

Satır düzeni tersten:
[[31 32 33 34]
 [21 22 23 24]
 [11 12 13 14]]

Satır elemanları sırası (veya sütun düzeni) tersten:
[[14 13 12 11]
 [24 23 22 21]
 [34 33 32 31]]

Satır düzeni ve satır elemanları sırası (veya sütun düzeni) tersten:
[[34 33 32 31]
 [24 23 22 21]
 [14 13 12 11]]
----------------------------------------

İlk satır kesik:
[[21 22 23 24]
 [31 32 33 34]]

İlk sütun kesik:
[[12 13 14]
 [22 23 24]
 [32 33 34]]

İlk satır ve ilk sütun kesik:
[[22 23 24]
 [32 33 34]]
"""