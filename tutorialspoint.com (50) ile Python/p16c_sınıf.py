# coding:iso-8859-9 T�rk�e

class S�n�f:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__ (self): # Program sonlan�rken otomatik olarak �al��t�r�l�r...
        s�n�f_ad� = self.__class__.__name__
        print (s�n�f_ad�, "�mha edildi.")
