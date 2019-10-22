# coding:iso-8859-9 Türkçe
# p_14002.py: Miraslayan metodlarının miras metodlarını override/esgeçme örneği.

class Kişi:
    def __init__ (self, ad, soyad, yıl):
        self.ad = ad
        self.soyad = soyad
        self.yıl = yıl
    def __str__ (self): return self.ad + " " + self.soyad + ", " + str (2019 - self.yıl)


class Personel (Kişi): # Miras...
    def __init__ (self, ad, soyad, yıl, pno):
        super().__init__ (ad, soyad, yıl) # Override/esgeçme Kişi__init__
        self.pno = pno
    def __str__ (self): return super().__str__() + "; " +  self.pno # Override/esgeçme Kişi__str__


x1 = Kişi ("M.Nihat", "Yavaş", 1957)
x2 = Kişi ("Z.Nihal", "Candan", 1955)

y1 = Personel ("M.Ali", "Göktürk", 2010, "20190429-001")
y2 = Personel ("Atilla", "Göktürk", 1982, "20190429-051")

print ("Ad soyad ve yaş:", x1)
print ("Ad soyad ve yaş:", x2)
print()
print ("Ad soyad, yaş ve personel no:", y1)
print ("Ad soyad, yaş ve personel no:", y2)

"""Çıktı:
>python p_14002.py
Ad soyad ve yaş: M.Nihat Yavaş, 62
Ad soyad ve yaş: Z.Nihal Candan, 64

Ad soyad, yaş ve personel no: M.Ali Göktürk, 9; 20190429-001
Ad soyad, yaş ve personel no: Atilla Göktürk, 37; 20190429-051
"""