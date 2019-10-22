# coding:iso-8859-9 Türkçe
# p_14202x.py: Farklı birim (mm, sm, m, km, inç, feet, yarda ve mil) uzunlukların toplanması ana/alt-örneği.

class Uzunluk:
    __metrik = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
        "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144, "mi" : 1609.344}
    def __init__ (self, değer, birim = "m" ):
        self.değer = değer
        self.birim = birim
    def metreyeÇevir (self): return self.değer * Uzunluk.__metrik [self.birim]
    def __add__ (self, diğer):
        if type (diğer) == int or type (diğer) == float: uz = self.metreyeÇevir() + diğer
        else: uz = self.metreyeÇevir() + diğer.metreyeÇevir()
        return Uzunluk (uz / Uzunluk.__metrik [self.birim], self.birim)
    def __iadd__ (self, diğer):
        if type (diğer) == int or type (diğer) == float: uz = self.metreyeÇevir() + diğer
        else: uz = self.metreyeÇevir() + diğer.metreyeÇevir()
        self.değer = uz / Uzunluk.__metrik [self.birim]
        return self
    def __radd__ (self, diğer): return Uzunluk.__add__ (self, diğer)
    def __str__ (self): return str (self.metreyeÇevir() )
    def __repr__ (self): return "Uzunluk (" + str (self.değer) + ", '" + self.birim + "')"


if __name__ == "__main__":
    x = Uzunluk (4)
    print ("4m = ", x, " metre", sep="") # __str__ tüm değerleri metre'ye çevirir...
    print ("4m =", repr (x) )

    y = Uzunluk (4.5, "yd") + Uzunluk (1)
    print ("\n4.5yd + 1m =", repr (y) ) # __repr__ tüm değerleri ilk verili birime çevirir...
    print ("4.5yd + 1m =", y, "metre")

    z = Uzunluk (4.5, "in") + Uzunluk (1.6, "cm") + Uzunluk (0.15, "ft")
    print ("\n4.5in + 1.6cm + 0.15ft =", repr (z) )
    print ("4.5in + 1.6cm + 0.15ft =", z, "metre")



"""Çıktı:
>python p_14202x.py
4m = 4 metre
4m = Uzunluk (4, 'm')

4.5yd + 1m = Uzunluk (5.593613298337708, 'yd')
4.5yd + 1m = 5.1148 metre

4.5in + 1.6cm + 0.15ft = Uzunluk (6.92992125984252, 'in')
4.5in + 1.6cm + 0.15ft = 0.17602 metre
"""