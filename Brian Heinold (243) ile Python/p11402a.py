# coding:iso-8859-9 T�rk�e

class �rnek:
    def __init__(self, a, b): # Kurucu...
        self.a = a
        self.b = b

    def topla (self): return self.a + self.b # S�n�f metodlar� (ilk arg�manlar� daima self'tir)...
    def ��kar (self): return self.a - self.b
    def �arp (self): return self.a * self.b
    def b�l (self): return self.a / self.b
    def �s (self): return self.a ** self.b
    def kalan (self): return self.a % self.b
    def y�zde (self): return (self.a - self.b) * 100 / self.a

�rn = �rnek (8, 6)
print ("8+6 =", �rn.topla())
print ("8-6 =", �rn.��kar())
print ("8*6 =", �rn.�arp())
print ("8/6 =", �rn.b�l())
print ("8**6 =", �rn.�s())
print ("8%6 =", �rn.kalan())
print ("y�zde(6/8) =", �rn.y�zde())
