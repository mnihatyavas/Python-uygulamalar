# coding:iso-8859-9 Türkçe
# p_14701.py: Argümanı normal ve meta sınıf olan sınıf nesnesi örneği.

class MetaSınıf (type): # "class MetaSınıf (object)" değil!..
    def __new__ (sınıf, sınıfAdı, süperSınıflar, özellikSözlüğü):
        print ("Sınıf adı: ", sınıfAdı)
        print ("Süper sınıflar: ", süperSınıflar)
        print ("Özellikler sözlüğü: ", özellikSözlüğü)
        return type.__new__ (sınıf, sınıfAdı, süperSınıflar, özellikSözlüğü)

class S: pass

class A (S, metaclass=MetaSınıf): pass

a = A()



"""Çıktı:
>python p_14701.py
Sınıf adı:  A
Süper sınıflar:  (<class '__main__.S'>,)
Özellikler sözlüğü:  {'__module__': '__main__', '__qualname__': 'A'}
"""