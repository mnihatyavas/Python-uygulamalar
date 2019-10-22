# coding:iso-8859-9 Türkçe

from random import shuffle
L = [1 for i in range (12)] + [0 for i in range (24)]
shuffle (L)
from pprint import pprint
L1 = [[0 for j in range (6)] for i in range (6)]
i=j=0
for e in L:
    L1[i][j] = e
    if j < 5: j +=1
    else: j = 0; i +=1
print ("12 adet gelişigüzel 1'li ve kalan 24 adeti 0'lı [6x6] matrisi==>")
pprint (L1)
print ("\nSatır ve sütunlarda farklı 1->9 değerli [9x9] matrisi==>")
L1 = [[0 for j in range (9)] for i in range (9)]
L = [i+1 for i in range (9)]
for i in range (9):
    shuffle (L)
    for j in range (9): L1[i][j] = L[j]
pprint (L1)
