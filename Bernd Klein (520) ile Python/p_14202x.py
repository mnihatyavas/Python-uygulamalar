# coding:iso-8859-9 T�rk�e
# p_14202x.py: Farkl� birim (mm, sm, m, km, in�, feet, yarda ve mil) uzunluklar�n toplanmas� ana/alt-�rne�i.

class Uzunluk:
    __metrik = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
        "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144, "mi" : 1609.344}
    def __init__ (self, de�er, birim = "m" ):
        self.de�er = de�er
        self.birim = birim
    def metreye�evir (self): return self.de�er * Uzunluk.__metrik [self.birim]
    def __add__ (self, di�er):
        if type (di�er) == int or type (di�er) == float: uz = self.metreye�evir() + di�er
        else: uz = self.metreye�evir() + di�er.metreye�evir()
        return Uzunluk (uz / Uzunluk.__metrik [self.birim], self.birim)
    def __iadd__ (self, di�er):
        if type (di�er) == int or type (di�er) == float: uz = self.metreye�evir() + di�er
        else: uz = self.metreye�evir() + di�er.metreye�evir()
        self.de�er = uz / Uzunluk.__metrik [self.birim]
        return self
    def __radd__ (self, di�er): return Uzunluk.__add__ (self, di�er)
    def __str__ (self): return str (self.metreye�evir() )
    def __repr__ (self): return "Uzunluk (" + str (self.de�er) + ", '" + self.birim + "')"


if __name__ == "__main__":
    x = Uzunluk (4)
    print ("4m = ", x, " metre", sep="") # __str__ t�m de�erleri metre'ye �evirir...
    print ("4m =", repr (x) )

    y = Uzunluk (4.5, "yd") + Uzunluk (1)
    print ("\n4.5yd + 1m =", repr (y) ) # __repr__ t�m de�erleri ilk verili birime �evirir...
    print ("4.5yd + 1m =", y, "metre")

    z = Uzunluk (4.5, "in") + Uzunluk (1.6, "cm") + Uzunluk (0.15, "ft")
    print ("\n4.5in + 1.6cm + 0.15ft =", repr (z) )
    print ("4.5in + 1.6cm + 0.15ft =", z, "metre")



"""��kt�:
>python p_14202x.py
4m = 4 metre
4m = Uzunluk (4, 'm')

4.5yd + 1m = Uzunluk (5.593613298337708, 'yd')
4.5yd + 1m = 5.1148 metre

4.5in + 1.6cm + 0.15ft = Uzunluk (6.92992125984252, 'in')
4.5in + 1.6cm + 0.15ft = 0.17602 metre
"""