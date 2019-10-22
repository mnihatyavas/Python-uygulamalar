# coding:iso-8859-9 Türkçe

from math import *
from random import randint

doğru=yanlış=0
for i in range (1,11):
    a = randint (1,9)
    b = randint (1,9)
    c = a * b
    print (i, ".soru: ", a, " * ", b, " = ?", sep="")
    cevap = eval (input ("Çarpmanın cevabını girin: "))
    if cevap == c: print ("Doğru!"); doğru += 1
    else: print ("Yanlış!"); yanlış += 1
    print()
print ("10 soruda toplam", doğru, "adet doğru ve", yanlış, "adet yanlış cevap verdiniz!")

zaman1 = eval (input ("\n[0-->24] arası bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = abs (eval (input ("\nKaç saat daha burada kalacaksın?: ")))
zaman3 = (zaman1 + zaman2 % 24) % 24
sembol =""
if zaman3 > 12: sembol = "pm"; zaman3 -= 12
else: sembol = "am"
print ("Buradan saat tam ", zaman3, ".00 ", sembol, "'de ayrılmalısınız!", sep="")
