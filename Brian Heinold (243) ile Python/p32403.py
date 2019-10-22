# coding:iso-8859-9 Türkçe

from itertools import *

L = [0, 0, 1, 1, 1, 2, 0, 4, 4, 4, 4, 4, 2, 13, 13]

print ("Ardışık aynılık grup listesi:\n", "-"*29, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', list (grup) )

L.sort()
print ("\nSıralı ardışık aynılık grup listesi:\n", "-"*36, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', list (grup) )

print ("\nSıralı ardışık aynılık grup eleman sayısı:\n", "-"*42, sep="")
for anahtar, grup in groupby (L): print (anahtar, ':', len (list (grup)) )
#-----------------------------------------------------------------------------------------

dizge = "Bu groupby fonksiyonunun tercihli argüman içeren bir örneğidir."
L = dizge.split()

L.sort (key=len)
print ("\nKelime uzunluğu ardışık aynılık grup listesi:\n", "-"*45, sep="")
for anahtar, grup in groupby (L, len): print (anahtar, ':', list (grup) )
#-----------------------------------------------------------------------------------------

from random import randint

L = [randint(1,6) for i in range (randint (1000,10000))]
print ("\n", len (L), " zar atışındaki ardışık azami tesadüfi 1->6'lar adedi:\n", "-"*58, sep="")
for i in range (1, 7): print (i, "arka arkaya azami:", max ([len (list (grup)) for anh, grup in groupby (L) if anh == i]), "kere geldi" )
#-----------------------------------------------------------------------------------------
def yortu (y): return randint (1,30)

L = [yortu (Y) for Y in range (1900,2101)]
L.sort()
print ("\n1900->2100 arası yıllık uydurma paskalya yortu gün sayılarının histogramı:\n", "-"*74, sep="")
for anh, grup in groupby (L): print (anh, ":", "*" * (len (list (grup))) )
