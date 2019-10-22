# coding:iso-8859-9 T�rk�e

from random import randint
L = [randint (1, 100) for i in range (50)]
print ("50 adet [1->100] tesad�fi tamsay� listesi:", L)
print ("\nL**2:", [i**2 for i in L])
print ("\nToplam eleman say�s�:", len (L), "; 50'den b�y�k eleman say�s�:", len ([i for i in L if i > 50]))

L = [randint (1, 100) for i in range (10000)]
print ("\n10000 adet [1->100] tesad�fi say�da ka� 1, ka� 2.. ka� 100 var?\n",
    [[i, ":", L.count (i)] for i in range (1, 101)])

from random import choice
alfabe = 'abc�defg�h�ijklmno�prs�tu�vyz'
print ("\n1000 tesad�fi harf birle�iminden olu�an dizge:\n    ", "".join ([choice (alfabe) for i in range (1000)]))
L =[]
for i in range (50): L.append ([i, i+1, i+2])
print ("\n��l� 50 elemanl� liste:", L)
print ("\n��l� eleman de�i�toku�lu liste:", [[z,y,x] for x,y,z in L])