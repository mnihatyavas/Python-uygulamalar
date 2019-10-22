#coding:iso-8859-9 Türkçe

from random import randint
x1 = randint (2,10); x2 = randint (2,10); x3 = randint (2,10)

L = [[[0]*x1 for j in range (x2)] for i in range (x3)]
from pprint import pprint
print ("[", x3, "x", x2, "x", x1, "] boyutlu boş matrisimiz:", sep="")
pprint (L)
print ("\n[", x3, "x", x2, "x", x1, "] boyutlu dolu matrisimiz:", sep="")
for i in range (x3):
    for j in range (x2):
        for k in range (x1):
            L[i][j][k] = randint (0,9)
pprint (L)
print ("\n[", x3, "x", x2, "x", x1, "] boyutlu dolu matrisimizin toplamı, ", x2*x3, " elemanlı listemiz:", sep="")
L1 = []
L1 += [sum (L[i][j]) for i in range (len(L)) for j in range (len(L[0]))]
print (L1)
print ("\n[", x3, "x", x2, "x", x1, "] boyutlu özel düzenlemeli matris ve listemiz yanyana==>", sep="")
for i in range(len(L)):
    for j in range(len(L[0])):
        print ("(", end="")
        for k in range(len(L[0][0])):
            if k < len(L[0][0])-1: print (L[i][j][k], ",", end="")
            else:
                print (L[i][j][k], ") ", end="")
                print (sum (L[i][j]))
    print()
print ("[4x3x2] sabit ve dolu yaratılan matrisimiz==>")
L = [[[randint (0,99) for k in range(2)] for j in range(3)] for i in range(4)]
pprint (L)
print ("\n[4x3x2] matrisimizin iç-eleman toplamlı dökümü==>")
for i in range(4):
    for j in range(3):
        for k in range(2):
            if k == 1: print (L[i][j][k], sep="", end="")
            else: print (L[i][j][k], sep="", end="+")
        print ("=", sum(L[i][j]), sep="", end=" ")
    print()

print ("\n[4x3x2] matrisimizin iç-eleman toplamlı yanyana dökümü==>")
for i in range(4):
    for j in range(3):
        print ("(", end="")
        for k in range(2):
            if k == 0: print (L[i][j][k], end=",")
            else: print (L[i][j][k], end=") ")
    print ("     ", [sum(L[i][j]) for j in range(3)] )

x1 = randint (2,10); x2 = randint (2,4); x3 = randint (2,3)
print ("\n[", x1, "x", x2, "x", x3, "] boyutlu matrisimiz==>", sep="")
L = [[[randint(10,99) for k in range(x3)] for j in range(x2)] for i in range(x1)]
pprint (L)

print ("\n[", x1, "x", x2, "x", x3, "] ve [", x1, "x", x2, "] toplamalı boyutlu matrislerimiz==>", sep="")
for i in range(x1):
    for j in range(x2):
        print ("(", end="")
        for k in range(x3):
            if k != x3-1: print (L[i][j][k], end=",")
            else: print (L[i][j][k], end=") ")
    print ("     ", [sum(L[i][j]) for j in range(x2)] )

print ("\n[", x1, "x", x2, "] toplamalı ve [", x1, "x", x2, "x", x3, "] ve boyutlu matrislerimiz==>", sep="")
for i in range(x1):
    print ([sum(L[i][j]) for j in range(x2)], end="     " )
    for j in range(x2):
        print ("(", end="")
        for k in range(x3):
            if k != x3-1: print (L[i][j][k], end=",")
            else: print (L[i][j][k], end=") ")
    print()
