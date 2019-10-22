# coding:iso-8859-9 Türkçe

from math import *
mFonk = """
    sin, cos, tan: Trigonometrik fonksiyonlar
    asin, acos, atan: Ters trigonometrik fonksiyonlar
    atan2 (y,x): arctan (y / x)
    sinh, cosh, tanh: Hiperbolik fonksiyonlar
    asinh, acosh, atanh: Ters hiperbolik fonksiyonlar
    log, log10: doğal ln ve 10 temelli log
    log1p: log (1 + x)
    exp: e^x
    degrees, radians: Derece'den<-->radyan'a çevirir (180 derece = 1.pi)
    floor: floor (x) alt zemin tamsayı
    ceil: ceil (x) üst tavan tamsayı
    e, pi: e ve ? sabitleri
    factorial: factorial (x), 1*2*3*..*x
    modf (x): x'in tamsayısını ve küsüratını ayırır
    gamma, erf: fonksiyonlar"""

print ("Temel matematik fonksiyonlar ve sabitler:", mFonk)

x = 1.0
y = 0.0
print ("\n[0-->180] derece arası atan(y/x) dönüşümlü tanjant açıları:")
while True:
    print ("derece (atan2 ({:.2f} / {:.2f}) = {:.2f}" . format (y, x, degrees (atan2 (y, x))) )
    x -=0.1
    if x >= 0: y +=0.1
    else: y -=0.1
    if x <= -1.0: break

print ("\nKayannoktalı 100.1**10 =", 100.1**10)
print ("Kayannoktalı 0.15**10 =", 0.15**10)

T = modf (100.123456789)
print ("\nKüsürat ve tamsayı tüple'si modf (100.123456789) =",  T[0], T[1] )