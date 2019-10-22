# coding:iso-8859-9 T�rk�e
# p_12002.py: �oklu ve ilk de�erli fonksiyon parametrelerine arg�manlar aktarma �rne�i.

from random import randint, random

def Selam (isim = "ahali"):
    """ Bu bir selamlama fasl� fonksiyonudur... """
    return "Selamlar olsun ey " + isim + "!.."

print (Selam ("Song�l Yava� G�kt�rk") )
print (Selam() )
print (Selam ("M.Nihat Yava�") )

print ("\nFonksiyonun ilk yorumu:", Selam.__doc__)
#------------------------------------------------------------------------------------------------------

def topla (a, b, c=0, d=0): return a+b+c+d

a = randint (0, 100) + random()
b =  randint (0, 100) + random()
print ("\n2 say�n�n toplam�: a={:.2f}, b={:.2f}, toplam={:.2f}" .format (a, b, topla (a, b)) )

x =  randint (0, 100) + random()
print ("3 say�n�n toplam�: a={:.2f}, b={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, x, topla (a, b, d=x)) )

y =  randint (0, 100) + random()
print ("4 say�n�n toplam�: a={:.2f}, b={:.2f}, c={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, y, x, topla (a, b, d=x, c=y)) )

print ("4 say�n�n toplam�: a={:.2f}, b={:.2f}, c={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, y, x, topla (a, b, y, x)) )


"""��kt�:
>python p_12002.py
Selamlar olsun ey Song�l Yava� G�kt�rk!..
Selamlar olsun ey ahali!..
Selamlar olsun ey M.Nihat Yava�!..

Fonksiyonun ilk yorumu:  Bu bir selamlama fasl� fonksiyonudur...

2 say�n�n toplam�: a=72.89, b=71.59, toplam=144.48
3 say�n�n toplam�: a=72.89, b=71.59, d=76.81, toplam=221.30
4 say�n�n toplam�: a=72.89, b=71.59, c=23.40, d=76.81, toplam=244.69
4 say�n�n toplam�: a=72.89, b=71.59, c=23.40, d=76.81, toplam=244.69
"""