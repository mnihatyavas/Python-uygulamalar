# coding:iso-8859-9 Türkçe

from math import *

santim = eval (input ("Santimetre değeri girin: "))
if santim < 0: santim = -santim
print (santim, "santimetre =", round (santim / 2.54, 2), "inch'dir.")

harf = input ("\nC: Celsius, F:Fahrenheit veya K:Kelvin gir: ")
if harf != 'c' and harf != 'f' and harf != 'k': harf = 'c'
ısı = eval (input (harf + " Isı değerini girin: "))
if harf == "k":
    if ısı < 0: ısı = 0;
    print (ısı, "K = ", round(ısı-273.15, 2), "C = ", round(1.8*(ısı-273.15)+32, 2), "F", sep="")
elif harf == "c":
    if ısı < -273.15: ısı = -273.15;
    print (ısı,"C = ", round(ısı+273.15, 2), "K = ", round(1.8*ısı+32, 2), "F", sep="", end="")
    if ısı < 0: print ("==>Donma noktası altı")
    elif 0 < ısı <=100: print ("==>Normal sıcaklık aralığı")
    else: print ("==>Kaynama noktası üstü")
else:
    if ısı < -459.67: ısı = -459.67;
    print (ısı, "F = ", round(5/9*(ısı-32), 2), "C = ", round(5/9*(ısı-32)+273.15, 2), "K", sep="")

sayı = trunc (eval (input ("\nBir tamsayı girin: ")))
print (sayı, "tamsayısının bölenleri:", end=" ")
if sayı < 0: sayı = -sayı; negatif = True
else: negatif = False
for i in range (1, sayı+1):
    if (sayı/i)*i == (sayı//i)*i:
        if not negatif: print (i, end=" ")
        else: print (-i, end=" ")
print("\n")