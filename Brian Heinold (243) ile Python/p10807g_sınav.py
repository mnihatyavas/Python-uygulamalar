#coding:iso-8859-9 T�rk�e

from random import randint
L1 = [[0]*10 for i in range (10)]
for i in range (10):
    for j in range (10): L1[i][j] = randint (0,1)

try: i = abs (eval ( input ("\n[0->9] sat�r endeks numaras� girin: ")))
except Exception: i = randint (0,9)
if i > 9: i = randint (0,9)
try: j = abs (eval ( input ("[0->9] kolon endeks numaras� girin: ")))
except Exception: j = randint (0,9)
if j > 9: j = randint (0,9)

print ("\nMatristeki at�� konumunuz:", i+1, j+1)
if L1[i][j]: print ("Bravo! Bir denizalt� vurdun...")
else: print ("Maalesef karavana at��...")

print ("\nAt���n�z� kontrol edin:")
from pprint import pprint
pprint (L1)
print()
ASCII = ''.join ([chr(i) for i in range(1,6)]) + ''.join ([chr(i) for i in range(14,47)]) + ''.join ([chr(i) for i in range(48,128)]) + ''.join ([chr(i) for i in range(161,173)]) + ''.join ([chr(i) for i in range(174,208)]) + ''.join ([chr(i)for i in range(209,221)]) + ''.join ([chr(i) for i in range(223,240)]) + ''.join ([chr(i) for i in range(255,256)]) + ''.join ([chr(i) for i in range(286,288)]) + ''.join ([chr(i) for i in range(304,306)]) + ''.join ([chr(i) for i in range(350,352)]) + ''.join ([chr(i) for i in range(496,497)])
ASCII = ASCII.replace (" ", "")
A = list (ASCII*2)
from random import shuffle
shuffle (A)
L1 = [[' ']*20 for i in range (20)]
k = 0
for i in range (len(L1)):
    for j in range (len(L1[0])):
        L1[i][j] = A[k]; k +=1
print ("\nHer bir karakterin azami 2 kez tekrarland��� [20x20] ASCII matrisi:")
for i in range (len(L1)):
    for j in range(len(L1[0])):
        print (L1[i][j], end='  ')
    print()
print ("\n�zel bo�lukluz tikel ASCII karakterlerimiz:")
for k in ASCII:
    print (ord (k), "=", k, sep="", end=" ")
