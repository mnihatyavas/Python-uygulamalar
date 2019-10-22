# coding:iso-8859-9 Türkçe
# p_13902.py: Genel init değişkenini normal, @dekoratörlü ve mutator'la özel yapma örneği.

class P:
    def __init__ (self, x): self.xKoy (x)
    def xKoy (self, x):
        if x < 0: self.__x = 0
        elif x > 1000: self.__x = 1000
        else: self.__x = x
    def xAl (self): return self.__x

print ("xKoy() ve xAl() metodlarıyla x geneli (0->1000 kontrollu) __x özel yapma :")

p1 = P (1001)
print (p1.xAl() )
p2 = P (15)
print (p2.xAl() )
p3 = P (-1)
print (p3.xAl() )
print ("-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

class P:
    def __init__ (self, x): self.x = x

    @property
    def fonk (self): return self.__x # Özelleştirilen sonucu döndürür...

    @fonk.setter # property nesnesi setter/getter özelliğine sahiptir...
    def x (self, değer):
        if değer < 0: self.__x = 0
        elif değer > 1000: self.__x = 1000
        else: self.__x = değer

print ("@property ve @fonk.setter dekoratörleriyle x geneli (0->1000 kontrollu) __x özel yapma:")

p1 = P (1001)
print (p1.x)
p2 = P (15)
print (p2.x)
p3 = P (-1)
print (p3.x)
print ("-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

class P:
    def __init__ (self, x): self.xKoy (x)
    def __xAl (self): return self.__x
    def xKoy (self, x):
        if x < 0: self.__x = 0
        elif x > 1000: self.__x = 1000
        else: self.__x = x
    x = property (__xAl, xKoy) # Mutator/değiştirici koy-al özellik çifti...


print ("Dekoratörsüz x geneli (0->1000 kontrollu) __x özel yapma:")

p1 = P (1001)
print (p1.x)
p2 = P (15)
print (p2.x)
p3 = P (-1)
print (p3.x)



"""Çıktı:
>python p_13902.py
xKoy() ve xAl() metodlarıyla x geneli (0->1000 kontrollu) __x özel yapma :
1000
15
0
---------------------------------------------------------------------------

@property ve @fonk.setter dekoratörleriyle x geneli (0->1000 kontrollu) __x özel yapma:
1000
15
0
---------------------------------------------------------------------------

Dekoratörsüz x geneli (0->1000 kontrollu) __x özel yapma:
1000
15
0
"""