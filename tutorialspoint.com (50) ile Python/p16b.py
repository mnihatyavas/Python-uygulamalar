# coding:iso-8859-9 T�rk�e
# Python 3 - Object Oriented

class S�n�f:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__ (self): # Program sonlan�rken otomatik olarak �al��t�r�l�r...
        s�n�f_ad� = self.__class__.__name__
        print (s�n�f_ad�, "�mha edildi.")

nesne1 = S�n�f()
nesne2 = nesne1
nesne3 = nesne1

print (id (nesne1), id (nesne2), id (nesne3));   # Nesne id kimlik referans numaralar�...

del nesne1
del nesne2
del nesne3
