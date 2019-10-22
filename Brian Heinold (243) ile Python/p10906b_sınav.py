# coding:iso-8859-9 Türkçe

from random import randint
try: sayı1 = abs (int (eval (input ("Enbüyük ortak bölenin ilk sayısını gir: "))))
except Exception: sayı1 = randint (2,1000)
try: sayı2 = abs (int (eval (input ("EOB'nin ikinci sayısını gir: "))))
except Exception: sayı2 = randint (2,1000)
print (sayı1,sayı2)
if sayı2 > sayı1: sayı1,sayı2 = sayı2,sayı1; print (sayı1,sayı2)
while sayı2:
    ara = sayı2
    sayı2 = sayı1 % sayı2
    sayı1 = ara
print (sayı1,sayı2)
if sayı1 != 1: print ("EOB=", sayı1)
else: print ("EOB namevcut!")
