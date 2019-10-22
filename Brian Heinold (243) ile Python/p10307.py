# coding:iso-8859-9 Türkçe

from math import *
from random import *

seri_toplamı = 0
for i in range (1, 10001): seri_toplamı = seri_toplamı + 1 / i**2
print ("1/1 + 1/ 2^2 +..+1/1000^2 =", seri_toplamı)
print ()
sayı = random()
print ("23.865^", sayı, ") = ", 23.865**sayı, sep="")
print ()
sayı1 = randint (1,100)
sayı2 = random()
sayı3 = sayı1 + sayı2
print (sayı3, "^", sayı2, ") = ", sayı3**sayı2, sep="")
print ("pow(", sayı3, ",", sayı2, ") = ", pow (sayı3, sayı2), sep="")
print ()
sayı = randint (1, 50)
print ("Faktöriyel(", sayı, ") = ", factorial (sayı), sep="")
