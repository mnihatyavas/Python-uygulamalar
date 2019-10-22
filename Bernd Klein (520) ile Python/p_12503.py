# coding:iso-8859-9 Türkçe
# p_12503.py: İçiçe polinom katsayıları ve değişkenine argüman aktarma örneği.

def fonk1 (x):
    def fonk2 (y): return x**2 + y + 3 
    return fonk2 # Bir fonksiyonu geri döndürme...


print ("fonk1(2)(3) ==> fonk1(x)(y):", fonk1 (2) (3) )
print ("fonk1(3)(-15) ==> fonk1(x)(y):", fonk1 (3) (-15) )

nesne1 = fonk1 (2) # fonk1(x)
nesne2 = fonk1 (3) # fonk1(x)

print ("fonk1(2)(3):", nesne1 (3) ) # fonk1(x)(y)
print ("fonk1(3)(-15):", nesne2 (-15) ) # fonk1(x)(y)
print ("-"*70)
#------------------------------------------------------------------------------------------------------

from random import randint

def polinomKatsayıları (a, b, c):
    def polinomDeğişkeni (x): return a * x**2 + b * x + c
    return polinomDeğişkeni

a = randint (-10, 10); b = randint (-10, 10); c = randint (-10, 10)

katsayı = polinomKatsayıları (a, b, c)

print ("\na*x**2 + b*x + c formülünde: a={}, b={} ve c={} ise" .format (a, b, c))
for x in range (-5, 6, 1): print ("x={} için: sonuç={}'dir." .format (x, katsayı (x)) )
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def polinomKatsayıları2 (*katsayılar):
    def polinomDeğişkeni (x):
        sonuç = 0
        # katsayılar yukardaki fonksiyona göre ters, yani son katsayı ilk yüksek üslünün önünde...
        for üs, katsayı in enumerate (katsayılar): sonuç += katsayı * x**üs
        return sonuç
    return polinomDeğişkeni

p1 = polinomKatsayıları2 (1) # f = 1
p2 = polinomKatsayıları2 (1, 2) # f = 2*x + 1
p3  = polinomKatsayıları2 (1, 2, 3) # f = 3*x**2 + 2*x + 1
p4 = polinomKatsayıları2 (1, 2, 3, 4) # f = 4*x**3 + 3*x**2 + 2*x + 1
p5 = polinomKatsayıları2 (1, 2, 3, 4, 5) # f = 5*x**4 + 4*x**3 + 3*x**2 + 2*x + 1
p6 = polinomKatsayıları2 (1, 1, 1, 1, 1, 1) # f = x**5 + x**4 + x**3 + x**2 + x + 1

for x in range (-5, 6, 1): print ("x={} için: p1(x)={}, p2(x)={}, p3(x)={}, p4(x)={}, p5(x)={}, p6(x)={}" .format (x, p1 (x), p2 (x), p3 (x), p4 (x), p5 (x), p6 (x)) )



"""Çıktı:
>python p_12503.py
fonk1(2)(3) ==> fonk1(x)(y): 10
fonk1(3)(-15) ==> fonk1(x)(y): -3
fonk1(2)(3): 10
fonk1(3)(-15): -3
----------------------------------------------------------------------

a*x**2 + b*x + c formülünde: a=9, b=1 ve c=2 ise
x=-5 için: sonuç=222'dir.
x=-4 için: sonuç=142'dir.
x=-3 için: sonuç=80'dir.
x=-2 için: sonuç=36'dir.
x=-1 için: sonuç=10'dir.
x=0 için: sonuç=2'dir.
x=1 için: sonuç=12'dir.
x=2 için: sonuç=40'dir.
x=3 için: sonuç=86'dir.
x=4 için: sonuç=150'dir.
x=5 için: sonuç=232'dir.
---------------------------------------------------------------------------

x=-5 için: p1(x)=1, p2(x)=-9, p3(x)=66, p4(x)=-434, p5(x)=2691, p6(x)=-2604
x=-4 için: p1(x)=1, p2(x)=-7, p3(x)=41, p4(x)=-215, p5(x)=1065, p6(x)=-819
x=-3 için: p1(x)=1, p2(x)=-5, p3(x)=22, p4(x)=-86, p5(x)=319, p6(x)=-182
x=-2 için: p1(x)=1, p2(x)=-3, p3(x)=9, p4(x)=-23, p5(x)=57, p6(x)=-21
x=-1 için: p1(x)=1, p2(x)=-1, p3(x)=2, p4(x)=-2, p5(x)=3, p6(x)=0
x=0 için: p1(x)=1, p2(x)=1, p3(x)=1, p4(x)=1, p5(x)=1, p6(x)=1
x=1 için: p1(x)=1, p2(x)=3, p3(x)=6, p4(x)=10, p5(x)=15, p6(x)=6
x=2 için: p1(x)=1, p2(x)=5, p3(x)=17, p4(x)=49, p5(x)=129, p6(x)=63
x=3 için: p1(x)=1, p2(x)=7, p3(x)=34, p4(x)=142, p5(x)=547, p6(x)=364
x=4 için: p1(x)=1, p2(x)=9, p3(x)=57, p4(x)=313, p5(x)=1593, p6(x)=1365
x=5 için: p1(x)=1, p2(x)=11, p3(x)=86, p4(x)=586, p5(x)=3711, p6(x)=3906
"""