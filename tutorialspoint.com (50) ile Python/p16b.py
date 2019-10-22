# coding:iso-8859-9 Türkçe
# Python 3 - Object Oriented

class Sınıf:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__ (self): # Program sonlanırken otomatik olarak çalıştırılır...
        sınıf_adı = self.__class__.__name__
        print (sınıf_adı, "İmha edildi.")

nesne1 = Sınıf()
nesne2 = nesne1
nesne3 = nesne1

print (id (nesne1), id (nesne2), id (nesne3));   # Nesne id kimlik referans numaraları...

del nesne1
del nesne2
del nesne3
