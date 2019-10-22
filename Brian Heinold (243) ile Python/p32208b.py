# coding:iso-8859-9 T�rk�e

from os import urandom
from math import log

def tekrars�zTesad�fi (a,b):
    x = urandom (int (log (b - a + 1) / log (256)) + 1)
    toplam = 0
    for (i, y) in enumerate (x): toplam += y * (2**i)
    return toplam % (b - a + 1) + a

print ("Urandom ile tekrars�z tesad�fi say� �retimi:", tekrars�zTesad�fi (-500, 500) )
print ([tekrars�zTesad�fi (-500, 500) for i in range (12)] )