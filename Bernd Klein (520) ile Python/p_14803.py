# coding:iso-8859-9 Türkçe
# p_14803.py: Metasınıf argümanlı sınıf nesnesi metodlarının çağrı sayıları tesbiti örneği.

class SayaçMetoduSınıfı (type): # Metasınıf tipli...
    @staticmethod
    def sayaçMetodu (fonk): # Metodun çağrı sayısını raporlar...
        def yardımcı (*a, **kwa):
            yardımcı.çağrı += 1
            return fonk (*a, **kwa)
        yardımcı.çağrı = 0
        yardımcı.__name__= fonk.__name__
        return yardımcı

    def __new__ (sınıf, sınıfAdı, süperSınıflar, özellikSözlüğü):
        for öz in özellikSözlüğü:
            if callable (özellikSözlüğü [öz]) and not öz.startswith ("__"):
                özellikSözlüğü [öz] = sınıf.sayaçMetodu (özellikSözlüğü [öz])
        return type.__new__ (sınıf, sınıfAdı, süperSınıflar, özellikSözlüğü)

class A (metaclass=SayaçMetoduSınıfı):
    def m1 (self):pass
    def m2 (self): pass


if __name__ == "__main__":
    x = A()
    print (x.m1.çağrı, x.m2.çağrı)

    x.m1()
    print (x.m1.çağrı, x.m2.çağrı)

    x.m1()
    x.m2()
    print (x.m1.çağrı, x.m2.çağrı)

    x = A()
    for _ in range (20): x.m1()
    for _ in range (10): x.m2()
    print (x.m1.çağrı, x.m2.çağrı)



"""Çıktı:
>python p_14803.py
0 0
1 0
2 1
22 11
"""