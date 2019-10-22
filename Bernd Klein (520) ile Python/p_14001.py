# coding:iso-8859-9 Türkçe
# p_14001.py: Bir sınıfın diğer bir sınıfa ait özellik ve metodları miraslaması örneği.

class Şahıs:
    def __init__ (self, adı, soyadı):
        self.ad = adı
        self.soyad = soyadı
    def adsoyadAl (self): return self.ad + " " + self.soyad

class İşgören (Şahıs): # inheritance/miras...
    def __init__ (self, adı, soyadı, bordroNosu):
        #Şahıs.__init__ (self, adı, soyadı)
        super().__init__ (adı, soyadı)
        #super (İşgören, self).__init__ (adı, soyadı)
        self.bordroNo = bordroNosu
    def işgörenAl (self): return self.adsoyadAl() + ", " +  self.bordroNo


x1 = Şahıs ("M.Nihat", "Yavaş")
x2 = Şahıs ("Z.Nihal", "Candan")

y1 = İşgören ("M.Ali", "Göktürk", "20190429-001")
y2 = İşgören ("Atilla", "Göktürk", "20190429-051")

print ("Ad soyad:", x1.adsoyadAl() )
print ("Ad soyad:", x2.adsoyadAl() )
print()
print ("Ad soyad ve personel no:", y1.işgörenAl() )
print ("Ad soyad ve personel no:", y2.işgörenAl() )

"""Çıktı:
>python p_14001.py
Ad soyad: M.Nihat Yavaş
Ad soyad: Z.Nihal Candan

Ad soyad ve personel no: M.Ali Göktürk, 20190429-001
Ad soyad ve personel no: Atilla Göktürk, 20190429-051
"""