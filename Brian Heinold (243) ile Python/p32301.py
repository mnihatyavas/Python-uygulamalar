# coding:iso-8859-9 Türkçe

def f(x): return x*x

kopya1 = f # Python fonksiyon nesneleri değişken adlarına kopyalanabilir...
kopya2 = kopya1

print ('f(3) =', f (3), '\nkopya1(3) =', kopya1(3), "\nkopya2(4) =", kopya2 (4))
#-------------------------------------------------------------------------------------------

def g(x): return x*x*x
def h(x): return x**0.5

L = [f, g, h]
print ("\nL[2](64) =", L[2](64), "\nL[0](5) =", L[0](5), "\nL[1](3) =", L[1](3) )
#-------------------------------------------------------------------------------------------

i = 0
while not(0 < i < 4):
    try: i = abs (int (eval (input ("\n1->3 arası bir tamsayı girin: "))))
    except Exception: i = 2

print ("L[", i-1, "](4) = ", L[i-1](4), sep="")
#-------------------------------------------------------------------------------------------

# 5 öğrencinin (ödev, ara, final) notlu tüpleli listesi...
L = [(45, 67, 52), (87, 75, 92), (62, 53, 79), (91, 85, 91), (42, 67, 35)]
print ("\n5 öğrencinin, ödev-ara-final notları (SIRASIZ):", L)
L.sort()
print ("\n5 öğrencinin, ödev-ara-final notları (ÖDEV'e göre artan SIRALI):", L)

def karşılaştır (x): return x[1]
L.sort (key=karşılaştır)
print ("\n5 öğrencinin, ödev-ara-final notları (ARASINAV'a göre artan SIRALI):", L)

def karşılaştır (x): return -x[2]
L.sort (key=karşılaştır)
print ("\n5 öğrencinin, ödev-ara-final notları (FİNAL'e göre AZALAN SIRALI):", L)
#-------------------------------------------------------------------------------------------

L = "Bu, kelimeleri dizgeden listeye dönüşen ve artan veya azalan sıralama yöntemidir.".split()
print ("\nOrijinal liste:", L)

L.sort()
print ("\nKelimeleri artan sıralı liste:", L)

L.reverse()
print ("\nKelimeleri azalan sıralı liste:", L)

L.sort (key=len)
print ("\nKelimeleri uzunluklarına göre artan sıralı liste:", L)

L.reverse()
print ("\nKelimeleri uzunluklarına göre azalan sıralı liste:", L)