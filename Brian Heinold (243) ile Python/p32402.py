# coding:iso-8859-9 Türkçe

from itertools import *

L = [''.join(ü) for ü in product ("abc", "12345")]
print ("('abc', '12345') dizge ikilisinin product/ürünleri:", L, "\nÜrün sayısı:", len (L) )
#-------------------------------------------------------------------------------------------

print ("-"*75)
print ("\n3-for döngülü [1->20] arası x^2 + y^2 = z^2 eşitliğini sağlayan değerler:")
for x in range (1, 21):
    for y in range (1, 21):
        for z in range (1,21):
            if x**2+y**2==z**2: print ("(x,y,z)=(", x, ",", y, ",", z, ")", sep="")

print ("\nProduct ve tek-for döngülü [1->20] arası x^2 + y^2 = z^2 eşitliğini sağlayan değerler:")
X = range (1, 21)
for (x, y, z) in product (X, X, X):
    if x**2+y**2==z**2: print ("(x,y,z)=(", x, ",", y, ",", z, ")", sep="")

X = range (1, 21)
print ("\nProduct ve kapsamlı liste'yle [1->20] arası x^2 + y^2 = z^2 eşitliğini sağlayan (x,y,z) değerleri:",
    [(x, y, z) for (x, y, z) in product (X, X, X) if x**2+y**2==z**2] )