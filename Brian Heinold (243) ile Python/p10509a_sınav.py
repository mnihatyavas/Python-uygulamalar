# coding:iso-8859-9 T�rk�e

from random import randint
from math import *

saya�1=saya�2=saya�3=0
kere = randint (1,1000)
for i in range (1, kere):
    if i**2 % 10 == 1: saya�1 +=1
    elif i**2 % 10 == 4: saya�2 +=1
    elif i**2 % 10 == 9: saya�3 +=1
print ("1->", kere, "karesi say�lardan sonu 1'le bitenler:", saya�1, ", 4'le bitenler:", saya�2, "ve 9'la bitenlerin toplam�:", saya�3)
print()
saya�=0
for i in range (1, kere): saya� = saya� + (i**(-1))
print (saya�, "- ln(", kere, ") =", saya� - log (kere))
print()
toplam=0
for i in range (1, 2001):
    if i % 2 == 0: toplam+=-i
    else: toplam+=i
# Ger�ekte 1000 kere -1'i toplar...
print ("[1->2000] +tekler ve -�iftler toplam�:", toplam)
print()
"""
for i in range (3, 10000):
    toplam=1
    for j in range (2, i):
        if (i//j)*j == i: toplam+=j
    if toplam == i: print (i, "bir ideal say�d�r")
��kt�:
6 bir ideal say�d�r
28 bir ideal say�d�r
496 bir ideal say�d�r
8128 bir ideal say�d�r
"""
print()
bayrak=0
for j in range (2, kere):
    if (kere//j)*j==kere and trunc (sqrt (j))**2 == j: bayrak=1; break
if not bayrak: print (kere, "say�s�n�n b�lenleri kare-muaf't�r")
else: print (kere, "say�s�n�n", j, "b�leni ideal-kare'dir")
print()
