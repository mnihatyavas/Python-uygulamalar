# coding:iso-8859-9 T�rk�e
# p_14803.py: Metas�n�f arg�manl� s�n�f nesnesi metodlar�n�n �a�r� say�lar� tesbiti �rne�i.

class Saya�MetoduS�n�f� (type): # Metas�n�f tipli...
    @staticmethod
    def saya�Metodu (fonk): # Metodun �a�r� say�s�n� raporlar...
        def yard�mc� (*a, **kwa):
            yard�mc�.�a�r� += 1
            return fonk (*a, **kwa)
        yard�mc�.�a�r� = 0
        yard�mc�.__name__= fonk.__name__
        return yard�mc�

    def __new__ (s�n�f, s�n�fAd�, s�perS�n�flar, �zellikS�zl���):
        for �z in �zellikS�zl���:
            if callable (�zellikS�zl��� [�z]) and not �z.startswith ("__"):
                �zellikS�zl��� [�z] = s�n�f.saya�Metodu (�zellikS�zl��� [�z])
        return type.__new__ (s�n�f, s�n�fAd�, s�perS�n�flar, �zellikS�zl���)

class A (metaclass=Saya�MetoduS�n�f�):
    def m1 (self):pass
    def m2 (self): pass


if __name__ == "__main__":
    x = A()
    print (x.m1.�a�r�, x.m2.�a�r�)

    x.m1()
    print (x.m1.�a�r�, x.m2.�a�r�)

    x.m1()
    x.m2()
    print (x.m1.�a�r�, x.m2.�a�r�)

    x = A()
    for _ in range (20): x.m1()
    for _ in range (10): x.m2()
    print (x.m1.�a�r�, x.m2.�a�r�)



"""��kt�:
>python p_14803.py
0 0
1 0
2 1
22 11
"""