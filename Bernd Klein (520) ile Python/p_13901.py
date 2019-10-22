# coding:iso-8859-9 T�rk�e
# p_13901.py: Private/�zel init de�i�kenlerine al/koy metodu gerekirken, genel'le s�n�f.�zellik i�lemi �rne�i.

class P:
    def __init__ (self, x): self.__x = x # __x: private/�zel...
    def xAl (self): return self.__x
    def xKoy (self, x): self.__x = x

print ("__x: �zel")

p1 = P (42)
p2 = P (4711)
print ("p1.xAl():", p1.xAl() )

p1.xKoy (47)
p1.xKoy (p1.xAl() + p2.xAl() )
print ("p1.xAl():", p1.xAl() )
print ("-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

class P:
    def __init__ (self, x): self.x = x # x: public/genel (koy->al gerekmiyor)...

print ("x: genel")

p1 = P (42)
p2 = P (4711)
print ("p1.x:", p1.x)

p1.x = 47
p1.x = p1.x + p2.x
print ("p1.x:", p1.x)



"""��kt�:
>python p_13901.py
__x: �zel
p1.xAl(): 42
p1.xAl(): 4758
---------------------------------------------------------------------------

x: genel
p1.x: 42
p1.x: 4758
"""