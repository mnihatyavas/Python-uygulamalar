# coding:iso-8859-9 T�rk�e
# p_14002.py: Miraslayan metodlar�n�n miras metodlar�n� override/esge�me �rne�i.

class Ki�i:
    def __init__ (self, ad, soyad, y�l):
        self.ad = ad
        self.soyad = soyad
        self.y�l = y�l
    def __str__ (self): return self.ad + " " + self.soyad + ", " + str (2019 - self.y�l)


class Personel (Ki�i): # Miras...
    def __init__ (self, ad, soyad, y�l, pno):
        super().__init__ (ad, soyad, y�l) # Override/esge�me Ki�i__init__
        self.pno = pno
    def __str__ (self): return super().__str__() + "; " +  self.pno # Override/esge�me Ki�i__str__


x1 = Ki�i ("M.Nihat", "Yava�", 1957)
x2 = Ki�i ("Z.Nihal", "Candan", 1955)

y1 = Personel ("M.Ali", "G�kt�rk", 2010, "20190429-001")
y2 = Personel ("Atilla", "G�kt�rk", 1982, "20190429-051")

print ("Ad soyad ve ya�:", x1)
print ("Ad soyad ve ya�:", x2)
print()
print ("Ad soyad, ya� ve personel no:", y1)
print ("Ad soyad, ya� ve personel no:", y2)

"""��kt�:
>python p_14002.py
Ad soyad ve ya�: M.Nihat Yava�, 62
Ad soyad ve ya�: Z.Nihal Candan, 64

Ad soyad, ya� ve personel no: M.Ali G�kt�rk, 9; 20190429-001
Ad soyad, ya� ve personel no: Atilla G�kt�rk, 37; 20190429-051
"""