# coding:iso-8859-9 T�rk�e
# p_13902.py: Genel init de�i�kenini normal, @dekorat�rl� ve mutator'la �zel yapma �rne�i.

class P:
    def __init__ (self, x): self.xKoy (x)
    def xKoy (self, x):
        if x < 0: self.__x = 0
        elif x > 1000: self.__x = 1000
        else: self.__x = x
    def xAl (self): return self.__x

print ("xKoy() ve xAl() metodlar�yla x geneli (0->1000 kontrollu) __x �zel yapma :")

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
    def fonk (self): return self.__x # �zelle�tirilen sonucu d�nd�r�r...

    @fonk.setter # property nesnesi setter/getter �zelli�ine sahiptir...
    def x (self, de�er):
        if de�er < 0: self.__x = 0
        elif de�er > 1000: self.__x = 1000
        else: self.__x = de�er

print ("@property ve @fonk.setter dekorat�rleriyle x geneli (0->1000 kontrollu) __x �zel yapma:")

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
    x = property (__xAl, xKoy) # Mutator/de�i�tirici koy-al �zellik �ifti...


print ("Dekorat�rs�z x geneli (0->1000 kontrollu) __x �zel yapma:")

p1 = P (1001)
print (p1.x)
p2 = P (15)
print (p2.x)
p3 = P (-1)
print (p3.x)



"""��kt�:
>python p_13902.py
xKoy() ve xAl() metodlar�yla x geneli (0->1000 kontrollu) __x �zel yapma :
1000
15
0
---------------------------------------------------------------------------

@property ve @fonk.setter dekorat�rleriyle x geneli (0->1000 kontrollu) __x �zel yapma:
1000
15
0
---------------------------------------------------------------------------

Dekorat�rs�z x geneli (0->1000 kontrollu) __x �zel yapma:
1000
15
0
"""