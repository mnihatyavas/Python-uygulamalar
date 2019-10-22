# coding:iso-8859-9 T�rk�e

class Vekt�r:
    def __init__ (self, a, b): # Kurucu...
        self.a = a
        self.b = b

    def __str__ (self): # Vekt�r print 'lerinin otomatik dizge d�n��t�r�c� metodu...
        return 'Vekt�r (%.2f, %.2f)' % (self.a, self.b)

    def __add__ (self, di�er): # Vekt�r toplam�n�n otomatik i�leme metodu...
        return Vekt�r (self.a + di�er.a, self.b + di�er.b)

v1 = Vekt�r (2,10)
v2 = Vekt�r (5, -2)
print ("�ki vekt�r�n toplam�:", (v1 + v2))
print ("�ki vekt�r�n toplam�:", (Vekt�r (3, -21)  + Vekt�r (-35.76, 42.98)))
