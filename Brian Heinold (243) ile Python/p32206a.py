# coding:iso-8859-9 T�rk�e

from cmath import *

print ("Kompleks say�lar:", 3+7j, 6.85 - 3.62J, 3.5j, complex (5, 8.5) )

a = 3+4j
b = 9.54 - 7.65j
print ("\nKompleks i�lemler:", a+b, a-b, a*b, a/b)

print ("\nPolar �evrimler:", polar (a), polar (b), polar (a*b), polar (a/b) )

print ("\nRectangular �evrimler:", rect (polar (a)[0], polar (a)[1]), rect (polar (b)[0], polar (b)[1]), rect (polar (a*b)[0], polar (a*b)[1]), rect (polar (a/b)[0], polar (a/b)[1]) )
