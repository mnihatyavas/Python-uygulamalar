# coding:iso-8859-9 T�rk�e

from math import *
from random import randint

do�ru=yanl��=0
for i in range (1,11):
    a = randint (1,9)
    b = randint (1,9)
    c = a * b
    print (i, ".soru: ", a, " * ", b, " = ?", sep="")
    cevap = eval (input ("�arpman�n cevab�n� girin: "))
    if cevap == c: print ("Do�ru!"); do�ru += 1
    else: print ("Yanl��!"); yanl�� += 1
    print()
print ("10 soruda toplam", do�ru, "adet do�ru ve", yanl��, "adet yanl�� cevap verdiniz!")

zaman1 = eval (input ("\n[0-->24] aras� bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = abs (eval (input ("\nKa� saat daha burada kalacaks�n?: ")))
zaman3 = (zaman1 + zaman2 % 24) % 24
sembol =""
if zaman3 > 12: sembol = "pm"; zaman3 -= 12
else: sembol = "am"
print ("Buradan saat tam ", zaman3, ".00 ", sembol, "'de ayr�lmal�s�n�z!", sep="")
