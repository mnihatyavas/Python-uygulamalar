# coding:iso-8859-9 T�rk�e
# p_14102a.py: �oklu mirasta miraslananlar�n �ncelikli s�ras� ve esge�en metod mevcudiyeti �rne�i.

class A: # veya "class A (object):"
    def metod (self): print ("A'n�n metod'u �a�r�ld�.")

class B (A): # B, A'y� miraslar...
    def metod (self): print ("B'n�n metod'u �a�r�ld�.") # A metodu override/esge�ilir...

class C (A): # C de A'y� miraslar...
    def metod (self): print ("C'n�n metod'u �a�r�ld�.") # A metodu override/esge�ilir...

class D (C, B): pass # �oklu miras (D ise B ve C'yi miraslar)...

x = D()
x.metod()
#------------------------------------------------------------------------------------------------

#del D
class D (B, C): pass # B miras�n� C miras�ndan �nceye de�i�tirdik...

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
    def metod (self): print ("B'n�n metod'u �a�r�ld�.")
class C (A):
    def metod (self): print ("C'n�n metod'u �a�r�ld�.")
class D (B, C):
    def metod (self): print ("D'n�n metod'u �a�r�ld�.")

x = D()
x.metod()



"""��kt�:
>python p_14102a.py
C'n�n metod'u �a�r�ld�.
B'n�n metod'u �a�r�ld�.
C'n�n metod'u �a�r�ld�.
D'n�n metod'u �a�r�ld�.
"""