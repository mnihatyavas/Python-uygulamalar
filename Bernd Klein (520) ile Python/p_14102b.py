# coding:iso-8859-9 Türkçe
# p_1402b.py: Miraslayanın mirasladıkları metodları sıra ve super() önceliğiyle esgeçmesi örneği.

class A:
    def metod (self): print ("A'nın metod'u çağrıldı.")
class B (A):
    def metod (self): print ("B'nın metod'u çağrıldı.")
class C (A):
    def metod (self): print ("C'nın metod'u çağrıldı.")
class D (B, C):
    def metod (self): print ("D'nın metod'u çağrıldı.")

x = D()

A.metod (object)
B.metod (x)
C.metod (x)
D.metod (object)
#------------------------------------------------------------------------------------------------

class D (B, C):
    def metod (self):
        print ("D'nın metod'u çağrıldı.")
        A.metod (self)
        B.metod (self)
        C.metod (self)

print()
x = D()
x.metod()
#------------------------------------------------------------------------------------------------

class B (A):
    def metod (self):
        print ("B'nın metod'u çağrıldı.")
        A.metod (self)
class C (A):
    def metod (self):
        print ("C'nın metod'u çağrıldı.")
        A.metod (self)
class D (B, C):
    def metod (self):
        print ("D'nın metod'u çağrıldı.")
        B.metod (self)
        C.metod (self)

print()
x = D()

x.metod() # Ancak A metodu, hem B hem de C'den yani 2 kez çağrılır...
#------------------------------------------------------------------------------------------------

class B (A):
    def metod (self):
        print ("B'nın metod'u çağrıldı.")
        super().metod()
class C (A):
    def metod (self):
        print ("C'nın metod'u çağrıldı.")
        super().metod()
class D (B, C):
    def metod (self):
        print ("D'nın metod'u çağrıldı.")
        super().metod() # Süper metodları sırasıyla B, C ve A olarak çağırır...

print()
x = D()

x.metod()
print ("-"*75)
#------------------------------------------------------------------------------------------------

class A:
    def __init__ (self): print ("A.__init__")
class B (A):
    def __init__ (self):
        print ("B.__init__")
        super().__init__() # süperler daha ziyade __init__ kurulurken yerleştirilir...
class C (A):
    def __init__ (self):
        print ("C.__init__")
        super().__init__()
class D (B, C):
    def __init__ (self):
        print ("D.__init__")
        super().__init__()

print ("\nD'yi başlatalım==>"); d = D()
print ("\nB'yi başlatalım==>"); b = B()
print ("\nC'yi başlatalım==>"); c = C()
print ("\nA'yı başlatalım==>"); a = A()



"""Çıktı:
>python p_14102b.py
A'nın metod'u çağrıldı.
B'nın metod'u çağrıldı.
C'nın metod'u çağrıldı.
D'nın metod'u çağrıldı.

D'nın metod'u çağrıldı.
A'nın metod'u çağrıldı.
B'nın metod'u çağrıldı.
C'nın metod'u çağrıldı.

D'nın metod'u çağrıldı.
B'nın metod'u çağrıldı.
A'nın metod'u çağrıldı.
C'nın metod'u çağrıldı.
A'nın metod'u çağrıldı.

D'nın metod'u çağrıldı.
B'nın metod'u çağrıldı.
C'nın metod'u çağrıldı.
A'nın metod'u çağrıldı.
---------------------------------------------------------------------------

D'yi başlatalım==>
D.__init__
B.__init__
C.__init__
A.__init__

B'yi başlatalım==>
B.__init__
A.__init__

C'yi başlatalım==>
C.__init__
A.__init__

A'yı başlatalım==>
A.__init__
"""