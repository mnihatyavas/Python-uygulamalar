# coding:iso-8859-9 Türkçe

from math import *
from fractions import Fraction
from fractions import gcd

f1 = Fraction (3, 4)
f2 = Fraction (4,3)
print ("Fraction(3,4) ve Fraction(4,3):", f1, f2)
print ("Fraction(3,4).numerator ve Fraction(3,4).denominator: ", f1.numerator, f1.denominator)
print ("log(Fraction(4,3))**12 =", log (f2)**12)

print ("\nfloat(Fraction(3,4)) =", float (f1) )
print ("Fraction(0.75) =", Fraction (0.75) )

print ("\nFraction('.333').limit_denominator(100) =", Fraction('.333').limit_denominator(100) )
print ("Fraction('.333').limit_denominator(1000) =", Fraction('.333').limit_denominator(1000) )
print ("Fraction(pi).limit_denominator(1000) =", Fraction(pi).limit_denominator(1000) )

print()
for i in range (20, 41):
    for j in range (i+1, 41):
        eob = gcd (i, j)
        if eob != 0 and eob != 1: print ("EnbüyükOrtakBölen gcd(",i,",",j,")=", eob, sep="")
