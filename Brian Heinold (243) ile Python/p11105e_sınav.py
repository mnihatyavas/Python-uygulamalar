# coding:iso-8859-9 Türkçe

print ("[0->100] gelişigüzel sayılı 15x10 matris listesi:\n", "-"*49, sep="")
from random import randint
L = [[randint (0,100) for j in range (15)] for i in range (10)]
from pprint import pprint
pprint (L)

print ("\nÖnceki matrisin artan sıralı 1x150 listesi:\n", "-"*43, sep="")
L1 = []
for i in range (len (L)):
    for j in range (len (L[0])):
        L1 = L1 + [L[i][j]]
L1.sort ()
print (L1)

S = {}
sayaç = 1
for i in range (len (L1)-1):
    if L1[i] == L1[i+1]:
        sayaç +=1
    else:
        S [L1[i] ] = sayaç
        sayaç = 1
S [L1[i+1] ] = sayaç
print ("\nÖnceki listenin her elemanının tekrarını içeren ", len (S), " ebatlı sözlük:\n", "-"*65, sep="")
pprint (S)

L = []
toplam = 0
for k in S.items():
    L = L + [(k[1], k[0])]
    toplam +=k[1]
L.sort()
print ("\nÖnceki sözlüğün artan tekrara göre sıralı listesi:\n", "-"*50, sep="")
pprint (L)
print ("-"*24, "\nTekrarların toplamı: ", toplam, sep="")
