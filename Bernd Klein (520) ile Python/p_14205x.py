# coding:iso-8859-9 T�rk�e
# p_14205x.py: Farkl� para birimlerini belirtilen birime yada yuroya �evirme ana/alt-�rne�i.

"""
p_14202x.py'deki Uzunluk s�n�f�n�n farkl� (uzunluk,"birim") s�n�f tip nesnelerini
ayn� birim alt�nda toparlamas� gibi, bu ParaBirimleri s�n�f� da farkl� �lke paralar�
aras�ndaki oranlara g�re �/yuro temeline �evrim yapmaktad�r.
"""

class ParaBirimleri:
    paralar =  {'CHF': 1.0821202355817312,
                   'CAD': 1.488609845538393,
                   'GBP': 0.8916546282920325,
                   'JPY': 114.38826536281809,
                   'EUR': 1.0,
                   'USD': 1.11123458162018,
                   'TL': 6.612356}
    def __init__ (self, de�er, birim="EUR"):
        self.de�er = de�er
        self.birim = birim
    def __str__ (self): return "{0:5.2f}".format (self.de�er) + " " + self.birim
    def __repr__ (self): return 'ParaBirimleri (' + str (self.de�er) + ', "' + self.birim + '")'
    def �evir (self, yeniBirim): # ParaBirimleri nesnesi self.birim'den yeniBirim'e �evrilir...
        self.de�er = (self.de�er / ParaBirimleri.paralar [self.birim] * ParaBirimleri.paralar [yeniBirim])
        self.birim = yeniBirim
    def __add__ (self, di�er): # Di�er ilk nesne birimine, belirtilmemi�se yuro'ya �evrilerek eklenir...
        if type (di�er) == int or type (di�er) == float: x = (di�er * ParaBirimleri.paralar[self.birim])
        else: x = (di�er.de�er / ParaBirimleri.paralar[di�er.birim] * ParaBirimleri.paralar[self.birim]) 
        return ParaBirimleri (x + self.de�er, self.birim)
    def __iadd__ (self, di�er): # __add__ gibidir, ancak increment/�steekleme yapar...
        if type (di�er) == int or type (di�er) == float: x = (di�er * ParaBirimleri.paralar[self.birim])
        else: x = (di�er.de�er / ParaBirimleri.paralar[di�er.birim] * ParaBirimleri.paralar[self.birim])
        self.de�er += x
        return self
    def __radd__ (self, di�er): # self+di�er veya di�er+self yapar...
        sonu� = self + di�er
        if self.birim != "EUR": sonu�.�evir ("EUR")
        return sonu�
    # __sub__, __isub__ and __rsub__ toplama gibi ��karma da yap�labilir...
    def __mul__ (self, di�er): # Skalar int-float para de�erleri �arp�m�n� yapar...
        if type (di�er) == int or type (di�er) == float: return ParaBirimleri (self.de�er * di�er, self.birim)
        else: raise TypeError ("Desteklenmeyen i�lemci tipi * ParaBirimleri ve " + type (di�er).__name__)
    def __rmul__ (self, di�er): return self.__mul__ (di�er)
    def __imul__ (self, di�er):
        if type (di�er) == int or type (di�er) == float:
            self.de�er *= di�er
            return self
        else: raise TypeError ("Desteklenmeyen i�lemci tipi * ParaBirimleri ve " + type (di�er).__name__)


if __name__ == "__main__":
    x = ParaBirimleri (10, "USD")
    y = ParaBirimleri (11)
    z = ParaBirimleri (12.34, "JPY")
    z += 7.8 + x + y + 255
    print ("12.34JPY + 7.8EUR + 10USD + 11EUR + 255EUR =", z)

    liste = [ParaBirimleri (10, "USD"), ParaBirimleri (11), ParaBirimleri (12.34, "JPY"), ParaBirimleri (12.34, "CAD"), ParaBirimleri (85.68, "TL")]

    z = sum (liste)

    print ("10USD + 11EUR + 12.23JPY + 12.34CAD + 85.68TL =", z)



"""��kt�:
>python p_14205x.py
12.34JPY + 7.8EUR + 10USD + 11EUR + 255EUR = 32361.23 JPY
10USD + 11EUR + 12.23JPY + 12.34CAD + 85.68TL = 41.35 EUR
"""