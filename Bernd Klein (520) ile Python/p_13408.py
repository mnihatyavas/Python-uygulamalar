# coding:iso-8859-9 Türkçe
# p_13408.py: for-yield ve yield-from'la aynı üretimi örneği.

def üreteç1():
    for krk in "Python": yield krk
    for i in range (5): yield i

def üreteç2():
    yield from "Python"
    yield from range (5)

# Her iki üreteç de aynıdır...
x1 = üreteç1()
x2 = üreteç2()

print ("üreteç1: ", end="")
for x in x1: print (x, end="-")

print ("\nüreteç2: ", end="")
for x in x2: print (x, end="-")
print ("\n", "-"*75, "\n", sep="")
#-------------------------------------------------------------------------------------------------

def şehirler():
    for şehir in ["Ankara", "İstanbul", "İzmir", "Bursa", "Mersin"]: yield şehir

def kareler():
    for sayı in range (10): yield sayı ** 2

def birleşik_üreteç():
    for şehir in şehirler(): yield şehir
    for sayı in kareler(): yield sayı

def ayrık_üreteç():
    yield from şehirler()
    yield from kareler()

liste1 = [eleman for eleman in birleşik_üreteç()]
liste2 = [eleman for eleman in ayrık_üreteç()]

print ([ş for ş in şehirler()] )
print ([k for k in kareler()] )

print()
print (liste1)
print (liste2)

print ("\nListe1 ile Liste2 eşit mi? ", end="")
print (liste1 == liste2)
print ("-"*75, "\n", sep="")
#--------------------------------------------------------------------------------------------

def üreteç():
    yield 1
    yield 5
    yield 27
    return 42

def temsilci():
    x = yield from üreteç()
    print (x)
    print (x)
    print (x)

print ("return'siz yield'leri verir:")
for x in üreteç(): print (x)

print ("\nyield'leri ve tekrarlı return'ü verir:")
for x in temsilci(): print (x)

"""Çıktı:
>python p_13408.py
üreteç1: P-y-t-h-o-n-0-1-2-3-4-
üreteç2: P-y-t-h-o-n-0-1-2-3-4-
---------------------------------------------------------------------------

['Ankara', 'İstanbul', 'İzmir', 'Bursa', 'Mersin']
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

['Ankara', 'İstanbul', 'İzmir', 'Bursa', 'Mersin', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
['Ankara', 'İstanbul', 'İzmir', 'Bursa', 'Mersin', 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Liste1 ile Liste2 eşit mi? True
---------------------------------------------------------------------------

return'siz yield'leri verir:
1
5
27

yield'leri ve tekrarlı return'ü verir:
1
5
27
42
42
42
"""