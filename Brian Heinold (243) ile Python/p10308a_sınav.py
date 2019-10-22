# coding:iso-8859-9 Türkçe

from random import *
from math import *

print ("[1->9] arası küsuratlı 50 tesadüfi sayı: [", end="")
for i in range (50):
    sayı1 = randint (1, 9)
    sayı2 = random()
    print (round ((sayı1 + sayı2), 2), end=" ")
print ("]")
print ("\n[1->51] arası küsuratlı 50 tesadüfi sayı: [", end="")
for i in range (50):
    sayı1 = randint (1, i+2)
    sayı2 = random()
    print (round (sayı1 + sayı2, 5), end=" ")
print ("]")

açı = eval (input ("\n[-180-->180] arası bir açı girin: "))
if açı >= 0:
    if açı <= 180: print ("Açınız:", açı, "derecedir.")
    else: print ("Açınız: 180 derecedir.")
else:
    if açı >= -180: print ("Açınız:", 360 + açı, "derecedir.")
    else: print ("Açınız: 180 derecedir.")

saniye = eval (input ("\n[0-->3599] arası bir saniye girin: "))
if saniye < 0: saniye = 0
if saniye > 3599: saniye = 3599
dakika = saniye // 60
saniye = saniye % 60
print ("Girdiğiniz zaman:", dakika, "dakika ve", saniye, "saniye'dir.")

zaman1 = eval (input ("\n[0-->24] arası bir saat girin: "))
if zaman1 < 0: zaman1 = 0
if zaman1 > 24: zaman1 = 24
zaman2 = eval (input ("\nKaç saat daha burada kalacaksın?: "))
if zaman2 < 0: zaman2 = -zaman2
print ("Buradan saat tam ", (zaman1 + zaman2 % 24) % 24, ".00'de ayrılmalısınız!", sep="")

değer = input ("\nHerhangibir (-/+) tamsayı girin: ")
sayı = trunc (eval (değer))
uzunluk = len (değer)
if sayı < 0:
    uzunluk = uzunluk - 1
    sayı = -sayı
    for i in range (uzunluk):
        taban = sayı % (10**(i+1))
        print ("2^", -taban, " = ", 2**(-taban), sep="")
        print()
else:
    for i in range (uzunluk):
        taban = sayı % (10**(i+1))
        print ("2^", taban, " = ", 2**(taban), sep="")
        print()
