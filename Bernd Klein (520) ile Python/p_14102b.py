# coding:iso-8859-9 T�rk�e
# p_1402b.py: Miraslayan�n miraslad�klar� metodlar� s�ra ve super() �nceli�iyle esge�mesi �rne�i.

class A:
    def metod (self): print ("A'n�n metod'u �a�r�ld�.")
class B (A):
    def metod (self): print ("B'n�n metod'u �a�r�ld�.")
class C (A):
    def metod (self): print ("C'n�n metod'u �a�r�ld�.")
class D (B, C):
    def metod (self): print ("D'n�n metod'u �a�r�ld�.")

x = D()

A.metod (object)
B.metod (x)
C.metod (x)
D.metod (object)
#------------------------------------------------------------------------------------------------

class D (B, C):
    def metod (self):
        print ("D'n�n metod'u �a�r�ld�.")
        A.metod (self)
        B.metod (self)
        C.metod (self)

print()
x = D()
x.metod()
#------------------------------------------------------------------------------------------------

class B (A):
    def metod (self):
        print ("B'n�n metod'u �a�r�ld�.")
        A.metod (self)
class C (A):
    def metod (self):
        print ("C'n�n metod'u �a�r�ld�.")
        A.metod (self)
class D (B, C):
    def metod (self):
        print ("D'n�n metod'u �a�r�ld�.")
        B.metod (self)
        C.metod (self)

print()
x = D()

x.metod() # Ancak A metodu, hem B hem de C'den yani 2 kez �a�r�l�r...
#------------------------------------------------------------------------------------------------

class B (A):
    def metod (self):
        print ("B'n�n metod'u �a�r�ld�.")
        super().metod()
class C (A):
    def metod (self):
        print ("C'n�n metod'u �a�r�ld�.")
        super().metod()
class D (B, C):
    def metod (self):
        print ("D'n�n metod'u �a�r�ld�.")
        super().metod() # S�per metodlar� s�ras�yla B, C ve A olarak �a��r�r...

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
        super().__init__() # s�perler daha ziyade __init__ kurulurken yerle�tirilir...
class C (A):
    def __init__ (self):
        print ("C.__init__")
        super().__init__()
class D (B, C):
    def __init__ (self):
        print ("D.__init__")
        super().__init__()

print ("\nD'yi ba�latal�m==>"); d = D()
print ("\nB'yi ba�latal�m==>"); b = B()
print ("\nC'yi ba�latal�m==>"); c = C()
print ("\nA'y� ba�latal�m==>"); a = A()



"""��kt�:
>python p_14102b.py
A'n�n metod'u �a�r�ld�.
B'n�n metod'u �a�r�ld�.
C'n�n metod'u �a�r�ld�.
D'n�n metod'u �a�r�ld�.

D'n�n metod'u �a�r�ld�.
A'n�n metod'u �a�r�ld�.
B'n�n metod'u �a�r�ld�.
C'n�n metod'u �a�r�ld�.

D'n�n metod'u �a�r�ld�.
B'n�n metod'u �a�r�ld�.
A'n�n metod'u �a�r�ld�.
C'n�n metod'u �a�r�ld�.
A'n�n metod'u �a�r�ld�.

D'n�n metod'u �a�r�ld�.
B'n�n metod'u �a�r�ld�.
C'n�n metod'u �a�r�ld�.
A'n�n metod'u �a�r�ld�.
---------------------------------------------------------------------------

D'yi ba�latal�m==>
D.__init__
B.__init__
C.__init__
A.__init__

B'yi ba�latal�m==>
B.__init__
A.__init__

C'yi ba�latal�m==>
C.__init__
A.__init__

A'y� ba�latal�m==>
A.__init__
"""