# coding:iso-8859-9 T�rk�e

from math import *

santim = eval (input ("Santimetre de�eri girin: "))
if santim < 0: santim = -santim
print (santim, "santimetre =", round (santim / 2.54, 2), "inch'dir.")

harf = input ("\nC: Celsius, F:Fahrenheit veya K:Kelvin gir: ")
if harf != 'c' and harf != 'f' and harf != 'k': harf = 'c'
�s� = eval (input (harf + " Is� de�erini girin: "))
if harf == "k":
    if �s� < 0: �s� = 0;
    print (�s�, "K = ", round(�s�-273.15, 2), "C = ", round(1.8*(�s�-273.15)+32, 2), "F", sep="")
elif harf == "c":
    if �s� < -273.15: �s� = -273.15;
    print (�s�,"C = ", round(�s�+273.15, 2), "K = ", round(1.8*�s�+32, 2), "F", sep="", end="")
    if �s� < 0: print ("==>Donma noktas� alt�")
    elif 0 < �s� <=100: print ("==>Normal s�cakl�k aral���")
    else: print ("==>Kaynama noktas� �st�")
else:
    if �s� < -459.67: �s� = -459.67;
    print (�s�, "F = ", round(5/9*(�s�-32), 2), "C = ", round(5/9*(�s�-32)+273.15, 2), "K", sep="")

say� = trunc (eval (input ("\nBir tamsay� girin: ")))
print (say�, "tamsay�s�n�n b�lenleri:", end=" ")
if say� < 0: say� = -say�; negatif = True
else: negatif = False
for i in range (1, say�+1):
    if (say�/i)*i == (say�//i)*i:
        if not negatif: print (i, end=" ")
        else: print (-i, end=" ")
print("\n")