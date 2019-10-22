# coding:iso-8859-9 T�rk�e
# p_12508x2.py: Dekorat�r ve ambalaj� ana programa sonralayan i�i�e fonksiyon alt-�rne�i.

def selam (fonk):
    def ambalaj (x):
        """ Bu, selam dekorat�r�n�n fonksiyon ambalaj�d�r. """
        print ("Merhaba, " + fonk.__name__ + " mesaj�n�z: ")
        return fonk (x)
    ambalaj.__name__ = fonk.__name__
    ambalaj.__doc__ = fonk.__doc__
    ambalaj.__module__ = fonk.__module__
    return ambalaj
