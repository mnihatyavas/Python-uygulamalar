#coding:iso-8859-9 T�rk�e

# 5 haneli tesad�fi [2->20] rakam �retip, paralel endeks de�erleri toplam�n�n tamsay� ortalamas�ndan yeni bir 5 haneli rakam t�retelim...
from random import randint
L=[randint (10000,99999) for i in range (randint(2,20))]
dizge = ""
for n in L: dizge = dizge + str (n) + " "
L = dizge.split()
print ("Tesad�fi 5 haneli toplam", len(L), "adet rakamlar�m�z:", L)

n = 0
for i in range (5):
    toplam = 0
    for j in range (len(L)):
        kelime = L[j]
        toplam += int(kelime[i])
    n += (toplam // len(L)) * (10**(4-i))
print()
print (len(L), "adet ve 5 haneli paralel herbir hanenin tamsay� ortalamas�ndan t�retilen yeni rakam�m�z:", n)
