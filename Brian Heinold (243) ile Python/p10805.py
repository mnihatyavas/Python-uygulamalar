# coding:iso-8859-9 Türkçe

from random import randint
L = [randint (1, 100) for i in range (50)]
print ("50 adet [1->100] tesadüfi tamsayı listesi:", L)
print ("\nL**2:", [i**2 for i in L])
print ("\nToplam eleman sayısı:", len (L), "; 50'den büyük eleman sayısı:", len ([i for i in L if i > 50]))

L = [randint (1, 100) for i in range (10000)]
print ("\n10000 adet [1->100] tesadüfi sayıda kaç 1, kaç 2.. kaç 100 var?\n",
    [[i, ":", L.count (i)] for i in range (1, 101)])

from random import choice
alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
print ("\n1000 tesadüfi harf birleşiminden oluşan dizge:\n    ", "".join ([choice (alfabe) for i in range (1000)]))
L =[]
for i in range (50): L.append ([i, i+1, i+2])
print ("\nÜçlü 50 elemanlı liste:", L)
print ("\nÜçlü eleman değiştokuşlu liste:", [[z,y,x] for x,y,z in L])