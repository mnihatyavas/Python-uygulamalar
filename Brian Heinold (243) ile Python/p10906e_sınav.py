# coding:iso-8859-9 Türkçe

from random import randint
from pprint import pprint

print ("7x5'lik sıfır matrisi==>")
L = [[0]*5 for i in range (7)]
pprint (L)

print ("\n7x5'lik tesadüfi sıfır-bir matrisi==>")
L = [[randint (0, 1) for j in range (5)] for i in range (7)]
pprint (L)
print()
b1 = len ([L[i][j] for i in range(7) for j in range(5) if L[i][j] == 0])
b2 = b3 = randint (0, b1-1)
for i in range (7):
    for j in range (5):
        if L[i][j] == 0: L[i][j] += 1; b2 -= 1
        if b2 < 0: break
    if b2 < 0: break
print ("\nToplam", b1, "0'dan ilk tesadüfi", b3+1, "adedini 1'ledim!")
pprint (L)
