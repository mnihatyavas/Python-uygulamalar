# coding:iso-8859-9 T�rk�e
# p_14702.py: Ayn� tip d�n��l� metas�n�f ve normal s�n�f nesnelerinin e�itli�i kar��la�t��mas� �rne�i.

class Singleton (type):
    _tipler = {}
    def __call__ (s�n�f, *arg�manlar, **kwarg�manlar):
        if s�n�f not in s�n�f._tipler: s�n�f._tipler [s�n�f] = super (Singleton, s�n�f).__call__ (*arg�manlar, **kwarg�manlar)
        return s�n�f._tipler [s�n�f]

class SingletonS�n�f� (metaclass=Singleton): pass
class NormalS�n�f(): pass

x = SingletonS�n�f�()
y = SingletonS�n�f�()
print ("Metas�n�f tiplemeli Singleton s�n�f nesneleri i�in: x==y?", x == y)

x = NormalS�n�f()
y = NormalS�n�f()
print ("Normal s�n�f nesneleri i�in: x==y?", x == y)
print ("-"*62)
#--------------------------------------------------------------------------------------------------

class Singleton (object):
    _tip = None
    def __new__ (s�n�f, *arg�manlar, **kwarg�manlar):
        if not s�n�f._tip: s�n�f._tip = object.__new__ (s�n�f, *arg�manlar, **kwarg�manlar)
        return s�n�f._tip

class SingletonS�n�f� (Singleton): pass
class NormalS�n�f(): pass

x = SingletonS�n�f�()
y = SingletonS�n�f�()
print ("Normal Singleton s�n�f nesneleri i�in: x==y?", x == y)

x = NormalS�n�f()
y = NormalS�n�f()
print ("Normal s�n�f nesneleri i�in: x==y?", x == y)



"""��kt�:
>python p_14702.py
Metas�n�f tiplemeli Singleton s�n�f nesneleri i�in: x==y? True
Normal s�n�f nesneleri i�in: x==y? False
--------------------------------------------------------------
Normal Singleton s�n�f nesneleri i�in: x==y? True
Normal s�n�f nesneleri i�in: x==y? False
"""