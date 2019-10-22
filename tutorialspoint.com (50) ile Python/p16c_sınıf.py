# coding:iso-8859-9 Türkçe

class Sınıf:
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__ (self): # Program sonlanırken otomatik olarak çalıştırılır...
        sınıf_adı = self.__class__.__name__
        print (sınıf_adı, "İmha edildi.")
