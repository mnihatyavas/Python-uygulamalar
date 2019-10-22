# coding:iso-8859-9 T�rk�e

L = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

print ("2 boyutlu (3x4) liste (yanyana):", L)

print ("\n2 boyutlu (3x4) liste (altalta):")
for sat�r in range(3):
    for kolon in range(4): print (L[sat�r][kolon], end=" ")
    print()

print ("\nTamsay� FORMATLI 2 boyutlu (3x4) liste (altalta):")
for i in range(3):
    for j in range(4): print ("{:3d}" .format (L[i][j]), end="")
    print()
# s ile dizge formatlan�r, ^ ile ortalan�r, > ile sa�a hizalan�r...

print ("\nOndal�k FORMATLI 2 boyutlu (3x4) liste (altalta):")
for i in range(3):
    for j in range(4): print ("{:6.2f}" .format (L[i][j]), end="")
    print()

from pprint import pprint
print ("\npprint ile 2 boyutlu (3x4) liste (altalta):")
for e in L: pprint (e)

print ("\n10x20'lik 2 boyutlu say�sal bir liste yaratma ve print'leme:")
L=[[0]*20 for i in range (10)]
print (L)

print ("\n10x20'lik 2 boyutlu say�sal listeyi pprint'leme:")
pprint (L)
from random import randint

print ("\n10x20'lik 2 boyutlu say�sal listeye [1->20] tesad�fi atama ve pprint'leme:")
for i in range (10):
    for j in range (20):
        L[i][j] = randint (1,20)
pprint (L)

print ("\n10x20'lik 2 boyutlu [1->20] tesad�fi de�erli listeyi altalta print'leme:")
for i in range (10):
    for j in range (20):
        print (L[i][j], end=" ")
    print()

saya� = 0
for i in range (10):
    for j in range (20):
        if L[i][j] % 2 == 0: saya� +=1
print ("\n10x20'lik 2 boyutlu [1->20] tesad�fi de�erli listedeki �iftli eleman say�s�:", saya�)
saya� = sum ([1 for i in range (10) for j in range (20) if L[i][j] % 2 != 0])
print ("\n10x20'lik 2 boyutlu [1->20] tesad�fi de�erli listedeki tekli eleman say�s�:", saya�)

print()
sat�r = randint (0, 9)
print (sat�r+1, " no'lu sat�r elemanlar�:", L[sat�r])

print()
kolon = randint (0, 19)
print (kolon+1, " no'lu kolon elemanlar�:", [L[i][kolon] for i in range (len (L))])

M = []
for i in range (10):
    for j in range (20):
        M.append (L[i][j])
print ("\n10x20'lik matris listeyi 1x200 dizi liste'ye �evirme:", M)

print ("\n10x20'lik matris listeyi 1x200 dizi liste'ye �evirme:", [j for M in L for j in M])