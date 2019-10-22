# coding:iso-8859-9 Türkçe
# p_14102a.py: Çoklu mirasta miraslananların öncelikli sırası ve esgeçen metod mevcudiyeti örneği.

class A: # veya "class A (object):"
    def metod (self): print ("A'nın metod'u çağrıldı.")

class B (A): # B, A'yı miraslar...
    def metod (self): print ("B'nın metod'u çağrıldı.") # A metodu override/esgeçilir...

class C (A): # C de A'yı miraslar...
    def metod (self): print ("C'nın metod'u çağrıldı.") # A metodu override/esgeçilir...

class D (C, B): pass # Çoklu miras (D ise B ve C'yi miraslar)...

x = D()
x.metod()
#------------------------------------------------------------------------------------------------

#del D
class D (B, C): pass # B mirasını C mirasından önceye değiştirdik...

x = D()
x.metod()
#------------------------------------------------------------------------------------------------

#del B, D
class B (A): pass
class D (B, C): pass

x = D()
x.metod()
#------------------------------------------------------------------------------------------------

class B (A):
    def metod (self): print ("B'nın metod'u çağrıldı.")
class C (A):
    def metod (self): print ("C'nın metod'u çağrıldı.")
class D (B, C):
    def metod (self): print ("D'nın metod'u çağrıldı.")

x = D()
x.metod()



"""Çıktı:
>python p_14102a.py
C'nın metod'u çağrıldı.
B'nın metod'u çağrıldı.
C'nın metod'u çağrıldı.
D'nın metod'u çağrıldı.
"""