# coding:iso-8859-9 Türkçe

from itertools import *
from random import randint

L1 = [randint (0,100) for i in range (randint (1,20))]
L2 = [randint (0,100) for i in range (randint (1,20))]
L3 = [randint (0,100) for i in range (randint (1,20))]

# 3 listeyi arka arkaya listeleyelim...
print ("3 ayrı listenin tek-tek dökümü:\n", L1, "\n", L2, "\n", L3, sep="")

print ("\n3 ayrı liste elemanlarının 'chain' ile tek listesizmişcesine dökümü:")
for i in chain (L1, L2, L3): print (i, end=" ")
#-------------------------------------------------------------------------------------------

print("\n\npprint ile 2 boyutlu 3 satır, x sütunlu liste dökümü:")
L = [[randint (0,100) for i in range (randint (1,20))], [randint (0,100) for i in range (randint (1,20))], [randint (0,100) for i in range (randint (1,20))]]

from pprint import pprint
pprint (L)

print("\nAynı liste  elemanlarının chain ile tek boyutluymuşcasına dökümü:")
print (list (chain (*tuple (L))) )
#--------------------------------------------------------------------------------------------

print()
for x in count(): # count()=range(sonsuz), count(5)=range(5,sonsuz) farzedilir...
    devam = input ("Devam edelim mi [e/h]: ").lower()
    if devam == 'h': break
    print ("   [0->4] devri-daimi:", x)
#--------------------------------------------------------------------------------------------

print()
for x in cycle (range (5)): # cycle ile döngü 0->4 ardışıklığında sonsuzca yinelenir...
    devam = input ("Devam edelim mi [e/h]: ").lower()
    if devam == 'h': break
    print ("   [0->4] devri-daimi:", x)
