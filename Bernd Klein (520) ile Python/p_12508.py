# coding:iso-8859-9 T�rk�e
# p_12508.py: �a�r�lan dekorat�r fonksiyonun ad�, a��klamas� ve mod�l� �rne�i.

from p_12508x1 import selam

@selam
def f (x):
    """ Bu, sadece girilen say�ya 4 ekleyen sa�ma-sapan bir fonksiyon i�te... """
    print ("Arg�man�n�za d�rt ekledim:", x + 4)

f (1957)
print ("Fonksiyon ad�: " + f.__name__)
print ("D�k�man dizgesi: " + f.__doc__)
print ("Mod�l ad�: " + f.__module__)

print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------
from p_12508x2 import selam

@selam
def f (x):
    """ Bu, sadece girilen say�ya 5 ekleyen sa�ma-sapan bir fonksiyon i�te... """
    print ("Arg�man�n�za be� ekledim:", x + 5)


f (1957)
print ("Fonksiyon ad�: " + f.__name__)
print ("D�k�man dizgesi: " + f.__doc__)
print ("Mod�l ad�: " + f.__module__)

print ("-"*75, "\n")
#-------------------------------------------------------------------------------------------------------

from p_12508x3 import selam

@selam
def f (x):
    """ Bu, sadece girilen say�ya 6 ekleyen sa�ma-sapan bir fonksiyon i�te... """
    print ("Arg�man�n�za alt� ekledim:", x + 6)


f (1957)
print ("Fonksiyon ad�: " + f.__name__)
print ("D�k�man dizgesi: " + f.__doc__)
print ("Mod�l ad�: " + f.__module__)



"""��kt�:
** >python p_12508.py  ** TEKRAR **
Merhaba, f mesaj�n�z:
Arg�man�n�za d�rt ekledim: 1961
Fonksiyon ad�: ambalaj
D�k�man dizgesi:  Bu, selam dekorat�r�n�n fonksiyon ambalaj�d�r.
Mod�l ad�: p_12508x1
---------------------------------------------------------------------------

Merhaba, f mesaj�n�z:
Arg�man�n�za be� ekledim: 1962
Fonksiyon ad�: f
D�k�man dizgesi:  Bu, sadece girilen say�ya 5 ekleyen sa�ma-sapan bir fonksiyon i�te...
Mod�l ad�: __main__
---------------------------------------------------------------------------

Merhaba, f mesaj�n�z:
Arg�man�n�za alt� ekledim: 1963
Fonksiyon ad�: f
D�k�man dizgesi:  Bu, sadece girilen say�ya 6 ekleyen sa�ma-sapan bir fonksiyon i�te...
Mod�l ad�: __main__
"""
