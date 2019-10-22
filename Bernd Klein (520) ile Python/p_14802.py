# coding:iso-8859-9 Türkçe
# p_14802.py: @Dekoratörlü ve atamalı fonksiyonla çağrı sayısı tesbiti örneği.

def sayaçMetodu (fonk):
    def yardımcı (*argümanlar, **kwargümanlar):
        yardımcı.çağrı += 1
        return fonk (*argümanlar, **kwargümanlar)
    yardımcı.çağrı = 0
    yardımcı.__name__= fonk.__name__
    return yardımcı

@sayaçMetodu # Dekoratörlü...
def f(): pass

print ("Dekoratörlü:")
print (f.çağrı)

for _ in range (10): f()
print (f.çağrı)
#------------------------------------------------------------------------------------------------------

def fnk(): pass # Dekoratörsüz...
f = sayaçMetodu (fnk)

print ("\nDekoratörsüz:")
print (f.çağrı)

for i in range (10): f()
print (f.çağrı)



"""Çıktı:
>python p_14802.py
Dekoratörlü:
0
10

Dekoratörsüz:
0
10
"""