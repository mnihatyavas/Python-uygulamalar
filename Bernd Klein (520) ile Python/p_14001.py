# coding:iso-8859-9 T�rk�e
# p_14001.py: Bir s�n�f�n di�er bir s�n�fa ait �zellik ve metodlar� miraslamas� �rne�i.

class �ah�s:
    def __init__ (self, ad�, soyad�):
        self.ad = ad�
        self.soyad = soyad�
    def adsoyadAl (self): return self.ad + " " + self.soyad

class ��g�ren (�ah�s): # inheritance/miras...
    def __init__ (self, ad�, soyad�, bordroNosu):
        #�ah�s.__init__ (self, ad�, soyad�)
        super().__init__ (ad�, soyad�)
        #super (��g�ren, self).__init__ (ad�, soyad�)
        self.bordroNo = bordroNosu
    def i�g�renAl (self): return self.adsoyadAl() + ", " +  self.bordroNo


x1 = �ah�s ("M.Nihat", "Yava�")
x2 = �ah�s ("Z.Nihal", "Candan")

y1 = ��g�ren ("M.Ali", "G�kt�rk", "20190429-001")
y2 = ��g�ren ("Atilla", "G�kt�rk", "20190429-051")

print ("Ad soyad:", x1.adsoyadAl() )
print ("Ad soyad:", x2.adsoyadAl() )
print()
print ("Ad soyad ve personel no:", y1.i�g�renAl() )
print ("Ad soyad ve personel no:", y2.i�g�renAl() )

"""��kt�:
>python p_14001.py
Ad soyad: M.Nihat Yava�
Ad soyad: Z.Nihal Candan

Ad soyad ve personel no: M.Ali G�kt�rk, 20190429-001
Ad soyad ve personel no: Atilla G�kt�rk, 20190429-051
"""