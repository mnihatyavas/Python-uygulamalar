# coding:iso-8859-9 Türkçe
# p_20704.py: Grafik modülüyle, bir yumrunun derecesi, azami-asgari dereceler, dereceler tüplesi örneği.

from p_20702 import Grafik

g = {
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c", "f"],
        "f" : ["e", "g"],
        "g" : ["f"],
        "h" : []
    }

grafik = Grafik (g)

print ("Verili yumru dereceleri:")
print ("c:", grafik.yumruDerecesi ("c") )
print ("g:", grafik.yumruDerecesi ("g") )
print ("h:", grafik.yumruDerecesi ("h") )

print ("\nİzole yumrular listesi:")
print (grafik.izoleYumrular() )

print ("\nAsgari ve azami dereceler:")
print (grafik.asgariDerece(), grafik.azamiDerece() )

print ("\nDerecelerin (tüple) silsilesi:")
silsileTüplesi = grafik.dereceSilsilesi()
print (silsileTüplesi)

print ("\nErdös-Galay'ın savı doğrulanıyor mu?: ", end="")
print (grafik.erdoes_gallai (silsileTüplesi) )



"""Çıktı:
>python p_20704.py
Verili yumru dereceleri:
c: 5
g: 1
h: 0

İzole yumrular listesi:
['h']

Asgari ve azami dereceler:
0 5

Derecelerin (tüple) silsilesi:
(5, 2, 2, 2, 1, 1, 1, 0)

Erdös-Galay'ın savı doğrulanıyor mu?: True
"""