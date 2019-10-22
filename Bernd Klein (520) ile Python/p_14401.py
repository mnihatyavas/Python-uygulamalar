# coding:iso-8859-9 T�rk�e
# p_14401.py: S�n�f init de�i�ken ve s�n�rs�z �zellikleri slot/yar�k'la s�n�rlama �rne�i.

class A(): pass

a = A()
a.x = 66
a.y = "dinamik yarat�lan �zellik"

print (a.x, a.y)
print (a.__dict__)
print (a.__dict__["x"], a.__dict__ ["y"])
#-----------------------------------------------------------------------------------------------

class Y():
    #__slots__ = ['de�er']
    def __init__ (self, d): self.de�er = d

print()
a = Y (57)
a.x = 66
a.y = "Dinamik �zellik m�mk�n"
a.z = "S�n�rs�z �zellik eklenebilir"

print (a.de�er, a.x, a.y, a.z)
print (a.__dict__)
#-----------------------------------------------------------------------------------------------

class Y():
    __slots__ = ['de�er1', "de�er2", "de�er3"]
    def __init__ (self, d1, d2, d3):
        self.de�er1 = d1
        self.de�er2 = d2
        self.de�er3 = d3

print()
a = Y(1957, "M.Nihat Yava�", "Ye�ilyurt-Malatya")
print (a.de�er1, a.de�er2, a.de�er3)

a.de�er1 = 2019
a.de�er2 = "Statik �zellik m�mk�n"
a.de�er3 = "Ancak mevcut s�n�rl� 3 �zellik kullan�labilir"
print (a.de�er1, a.de�er2, a.de�er3)

print()
try: a.x = 1
except Exception as ist: print (ist)
try: a.y = "__slots__ (yar�klar) listesinde tan�ml� olmayan �zelli�i reddeder"
except Exception as ist: print (ist)



"""��kt�:
>python p_14401.py
66 dinamik yarat�lan �zellik
{'x': 66, 'y': 'dinamik yarat�lan �zellik'}
66 dinamik yarat�lan �zellik

57 66 Dinamik �zellik m�mk�n S�n�rs�z �zellik eklenebilir
{'de�er': 57, 'x': 66, 'y': 'Dinamik �zellik m�mk�n', 'z': 'S�n�rs�z �zellik eklenebilir'}

1957 M.Nihat Yava� Ye�ilyurt-Malatya
2019 Statik �zellik m�mk�n Ancak mevcut s�n�rl� 3 �zellik kullan�labilir

'Y' object has no attribute 'x'
'Y' object has no attribute 'y'
"""