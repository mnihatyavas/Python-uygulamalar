# coding:iso-8859-9 T�rk�e

def birle�tir1 (La, Lb):
    L = La + Lb
    return L

def birle�tir2 (La, Lb):
    L = La + Lb
    L.sort()
    return L

def birle�tir3 (La, Lb):
    L = []
    if len (La) <= len (Lb): u = len (La)
    else: u = len (Lb)
    for i in range (u):
        L = L + [La[i]]
        L = L + [Lb[i]]
    return L

def birle�tir4 (La, Lb):
    L = []
    if len (La) <= len (Lb):
        for i in range (len (La)):
            L = L + [La[i]]
            L = L + [Lb[i]]
        for j in range (i, len (Lb)):
            L = L + [Lb[j]]
    else:
        for i in range (len (Lb)):
            L = L + [La[i]]
            L = L + [Lb[i]]
        for j in range (i, len (La)):
            L = L + [La[j]]
    return L

L1 = L2 = []
i = 0
for sat�r in open ("sorular.txt"):
    L1 = L1 + ["Soru: " + str (i+1) + ") " + sat�r.strip()]
    i +=1

i = 0
for sat�r in open ("cevaplar.txt"):
    L2 = L2 + ["Cevap: " + str (i+1) + ") " + sat�r.strip()]
    i +=1

from pprint import pprint
pprint (L1)
print()
pprint (L2)

print()
pprint (birle�tir1 (L1, L2) )
print()
pprint (birle�tir2 (L1, L2) )
print()
pprint (birle�tir3 (L1, L2) )
print()
pprint (birle�tir4 (L1, L2) )