# coding:iso-8859-9 Türkçe

def faktör1 (sayı):
    L = []
    i = 2
    while 2 <= i < (sayı//2+1):
        if sayı % i == 0:
            L = L + [i]
            sayı = sayı // i
            i = 2
        else: i +=1
    return L + [sayı]

def faktör2 (sayı, L=[]):
    for i in range (2, sayı // 2 + 1):
        if sayı % i == 0: return L + [i] + faktör2 (sayı // i)
    return L + [sayı]

print ("2 ayrı yöntemle [0,10000] arası tesadüfi sayının faktör listesi:")
from random import randint
n = randint (0, 10000)
L = faktör1 (n)
print ("Sayı: ", n, ", listeler: ", L, " ve ", faktör2 (n), ", faktör sayısı: ", len (L), sep="")
