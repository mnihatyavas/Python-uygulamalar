# coding:iso-8859-9 T�rk�e

from math import *
from random import *

seri_toplam� = 0
for i in range (1, 10001): seri_toplam� = seri_toplam� + 1 / i**2
print ("1/1 + 1/ 2^2 +..+1/1000^2 =", seri_toplam�)
print ()
say� = random()
print ("23.865^", say�, ") = ", 23.865**say�, sep="")
print ()
say�1 = randint (1,100)
say�2 = random()
say�3 = say�1 + say�2
print (say�3, "^", say�2, ") = ", say�3**say�2, sep="")
print ("pow(", say�3, ",", say�2, ") = ", pow (say�3, say�2), sep="")
print ()
say� = randint (1, 50)
print ("Fakt�riyel(", say�, ") = ", factorial (say�), sep="")
