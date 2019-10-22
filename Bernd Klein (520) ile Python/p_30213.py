# coding:iso-8859-9 T�rk�e
# p_30213.py: numpy.array'de kopyadaki de�i�ikli�in asl�nda yans�mas�, sat�r ve/veya kolon tersten [::-1, ::-1] �rne�i.

import numpy as np

a = np.array ([3, 8, 12, 18, 7, 11, 30])
print ("Dizi a: ", a, "\n�ekli: ", a.shape, "\nBoyutu: ", np.ndim (a), sep="")

print ("\n�iftli elemanlar�:", a[0::2])
print ("Tekli elemanlar�:", a[1::2])

print ("\nTersten dizi:", a[::-1])

b = a[1:len(a)-1]
b[0] = 200
print ("\nKopya a[1:len(a)-1] ve b[0]=200 dizisi: ", b, "\nOtomatik de�i�en a dizisi: ", a, sep="")
print ("-"*40)
#-------------------------------------------------------------------------------------------------

m = np.array ([ [11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]] )
print ("Matris m:\n", m, "\n�ekli: ", m.shape, "\nBoyutu: ", np.ndim (m), sep="")

print ("\nSat�r d�zeni tersten:\n", m[::-1], sep="")

print ("\nSat�r elemanlar� s�ras� (veya s�tun d�zeni) tersten:\n", m[::, ::-1], sep="")

print ("\nSat�r d�zeni ve sat�r elemanlar� s�ras� (veya s�tun d�zeni) tersten:\n", m[::-1, ::-1], sep="")
print ("-"*40)
#-------------------------------------------------------------------------------------------------

print ("\n�lk sat�r kesik:\n", m[1:], sep="")

print ("\n�lk s�tun kesik:\n", m[:,1:], sep="")

print ("\n�lk sat�r ve ilk s�tun kesik:\n", m[1:, 1:], sep="")



"""��kt�:
>python p_30213.py
Dizi a: [ 3  8 12 18  7 11 30]
�ekli: (7,)
Boyutu: 1

�iftli elemanlar�: [ 3 12  7 30]
Tekli elemanlar�: [ 8 18 11]

Tersten dizi: [30 11  7 18 12  8  3]

Kopya a[1:len(a)-1] ve b[0]=200 dizisi: [200  12  18   7  11]
Otomatik de�i�en a dizisi: [  3 200  12  18   7  11  30]
----------------------------------------
Matris m:
[[11 12 13 14]
 [21 22 23 24]
 [31 32 33 34]]
�ekli: (3, 4)
Boyutu: 2

Sat�r d�zeni tersten:
[[31 32 33 34]
 [21 22 23 24]
 [11 12 13 14]]

Sat�r elemanlar� s�ras� (veya s�tun d�zeni) tersten:
[[14 13 12 11]
 [24 23 22 21]
 [34 33 32 31]]

Sat�r d�zeni ve sat�r elemanlar� s�ras� (veya s�tun d�zeni) tersten:
[[34 33 32 31]
 [24 23 22 21]
 [14 13 12 11]]
----------------------------------------

�lk sat�r kesik:
[[21 22 23 24]
 [31 32 33 34]]

�lk s�tun kesik:
[[12 13 14]
 [22 23 24]
 [32 33 34]]

�lk sat�r ve ilk s�tun kesik:
[[22 23 24]
 [32 33 34]]
"""