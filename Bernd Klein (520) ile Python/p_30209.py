# coding:iso-8859-9 T�rk�e
# p_30209.py: Dizi kopyalar�ndaki de�i�iklik python'da asl�n� de�i�tirmezken, numpy.array'de de�i�tirir �rne�i.

import numpy as np

liste1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ("Python liste1:", liste1)
liste2 = liste1[2:6]
liste2[0] = 22
liste2[1] = 23
print ("Python liste1 dilimlerindeki de�i�iklik orijinali DE���T�RMEZ:", liste1)

dizi1 = np.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print ("\nNumpy dizi1:", dizi1)
dizi2 = dizi1[2:6]
dizi2[0] = 22
dizi2[1] = 23
print ("Numpy dizi1 dilimlerindeki de�i�iklik orijinali de DE���T�R�R:", dizi1)
print ("Numpy dizi1 ve dizi2 ayn� haf�zay� m� kullan�yor?", np.may_share_memory (dizi1, dizi2) )

A = np.arange (12)
print ("\nDizi A:", A)
B = A.reshape (3, 4)
print ("Dizi B=A.reshape(3,4):\n", B, sep="")
A[0] = 42
print ("A[0]=42 sonras� dizi B:\n", B, sep="")
print ("Numpy dizi A ve dizi B ayn� haf�zay� m� kullan�yor?", np.may_share_memory (A, B) )



"""��kt�:
>python p_30209.py
Python liste1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Python liste1 dilimlerindeki de�i�iklik orijinali DE���T�RMEZ: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Numpy dizi1: [0 1 2 3 4 5 6 7 8 9]
Numpy dizi1 dilimlerindeki de�i�iklik orijinali de DE���T�R�R: [ 0  1 22 23  4  5  6  7  8  9]
Numpy dizi1 ve dizi2 ayn� haf�zay� m� kullan�yor? True

Dizi A: [ 0  1  2  3  4  5  6  7  8  9 10 11]
Dizi B=A.reshape(3,4):
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
A[0]=42 sonras� dizi B:
[[42  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
Numpy dizi A ve dizi B ayn� haf�zay� m� kullan�yor? True
"""