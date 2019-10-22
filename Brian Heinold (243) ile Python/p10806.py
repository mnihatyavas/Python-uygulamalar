# coding:iso-8859-9 Türkçe

L = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

print ("2 boyutlu (3x4) liste (yanyana):", L)

print ("\n2 boyutlu (3x4) liste (altalta):")
for satır in range(3):
    for kolon in range(4): print (L[satır][kolon], end=" ")
    print()

print ("\nTamsayı FORMATLI 2 boyutlu (3x4) liste (altalta):")
for i in range(3):
    for j in range(4): print ("{:3d}" .format (L[i][j]), end="")
    print()
# s ile dizge formatlanır, ^ ile ortalanır, > ile sağa hizalanır...

print ("\nOndalık FORMATLI 2 boyutlu (3x4) liste (altalta):")
for i in range(3):
    for j in range(4): print ("{:6.2f}" .format (L[i][j]), end="")
    print()

from pprint import pprint
print ("\npprint ile 2 boyutlu (3x4) liste (altalta):")
for e in L: pprint (e)

print ("\n10x20'lik 2 boyutlu sayısal bir liste yaratma ve print'leme:")
L=[[0]*20 for i in range (10)]
print (L)

print ("\n10x20'lik 2 boyutlu sayısal listeyi pprint'leme:")
pprint (L)
from random import randint

print ("\n10x20'lik 2 boyutlu sayısal listeye [1->20] tesadüfi atama ve pprint'leme:")
for i in range (10):
    for j in range (20):
        L[i][j] = randint (1,20)
pprint (L)

print ("\n10x20'lik 2 boyutlu [1->20] tesadüfi değerli listeyi altalta print'leme:")
for i in range (10):
    for j in range (20):
        print (L[i][j], end=" ")
    print()

sayaç = 0
for i in range (10):
    for j in range (20):
        if L[i][j] % 2 == 0: sayaç +=1
print ("\n10x20'lik 2 boyutlu [1->20] tesadüfi değerli listedeki çiftli eleman sayısı:", sayaç)
sayaç = sum ([1 for i in range (10) for j in range (20) if L[i][j] % 2 != 0])
print ("\n10x20'lik 2 boyutlu [1->20] tesadüfi değerli listedeki tekli eleman sayısı:", sayaç)

print()
satır = randint (0, 9)
print (satır+1, " no'lu satır elemanları:", L[satır])

print()
kolon = randint (0, 19)
print (kolon+1, " no'lu kolon elemanları:", [L[i][kolon] for i in range (len (L))])

M = []
for i in range (10):
    for j in range (20):
        M.append (L[i][j])
print ("\n10x20'lik matris listeyi 1x200 dizi liste'ye çevirme:", M)

print ("\n10x20'lik matris listeyi 1x200 dizi liste'ye çevirme:", [j for M in L for j in M])