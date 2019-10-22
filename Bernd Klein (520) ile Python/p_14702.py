# coding:iso-8859-9 Türkçe
# p_14702.py: Aynı tip dönüşlü metasınıf ve normal sınıf nesnelerinin eşitliği karşılaştışması örneği.

class Singleton (type):
    _tipler = {}
    def __call__ (sınıf, *argümanlar, **kwargümanlar):
        if sınıf not in sınıf._tipler: sınıf._tipler [sınıf] = super (Singleton, sınıf).__call__ (*argümanlar, **kwargümanlar)
        return sınıf._tipler [sınıf]

class SingletonSınıfı (metaclass=Singleton): pass
class NormalSınıf(): pass

x = SingletonSınıfı()
y = SingletonSınıfı()
print ("Metasınıf tiplemeli Singleton sınıf nesneleri için: x==y?", x == y)

x = NormalSınıf()
y = NormalSınıf()
print ("Normal sınıf nesneleri için: x==y?", x == y)
print ("-"*62)
#--------------------------------------------------------------------------------------------------

class Singleton (object):
    _tip = None
    def __new__ (sınıf, *argümanlar, **kwargümanlar):
        if not sınıf._tip: sınıf._tip = object.__new__ (sınıf, *argümanlar, **kwargümanlar)
        return sınıf._tip

class SingletonSınıfı (Singleton): pass
class NormalSınıf(): pass

x = SingletonSınıfı()
y = SingletonSınıfı()
print ("Normal Singleton sınıf nesneleri için: x==y?", x == y)

x = NormalSınıf()
y = NormalSınıf()
print ("Normal sınıf nesneleri için: x==y?", x == y)



"""Çıktı:
>python p_14702.py
Metasınıf tiplemeli Singleton sınıf nesneleri için: x==y? True
Normal sınıf nesneleri için: x==y? False
--------------------------------------------------------------
Normal Singleton sınıf nesneleri için: x==y? True
Normal sınıf nesneleri için: x==y? False
"""