# coding:iso-8859-9 Türkçe
# p_12002.py: Çoklu ve ilk değerli fonksiyon parametrelerine argümanlar aktarma örneği.

from random import randint, random

def Selam (isim = "ahali"):
    """ Bu bir selamlama faslı fonksiyonudur... """
    return "Selamlar olsun ey " + isim + "!.."

print (Selam ("Songül Yavaş Göktürk") )
print (Selam() )
print (Selam ("M.Nihat Yavaş") )

print ("\nFonksiyonun ilk yorumu:", Selam.__doc__)
#------------------------------------------------------------------------------------------------------

def topla (a, b, c=0, d=0): return a+b+c+d

a = randint (0, 100) + random()
b =  randint (0, 100) + random()
print ("\n2 sayının toplamı: a={:.2f}, b={:.2f}, toplam={:.2f}" .format (a, b, topla (a, b)) )

x =  randint (0, 100) + random()
print ("3 sayının toplamı: a={:.2f}, b={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, x, topla (a, b, d=x)) )

y =  randint (0, 100) + random()
print ("4 sayının toplamı: a={:.2f}, b={:.2f}, c={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, y, x, topla (a, b, d=x, c=y)) )

print ("4 sayının toplamı: a={:.2f}, b={:.2f}, c={:.2f}, d={:.2f}, toplam={:.2f}" .format (a, b, y, x, topla (a, b, y, x)) )


"""Çıktı:
>python p_12002.py
Selamlar olsun ey Songül Yavaş Göktürk!..
Selamlar olsun ey ahali!..
Selamlar olsun ey M.Nihat Yavaş!..

Fonksiyonun ilk yorumu:  Bu bir selamlama faslı fonksiyonudur...

2 sayının toplamı: a=72.89, b=71.59, toplam=144.48
3 sayının toplamı: a=72.89, b=71.59, d=76.81, toplam=221.30
4 sayının toplamı: a=72.89, b=71.59, c=23.40, d=76.81, toplam=244.69
4 sayının toplamı: a=72.89, b=71.59, c=23.40, d=76.81, toplam=244.69
"""