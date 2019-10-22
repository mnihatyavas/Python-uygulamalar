# coding:iso-8859-9 Türkçe
# p_14205x.py: Farklı para birimlerini belirtilen birime yada yuroya çevirme ana/alt-örneği.

"""
p_14202x.py'deki Uzunluk sınıfının farklı (uzunluk,"birim") sınıf tip nesnelerini
aynı birim altında toparlaması gibi, bu ParaBirimleri sınıfı da farklı ülke paraları
arasındaki oranlara göre €/yuro temeline çevrim yapmaktadır.
"""

class ParaBirimleri:
    paralar =  {'CHF': 1.0821202355817312,
                   'CAD': 1.488609845538393,
                   'GBP': 0.8916546282920325,
                   'JPY': 114.38826536281809,
                   'EUR': 1.0,
                   'USD': 1.11123458162018,
                   'TL': 6.612356}
    def __init__ (self, değer, birim="EUR"):
        self.değer = değer
        self.birim = birim
    def __str__ (self): return "{0:5.2f}".format (self.değer) + " " + self.birim
    def __repr__ (self): return 'ParaBirimleri (' + str (self.değer) + ', "' + self.birim + '")'
    def çevir (self, yeniBirim): # ParaBirimleri nesnesi self.birim'den yeniBirim'e çevrilir...
        self.değer = (self.değer / ParaBirimleri.paralar [self.birim] * ParaBirimleri.paralar [yeniBirim])
        self.birim = yeniBirim
    def __add__ (self, diğer): # Diğer ilk nesne birimine, belirtilmemişse yuro'ya çevrilerek eklenir...
        if type (diğer) == int or type (diğer) == float: x = (diğer * ParaBirimleri.paralar[self.birim])
        else: x = (diğer.değer / ParaBirimleri.paralar[diğer.birim] * ParaBirimleri.paralar[self.birim]) 
        return ParaBirimleri (x + self.değer, self.birim)
    def __iadd__ (self, diğer): # __add__ gibidir, ancak increment/üsteekleme yapar...
        if type (diğer) == int or type (diğer) == float: x = (diğer * ParaBirimleri.paralar[self.birim])
        else: x = (diğer.değer / ParaBirimleri.paralar[diğer.birim] * ParaBirimleri.paralar[self.birim])
        self.değer += x
        return self
    def __radd__ (self, diğer): # self+diğer veya diğer+self yapar...
        sonuç = self + diğer
        if self.birim != "EUR": sonuç.çevir ("EUR")
        return sonuç
    # __sub__, __isub__ and __rsub__ toplama gibi çıkarma da yapılabilir...
    def __mul__ (self, diğer): # Skalar int-float para değerleri çarpımını yapar...
        if type (diğer) == int or type (diğer) == float: return ParaBirimleri (self.değer * diğer, self.birim)
        else: raise TypeError ("Desteklenmeyen işlemci tipi * ParaBirimleri ve " + type (diğer).__name__)
    def __rmul__ (self, diğer): return self.__mul__ (diğer)
    def __imul__ (self, diğer):
        if type (diğer) == int or type (diğer) == float:
            self.değer *= diğer
            return self
        else: raise TypeError ("Desteklenmeyen işlemci tipi * ParaBirimleri ve " + type (diğer).__name__)


if __name__ == "__main__":
    x = ParaBirimleri (10, "USD")
    y = ParaBirimleri (11)
    z = ParaBirimleri (12.34, "JPY")
    z += 7.8 + x + y + 255
    print ("12.34JPY + 7.8EUR + 10USD + 11EUR + 255EUR =", z)

    liste = [ParaBirimleri (10, "USD"), ParaBirimleri (11), ParaBirimleri (12.34, "JPY"), ParaBirimleri (12.34, "CAD"), ParaBirimleri (85.68, "TL")]

    z = sum (liste)

    print ("10USD + 11EUR + 12.23JPY + 12.34CAD + 85.68TL =", z)



"""Çıktı:
>python p_14205x.py
12.34JPY + 7.8EUR + 10USD + 11EUR + 255EUR = 32361.23 JPY
10USD + 11EUR + 12.23JPY + 12.34CAD + 85.68TL = 41.35 EUR
"""