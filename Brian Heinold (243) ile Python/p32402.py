# coding:iso-8859-9 T�rk�e

from itertools import *

L = [''.join(�) for � in product ("abc", "12345")]
print ("('abc', '12345') dizge ikilisinin product/�r�nleri:", L, "\n�r�n say�s�:", len (L) )
#-------------------------------------------------------------------------------------------

print ("-"*75)
print ("\n3-for d�ng�l� [1->20] aras� x^2 + y^2 = z^2 e�itli�ini sa�layan de�erler:")
for x in range (1, 21):
    for y in range (1, 21):
        for z in range (1,21):
            if x**2+y**2==z**2: print ("(x,y,z)=(", x, ",", y, ",", z, ")", sep="")

print ("\nProduct ve tek-for d�ng�l� [1->20] aras� x^2 + y^2 = z^2 e�itli�ini sa�layan de�erler:")
X = range (1, 21)
for (x, y, z) in product (X, X, X):
    if x**2+y**2==z**2: print ("(x,y,z)=(", x, ",", y, ",", z, ")", sep="")

X = range (1, 21)
print ("\nProduct ve kapsaml� liste'yle [1->20] aras� x^2 + y^2 = z^2 e�itli�ini sa�layan (x,y,z) de�erleri:",
    [(x, y, z) for (x, y, z) in product (X, X, X) if x**2+y**2==z**2] )