# coding:iso-8859-9 T�rk�e

from itertools import *
from random import randint

L1 = [randint (0,100) for i in range (randint (1,20))]
L2 = [randint (0,100) for i in range (randint (1,20))]
L3 = [randint (0,100) for i in range (randint (1,20))]

# 3 listeyi arka arkaya listeleyelim...
print ("3 ayr� listenin tek-tek d�k�m�:\n", L1, "\n", L2, "\n", L3, sep="")

print ("\n3 ayr� liste elemanlar�n�n 'chain' ile tek listesizmi�cesine d�k�m�:")
for i in chain (L1, L2, L3): print (i, end=" ")
#-------------------------------------------------------------------------------------------

print("\n\npprint ile 2 boyutlu 3 sat�r, x s�tunlu liste d�k�m�:")
L = [[randint (0,100) for i in range (randint (1,20))], [randint (0,100) for i in range (randint (1,20))], [randint (0,100) for i in range (randint (1,20))]]

from pprint import pprint
pprint (L)

print("\nAyn� liste  elemanlar�n�n chain ile tek boyutluymu�cas�na d�k�m�:")
print (list (chain (*tuple (L))) )
#--------------------------------------------------------------------------------------------

print()
for x in count(): # count()=range(sonsuz), count(5)=range(5,sonsuz) farzedilir...
    devam = input ("Devam edelim mi [e/h]: ").lower()
    if devam == 'h': break
    print ("   [0->4] devri-daimi:", x)
#--------------------------------------------------------------------------------------------

print()
for x in cycle (range (5)): # cycle ile d�ng� 0->4 ard���kl���nda sonsuzca yinelenir...
    devam = input ("Devam edelim mi [e/h]: ").lower()
    if devam == 'h': break
    print ("   [0->4] devri-daimi:", x)
