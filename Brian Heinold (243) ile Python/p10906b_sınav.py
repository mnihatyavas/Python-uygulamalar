# coding:iso-8859-9 T�rk�e

from random import randint
try: say�1 = abs (int (eval (input ("Enb�y�k ortak b�lenin ilk say�s�n� gir: "))))
except Exception: say�1 = randint (2,1000)
try: say�2 = abs (int (eval (input ("EOB'nin ikinci say�s�n� gir: "))))
except Exception: say�2 = randint (2,1000)
print (say�1,say�2)
if say�2 > say�1: say�1,say�2 = say�2,say�1; print (say�1,say�2)
while say�2:
    ara = say�2
    say�2 = say�1 % say�2
    say�1 = ara
print (say�1,say�2)
if say�1 != 1: print ("EOB=", say�1)
else: print ("EOB namevcut!")
