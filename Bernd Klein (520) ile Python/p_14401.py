# coding:iso-8859-9 Türkçe
# p_14401.py: Sınıf init değişken ve sınırsız özellikleri slot/yarık'la sınırlama örneği.

class A(): pass

a = A()
a.x = 66
a.y = "dinamik yaratılan özellik"

print (a.x, a.y)
print (a.__dict__)
print (a.__dict__["x"], a.__dict__ ["y"])
#-----------------------------------------------------------------------------------------------

class Y():
    #__slots__ = ['değer']
    def __init__ (self, d): self.değer = d

print()
a = Y (57)
a.x = 66
a.y = "Dinamik özellik mümkün"
a.z = "Sınırsız özellik eklenebilir"

print (a.değer, a.x, a.y, a.z)
print (a.__dict__)
#-----------------------------------------------------------------------------------------------

class Y():
    __slots__ = ['değer1', "değer2", "değer3"]
    def __init__ (self, d1, d2, d3):
        self.değer1 = d1
        self.değer2 = d2
        self.değer3 = d3

print()
a = Y(1957, "M.Nihat Yavaş", "Yeşilyurt-Malatya")
print (a.değer1, a.değer2, a.değer3)

a.değer1 = 2019
a.değer2 = "Statik özellik mümkün"
a.değer3 = "Ancak mevcut sınırlı 3 özellik kullanılabilir"
print (a.değer1, a.değer2, a.değer3)

print()
try: a.x = 1
except Exception as ist: print (ist)
try: a.y = "__slots__ (yarıklar) listesinde tanımlı olmayan özelliği reddeder"
except Exception as ist: print (ist)



"""Çıktı:
>python p_14401.py
66 dinamik yaratılan özellik
{'x': 66, 'y': 'dinamik yaratılan özellik'}
66 dinamik yaratılan özellik

57 66 Dinamik özellik mümkün Sınırsız özellik eklenebilir
{'değer': 57, 'x': 66, 'y': 'Dinamik özellik mümkün', 'z': 'Sınırsız özellik eklenebilir'}

1957 M.Nihat Yavaş Yeşilyurt-Malatya
2019 Statik özellik mümkün Ancak mevcut sınırlı 3 özellik kullanılabilir

'Y' object has no attribute 'x'
'Y' object has no attribute 'y'
"""