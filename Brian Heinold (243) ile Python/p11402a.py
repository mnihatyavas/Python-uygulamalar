# coding:iso-8859-9 Türkçe

class Örnek:
    def __init__(self, a, b): # Kurucu...
        self.a = a
        self.b = b

    def topla (self): return self.a + self.b # Sınıf metodları (ilk argümanları daima self'tir)...
    def çıkar (self): return self.a - self.b
    def çarp (self): return self.a * self.b
    def böl (self): return self.a / self.b
    def üs (self): return self.a ** self.b
    def kalan (self): return self.a % self.b
    def yüzde (self): return (self.a - self.b) * 100 / self.a

örn = Örnek (8, 6)
print ("8+6 =", örn.topla())
print ("8-6 =", örn.çıkar())
print ("8*6 =", örn.çarp())
print ("8/6 =", örn.böl())
print ("8**6 =", örn.üs())
print ("8%6 =", örn.kalan())
print ("yüzde(6/8) =", örn.yüzde())
