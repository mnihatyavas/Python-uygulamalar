# coding:iso-8859-9 T�rk�e

from random import *
from math import *

a�� = eval (input ("Herhangi bir '-/+' a�� girin: "))
radyan = a�� * pi / 180
print ("Sin(", a��, ") = ", sin (radyan), sep="")
print ("Cos(", a��, ") = ", cos (radyan), sep="")
print ("Tan(", a��, ") = ", tan (radyan), sep="")

Y = abs (eval (input ("\nHerhangibir 4 haneli '+' y�l girin: ")))
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

art�k = False
if   Y//100 * 100 == Y and Y % 400 == 0: art�k = True
elif Y//100 * 100 != Y and Y%4 == 0: art�k = True

if art�k: print (Y, "y�l� art�k y�ld�r, yani �ubat 29 �eker.")
else: print (Y, "y�l� art�k y�l de�ildir, yani �ubat 28 �eker.")

if Y > 1600:
    art�k = False
    saya� = 0
    for i in range (1600, Y+1):
        if   i//100 * 100 == i and i % 400 == 0: art�k = True
        elif i//100 * 100 != i and i%4 == 0: art�k = True
        if art�k: saya� += 1; art�k=False
    print ("Ayr�ca 1600 y�l�ndan bu y�la kadar toplam:", saya�, "adet art�k y�l vard�r.")

kuru� = abs (trunc (eval (input ("\n100 Kr� veya alt� tamsay� bozukluk girin: "))))
if kuru� > 100: kuru� = 100
kalan = kuru�
k1=k2=k3=k4=0
if kalan >= 50: k1 = kalan//50; kalan = kalan - k1*50
if kalan >= 25: k2 = kalan//25; kalan = kalan - k2*25
if kalan >= 10: k3 = kalan//10; kalan = kalan - k3*10
if kalan >= 5: k4 = kalan//5; kalan = kalan - k4*5

print (kuru�, " kuru� i�inde ", k1, " adet 50 kuru� ", k2, " adet 25 kuru� ", k3, " adet 10 kuru� ", k4, " adet 5 kuru� ve ", kalan, " adet 1 kuru� bozukluk vard�r.")

sat�r = abs (trunc (eval (input ("\nMatrisin sat�r say�s�n� girin: "))))
s�tun = abs (trunc (eval (input ("\nMatrisin s�tun say�s�n� girin: "))))
print()
k=0
for i in range (sat�r):
    for j in range (s�tun):
        print (k, end=" ")
        k += 1
        if k > 9: k = 0
    print()
