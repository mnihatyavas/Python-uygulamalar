# coding:iso-8859-9 Türkçe

from os import urandom
from math import log

def tekrarsızTesadüfi (a,b):
    x = urandom (int (log (b - a + 1) / log (256)) + 1)
    toplam = 0
    for (i, y) in enumerate (x): toplam += y * (2**i)
    return toplam % (b - a + 1) + a

print ("Urandom ile tekrarsız tesadüfi sayı üretimi:", tekrarsızTesadüfi (-500, 500) )
print ([tekrarsızTesadüfi (-500, 500) for i in range (12)] )