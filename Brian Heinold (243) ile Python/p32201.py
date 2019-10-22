# coding:iso-8859-9 T�rk�e

from math import *
mFonk = """
    sin, cos, tan: Trigonometrik fonksiyonlar
    asin, acos, atan: Ters trigonometrik fonksiyonlar
    atan2 (y,x): arctan (y / x)
    sinh, cosh, tanh: Hiperbolik fonksiyonlar
    asinh, acosh, atanh: Ters hiperbolik fonksiyonlar
    log, log10: do�al ln ve 10 temelli log
    log1p: log (1 + x)
    exp: e^x
    degrees, radians: Derece'den<-->radyan'a �evirir (180 derece = 1.pi)
    floor: floor (x) alt zemin tamsay�
    ceil: ceil (x) �st tavan tamsay�
    e, pi: e ve ? sabitleri
    factorial: factorial (x), 1*2*3*..*x
    modf (x): x'in tamsay�s�n� ve k�s�rat�n� ay�r�r
    gamma, erf: fonksiyonlar"""

print ("Temel matematik fonksiyonlar ve sabitler:", mFonk)

x = 1.0
y = 0.0
print ("\n[0-->180] derece aras� atan(y/x) d�n���ml� tanjant a��lar�:")
while True:
    print ("derece (atan2 ({:.2f} / {:.2f}) = {:.2f}" . format (y, x, degrees (atan2 (y, x))) )
    x -=0.1
    if x >= 0: y +=0.1
    else: y -=0.1
    if x <= -1.0: break

print ("\nKayannoktal� 100.1**10 =", 100.1**10)
print ("Kayannoktal� 0.15**10 =", 0.15**10)

T = modf (100.123456789)
print ("\nK�s�rat ve tamsay� t�ple'si modf (100.123456789) =",  T[0], T[1] )