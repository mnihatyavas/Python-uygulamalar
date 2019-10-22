# coding:iso-8859-9 T�rk�e
# p_12503.py: ��i�e polinom katsay�lar� ve de�i�kenine arg�man aktarma �rne�i.

def fonk1 (x):
    def fonk2 (y): return x**2 + y + 3 
    return fonk2 # Bir fonksiyonu geri d�nd�rme...


print ("fonk1(2)(3) ==> fonk1(x)(y):", fonk1 (2) (3) )
print ("fonk1(3)(-15) ==> fonk1(x)(y):", fonk1 (3) (-15) )

nesne1 = fonk1 (2) # fonk1(x)
nesne2 = fonk1 (3) # fonk1(x)

print ("fonk1(2)(3):", nesne1 (3) ) # fonk1(x)(y)
print ("fonk1(3)(-15):", nesne2 (-15) ) # fonk1(x)(y)
print ("-"*70)
#------------------------------------------------------------------------------------------------------

from random import randint

def polinomKatsay�lar� (a, b, c):
    def polinomDe�i�keni (x): return a * x**2 + b * x + c
    return polinomDe�i�keni

a = randint (-10, 10); b = randint (-10, 10); c = randint (-10, 10)

katsay� = polinomKatsay�lar� (a, b, c)

print ("\na*x**2 + b*x + c form�l�nde: a={}, b={} ve c={} ise" .format (a, b, c))
for x in range (-5, 6, 1): print ("x={} i�in: sonu�={}'dir." .format (x, katsay� (x)) )
print ("-"*75, "\n")
#------------------------------------------------------------------------------------------------------

def polinomKatsay�lar�2 (*katsay�lar):
    def polinomDe�i�keni (x):
        sonu� = 0
        # katsay�lar yukardaki fonksiyona g�re ters, yani son katsay� ilk y�ksek �sl�n�n �n�nde...
        for �s, katsay� in enumerate (katsay�lar): sonu� += katsay� * x**�s
        return sonu�
    return polinomDe�i�keni

p1 = polinomKatsay�lar�2 (1) # f = 1
p2 = polinomKatsay�lar�2 (1, 2) # f = 2*x + 1
p3  = polinomKatsay�lar�2 (1, 2, 3) # f = 3*x**2 + 2*x + 1
p4 = polinomKatsay�lar�2 (1, 2, 3, 4) # f = 4*x**3 + 3*x**2 + 2*x + 1
p5 = polinomKatsay�lar�2 (1, 2, 3, 4, 5) # f = 5*x**4 + 4*x**3 + 3*x**2 + 2*x + 1
p6 = polinomKatsay�lar�2 (1, 1, 1, 1, 1, 1) # f = x**5 + x**4 + x**3 + x**2 + x + 1

for x in range (-5, 6, 1): print ("x={} i�in: p1(x)={}, p2(x)={}, p3(x)={}, p4(x)={}, p5(x)={}, p6(x)={}" .format (x, p1 (x), p2 (x), p3 (x), p4 (x), p5 (x), p6 (x)) )



"""��kt�:
>python p_12503.py
fonk1(2)(3) ==> fonk1(x)(y): 10
fonk1(3)(-15) ==> fonk1(x)(y): -3
fonk1(2)(3): 10
fonk1(3)(-15): -3
----------------------------------------------------------------------

a*x**2 + b*x + c form�l�nde: a=9, b=1 ve c=2 ise
x=-5 i�in: sonu�=222'dir.
x=-4 i�in: sonu�=142'dir.
x=-3 i�in: sonu�=80'dir.
x=-2 i�in: sonu�=36'dir.
x=-1 i�in: sonu�=10'dir.
x=0 i�in: sonu�=2'dir.
x=1 i�in: sonu�=12'dir.
x=2 i�in: sonu�=40'dir.
x=3 i�in: sonu�=86'dir.
x=4 i�in: sonu�=150'dir.
x=5 i�in: sonu�=232'dir.
---------------------------------------------------------------------------

x=-5 i�in: p1(x)=1, p2(x)=-9, p3(x)=66, p4(x)=-434, p5(x)=2691, p6(x)=-2604
x=-4 i�in: p1(x)=1, p2(x)=-7, p3(x)=41, p4(x)=-215, p5(x)=1065, p6(x)=-819
x=-3 i�in: p1(x)=1, p2(x)=-5, p3(x)=22, p4(x)=-86, p5(x)=319, p6(x)=-182
x=-2 i�in: p1(x)=1, p2(x)=-3, p3(x)=9, p4(x)=-23, p5(x)=57, p6(x)=-21
x=-1 i�in: p1(x)=1, p2(x)=-1, p3(x)=2, p4(x)=-2, p5(x)=3, p6(x)=0
x=0 i�in: p1(x)=1, p2(x)=1, p3(x)=1, p4(x)=1, p5(x)=1, p6(x)=1
x=1 i�in: p1(x)=1, p2(x)=3, p3(x)=6, p4(x)=10, p5(x)=15, p6(x)=6
x=2 i�in: p1(x)=1, p2(x)=5, p3(x)=17, p4(x)=49, p5(x)=129, p6(x)=63
x=3 i�in: p1(x)=1, p2(x)=7, p3(x)=34, p4(x)=142, p5(x)=547, p6(x)=364
x=4 i�in: p1(x)=1, p2(x)=9, p3(x)=57, p4(x)=313, p5(x)=1593, p6(x)=1365
x=5 i�in: p1(x)=1, p2(x)=11, p3(x)=86, p4(x)=586, p5(x)=3711, p6(x)=3906
"""