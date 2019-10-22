# coding:iso-8859-9 T�rk�e
# p_12508x3.py: Dekorat�r ve ambalaj� @wraps'le ana-programa sonralayan i�i�e fonksiyon alt-�rne�i.

from functools import wraps

def selam (fonk):
    @wraps (fonk)
    def ambalaj (x):
        """ Bu, selam dekorat�r�n�n fonksiyon ambalaj�d�r. """
        print ("Merhaba, " + fonk.__name__ + " mesaj�n�z: ")
        return fonk (x)
    return ambalaj
