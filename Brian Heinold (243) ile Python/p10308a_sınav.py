# coding:iso-8859-9 T�rk�e

from random import *
from math import *

print ("[1->9] aras� k�suratl� 50 tesad�fi say�: [", end="")
for i in range (50):
    say�1 = randint (1, 9)
    say�2 = random()
    print (round ((say�1 + say�2), 2), end=" ")
print ("]")
print ("\n[1->51] aras� k�suratl� 50 tesad�fi say�: [", end="")
for i in range (50):
    say�1 = randint (1, i+2)
    say�2 = random()
    print (round (say�1 + say�2, 5), end=" ")
print ("]")

a�� = eval (input ("\n[-180-->180] aras� bir a�� girin: "))
if a�� >= 0:
    if a�� <= 180: print ("A��n�z:", a��, "derecedir.")
    else: print ("A��n�z: 180 derecedir.")
else:
    if a�� >= -180: print ("A��n�z:", 360 + a��, "derecedir.")
    else: print ("A��n�z: 180 derecedir.")

saniye = eval (input ("\n[0-->3599] aras� bir saniye girin: "))
if saniye < 0: saniye = 0
if saniye > 3599: saniye = 3599
dakika = saniye // 60
saniye = saniye % 60
print ("Girdi�iniz zaman:", dakika, "dakika ve", saniye, "saniye'dir.")

zaman1 = eval (input ("\n[0-->24] aras� bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = eval (input ("\nKa� saat daha burada kalacaks�n?: "))
if zaman2 < 0: zaman2 = -zaman2
print ("Buradan saat tam ", (zaman1 + zaman2 % 24) % 24, ".00'de ayr�lmal�s�n�z!", sep="")

de�er = input ("\nHerhangibir (-/+) tamsay� girin: ")
say� = trunc (eval (de�er))
uzunluk = len (de�er)
if say� < 0:
    uzunluk = uzunluk - 1
    say� = -say�
    for i in range (uzunluk):
        taban = say� % (10**(i+1))
        print ("2^", -taban, " = ", 2**(-taban), sep="")
        print()
else:
    for i in range (uzunluk):
        taban = say� % (10**(i+1))
        print ("2^", taban, " = ", 2**(taban), sep="")
        print()
