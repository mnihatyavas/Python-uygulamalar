# coding:iso-8859-9 T�rk�e

from itertools import *

L = [0, 0, 1, 1, 1, 2, 0, 4, 4, 4, 4, 4, 2, 13, 13]

print ("Ard���k ayn�l�k grup listesi:\n", "-"*29, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', list (grup) )

L.sort()
print ("\nS�ral� ard���k ayn�l�k grup listesi:\n", "-"*36, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', list (grup) )

print ("\nS�ral� ard���k ayn�l�k grup eleman say�s�:\n", "-"*42, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', len (list (grup)) )
#-----------------------------------------------------------------------------------------

dizge = "Bu groupby fonksiyonunun tercihli arg�man i�eren bir �rne�idir."
L = dizge.split()

L.sort (key=len)
print ("\nKelime uzunlu�u ard���k ayn�l�k grup listesi:\n", "-"*45, sep="")
for anahtar, grup in groupby (L, len): print (anahtar, ':', list (grup) )
#-----------------------------------------------------------------------------------------

from random import randint

L = [randint(1,6) for i in range (randint (1000,10000))]
print ("\n", len (L), " zar at���ndaki ard���k azami tesad�fi 1->6'lar adedi:\n", "-"*58, sep="")
for i in range (1, 7): print (i, "arka arkaya azami:", max ([len (list (grup)) for anh, grup in groupby (L) if anh == i]), "kere geldi" )
#-----------------------------------------------------------------------------------------
def yortu (y): return randint (1,30)

L = [yortu (Y) for Y in range (1900,2101)]
L.sort()
print ("\n1900->2100 aras� y�ll�k uydurma paskalya yortu g�n say�lar�n�n histogram�:\n", "-"*74, sep="")
for anh, grup in groupby (L): print (anh, ":", "*" * (len (list (grup))) )
