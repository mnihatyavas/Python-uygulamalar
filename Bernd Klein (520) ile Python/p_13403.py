# coding:iso-8859-9 Türkçe
# p_13403.py: yield-next fonksiyonda raise veya return istisna yönetimi örneği.

def üreteç1():
    yield 1
    yield 2
    yield 3
    raise StopIteration (42) # return, return 42, raise, raise 42
    yield 4
    yield 5

ürün = üreteç1()

print ("raise'li üreteç elementleri:")

try:
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
except Exception as ist: print ("HATA:", ist, "(yield sonu veya raise/return'e rastlanıldı...)")
#---------------------------------------------------------------------------------------------

def üreteç2():
    yield 1
    yield 2
    yield 3
    raise #return 42
    yield 4
    yield 5

ürün = üreteç2()

print ("\nreturn'lü üreteç elementleri:")

try:
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
    print ("-->Ürün:", next (ürün) )
except: print ("HATA: yield sonu veya raise/return'e rastlanıldı...")

"""Çıktı:
>python p_13403.py
raise'li üreteç elementleri:
-->Ürün: 1
-->Ürün: 2
-->Ürün: 3
HATA: generator raised StopIteration (yield sonu veya raise/return'e rastlanıldı...)

return'lü üreteç elementleri:
-->Ürün: 1
-->Ürün: 2
-->Ürün: 3
HATA: yield sonu veya raise/return'e rastlanıldı...
"""