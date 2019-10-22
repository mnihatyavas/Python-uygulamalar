# coding:iso-8859-9 Türkçe
# p_13901.py: Private/özel init değişkenlerine al/koy metodu gerekirken, genel'le sınıf.özellik işlemi örneği.

class P:
    def __init__ (self, x): self.__x = x # __x: private/özel...
    def xAl (self): return self.__x
    def xKoy (self, x): self.__x = x

print ("__x: özel")

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



"""Çıktı:
>python p_13901.py
__x: özel
p1.xAl(): 42
p1.xAl(): 4758
---------------------------------------------------------------------------

x: genel
p1.x: 42
p1.x: 4758
"""