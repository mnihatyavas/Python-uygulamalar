# coding:iso-8859-9 Türkçe

from random import *
from math import *

açı = eval (input ("Herhangi bir '-/+' açı girin: "))
radyan = açı * pi / 180
print ("Sin(", açı, ") = ", sin (radyan), sep="")
print ("Cos(", açı, ") = ", cos (radyan), sep="")
print ("Tan(", açı, ") = ", tan (radyan), sep="")

Y = abs (eval (input ("\nHerhangibir 4 haneli '+' yıl girin: ")))
C = trunc (Y / 100)
m = (15 + C - (C/4) - (8*C+13)/25) % 30
n = (4 + C - C/4) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7

if d == 29 and e == 6: print ("Paskalya tarihi: Nisan 19")
elif d == 28 and e == 6 and (m==2 or m==5 or m==10 or m==13 or m==16 or m==21 or m==24 or m==39): print ("Paskalya tarihi: Nisan 18")
elif (trunc(d)+trunc(e)) > 9: print ("Paskalya tarihi: Nisan", trunc (d+e-9))
else: print ("Paskalya tarihi: Mart", trunc (22+d+e))

artık = False
if   Y//100 * 100 == Y and Y % 400 == 0: artık = True
elif Y//100 * 100 != Y and Y%4 == 0: artık = True

if artık: print (Y, "yılı artık yıldır, yani Şubat 29 çeker.")
else: print (Y, "yılı artık yıl değildir, yani Şubat 28 çeker.")

if Y > 1600:
    artık = False
    sayaç = 0
    for i in range (1600, Y+1):
        if   i//100 * 100 == i and i % 400 == 0: artık = True
        elif i//100 * 100 != i and i%4 == 0: artık = True
        if artık: sayaç += 1; artık=False
    print ("Ayrıca 1600 yılından bu yıla kadar toplam:", sayaç, "adet artık yıl vardır.")

kuruş = abs (trunc (eval (input ("\n100 Krş veya altı tamsayı bozukluk girin: "))))
if kuruş > 100: kuruş = 100
kalan = kuruş
k1=k2=k3=k4=0
if kalan >= 50: k1 = kalan//50; kalan = kalan - k1*50
if kalan >= 25: k2 = kalan//25; kalan = kalan - k2*25
if kalan >= 10: k3 = kalan//10; kalan = kalan - k3*10
if kalan >= 5: k4 = kalan//5; kalan = kalan - k4*5

print (kuruş, " kuruş içinde ", k1, " adet 50 kuruş ", k2, " adet 25 kuruş ", k3, " adet 10 kuruş ", k4, " adet 5 kuruş ve ", kalan, " adet 1 kuruş bozukluk vardır.")

satır = abs (trunc (eval (input ("\nMatrisin satır sayısını girin: "))))
sütun = abs (trunc (eval (input ("\nMatrisin sütun sayısını girin: "))))
print()
k=0
for i in range (satır):
    for j in range (sütun):
        print (k, end=" ")
        k += 1
        if k > 9: k = 0
    print()
