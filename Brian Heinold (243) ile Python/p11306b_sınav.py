# coding:iso-8859-9 T�rk�e

def fakt�r1 (say�):
    L = []
    i = 2
    while 2 <= i < (say�//2+1):
        if say� % i == 0:
            L = L + [i]
            say� = say� // i
            i = 2
        else: i +=1
    return L + [say�]

def fakt�r2 (say�, L=[]):
    for i in range (2, say� // 2 + 1):
        if say� % i == 0: return L + [i] + fakt�r2 (say� // i)
    return L + [say�]

print ("2 ayr� y�ntemle [0,10000] aras� tesad�fi say�n�n fakt�r listesi:")
from random import randint
n = randint (0, 10000)
L = fakt�r1 (n)
print ("Say�: ", n, ", listeler: ", L, " ve ", fakt�r2 (n), ", fakt�r say�s�: ", len (L), sep="")
