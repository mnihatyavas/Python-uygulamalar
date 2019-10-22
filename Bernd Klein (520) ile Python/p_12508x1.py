# coding:iso-8859-9 T�rk�e
# p_12508x1.py: Dekorat�r ve ambalaj� ana-programa �ncelleyen i�i�e fonksiyon alt-�rne�i.

def selam (fonk):
    def ambalaj (x):
        """ Bu, selam dekorat�r�n�n fonksiyon ambalaj�d�r. """
        print ("Merhaba, " + fonk.__name__ + " mesaj�n�z: ")
        return fonk (x)
    return ambalaj
