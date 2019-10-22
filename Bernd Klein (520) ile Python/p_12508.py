# coding:iso-8859-9 Türkçe
# p_12508.py: Çağrılan dekoratör fonksiyonun adı, açıklaması ve modülü örneği.

from p_12508x1 import selam

@selam
def f (x):
    """ Bu, sadece girilen sayıya 4 ekleyen saçma-sapan bir fonksiyon işte... """
    print ("Argümanınıza dört ekledim:", x + 4)

f (1957)
print ("Fonksiyon adı: " + f.__name__)
print ("Döküman dizgesi: " + f.__doc__)
print ("Modül adı: " + f.__module__)

print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------
from p_12508x2 import selam

@selam
def f (x):
    """ Bu, sadece girilen sayıya 5 ekleyen saçma-sapan bir fonksiyon işte... """
    print ("Argümanınıza beş ekledim:", x + 5)


f (1957)
print ("Fonksiyon adı: " + f.__name__)
print ("Döküman dizgesi: " + f.__doc__)
print ("Modül adı: " + f.__module__)

print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

from p_12508x3 import selam

@selam
def f (x):
    """ Bu, sadece girilen sayıya 6 ekleyen saçma-sapan bir fonksiyon işte... """
    print ("Argümanınıza altı ekledim:", x + 6)


f (1957)
print ("Fonksiyon adı: " + f.__name__)
print ("Döküman dizgesi: " + f.__doc__)
print ("Modül adı: " + f.__module__)



"""Çıktı:
** >python p_12508.py  ** TEKRAR **
Merhaba, f mesajınız:
Argümanınıza dört ekledim: 1961
Fonksiyon adı: ambalaj
Döküman dizgesi:  Bu, selam dekoratörünün fonksiyon ambalajıdır.
Modül adı: p_12508x1
---------------------------------------------------------------------------

Merhaba, f mesajınız:
Argümanınıza beş ekledim: 1962
Fonksiyon adı: f
Döküman dizgesi:  Bu, sadece girilen sayıya 5 ekleyen saçma-sapan bir fonksiyon işte...
Modül adı: __main__
---------------------------------------------------------------------------

Merhaba, f mesajınız:
Argümanınıza altı ekledim: 1963
Fonksiyon adı: f
Döküman dizgesi:  Bu, sadece girilen sayıya 6 ekleyen saçma-sapan bir fonksiyon işte...
Modül adı: __main__
"""
