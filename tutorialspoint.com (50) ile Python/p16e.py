# coding:iso-8859-9 Türkçe

class Vektör:
    def __init__ (self, a, b): # Kurucu...
        self.a = a
        self.b = b

    def __str__ (self): # Vektör print 'lerinin otomatik dizge dönüştürücü metodu...
        return 'Vektör (%.2f, %.2f)' % (self.a, self.b)

    def __add__ (self, diğer): # Vektör toplamının otomatik işleme metodu...
        return Vektör (self.a + diğer.a, self.b + diğer.b)

v1 = Vektör (2,10)
v2 = Vektör (5, -2)
print ("İki vektörün toplamı:", (v1 + v2))
print ("İki vektörün toplamı:", (Vektör (3, -21)  + Vektör (-35.76, 42.98)))
