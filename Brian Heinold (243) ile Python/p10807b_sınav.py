# coding:iso-8859-9 T�rk�e

from random import randint
L = []
for i in range (4): L.append (randint (1, 5))
print (L)
tutturdu = False
M = [[0]*4 for i in range (100)]
for i in range (100):
    for j in range (4):
        M[i][j] = randint (1, 5)
#from pprint import pprint
#pprint (M)
if L in M: print ("Ya�as�n, nihayet 100 kolonluk 4'l� lotariyi tutturdum!")
else: print ("Maalesef, 100 kolonluk 4'l� lotariyi yine tutturamad�m!")

from random import shuffle
L = [0,1,2,3,4,5]
shuffle (L)
for i in range (2): del L[0]
print ("\nSay�lar�m:", L)
toplam = 0
for i in range (100):
    for j in range (100000):
        M = [0,1,2,3,4,5]
        shuffle (M)
        for k in range (2): del M[0]
        if L == M: break;
    toplam +=j
print ("100 kerede ortalama bulma say�s�:", toplam//100)
