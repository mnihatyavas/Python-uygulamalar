# coding:iso-8859-9 T�rk�e

print ("[0->100] geli�ig�zel say�l� 15x10 matris listesi:\n", "-"*49, sep="")
from random import randint
L = [[randint (0,100) for j in range (15)] for i in range (10)]
from pprint import pprint
pprint (L)

print ("\n�nceki matrisin artan s�ral� 1x150 listesi:\n", "-"*43, sep="")
L1 = []
for i in range (len (L)):
    for j in range (len (L[0])):
        L1 = L1 + [L[i][j]]
L1.sort ()
print (L1)

S = {}
saya� = 1
for i in range (len (L1)-1):
    if L1[i] == L1[i+1]:
        saya� +=1
    else:
        S [L1[i] ] = saya�
        saya� = 1
S [L1[i+1] ] = saya�
print ("\n�nceki listenin her eleman�n�n tekrar�n� i�eren ", len (S), " ebatl� s�zl�k:\n", "-"*65, sep="")
pprint (S)

L = []
toplam = 0
for k in S.items():
    L = L + [(k[1], k[0])]
    toplam +=k[1]
L.sort()
print ("\n�nceki s�zl���n artan tekrara g�re s�ral� listesi:\n", "-"*50, sep="")
pprint (L)
print ("-"*24, "\nTekrarlar�n toplam�: ", toplam, sep="")
