# coding:iso-8859-9 Türkçe

from random import randint
from math import *

sayaç1=sayaç2=sayaç3=0
kere = randint (1,1000)
for i in range (1, kere):
    if i**2 % 10 == 1: sayaç1 +=1
    elif i**2 % 10 == 4: sayaç2 +=1
    elif i**2 % 10 == 9: sayaç3 +=1
print ("1->", kere, "karesi sayılardan sonu 1'le bitenler:", sayaç1, ", 4'le bitenler:", sayaç2, "ve 9'la bitenlerin toplamı:", sayaç3)
print()
sayaç=0
for i in range (1, kere): sayaç = sayaç + (i**(-1))
print (sayaç, "- ln(", kere, ") =", sayaç - log (kere))
print()
toplam=0
for i in range (1, 2001):
    if i % 2 == 0: toplam+=-i
    else: toplam+=i
# Gerçekte 1000 kere -1'i toplar...
print ("[1->2000] +tekler ve -çiftler toplamı:", toplam)
print()
"""
for i in range (3, 10000):
    toplam=1
    for j in range (2, i):
        if (i//j)*j == i: toplam+=j
    if toplam == i: print (i, "bir ideal sayıdır")
Çıktı:
6 bir ideal sayıdır
28 bir ideal sayıdır
496 bir ideal sayıdır
8128 bir ideal sayıdır
"""
print()
bayrak=0
for j in range (2, kere):
    if (kere//j)*j==kere and trunc (sqrt (j))**2 == j: bayrak=1; break
if not bayrak: print (kere, "sayısının bölenleri kare-muaf'tır")
else: print (kere, "sayısının", j, "böleni ideal-kare'dir")
print()
