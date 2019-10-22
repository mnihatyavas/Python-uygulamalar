# coding:iso-8859-9 T�rk�e
# p_20704.py: Grafik mod�l�yle, bir yumrunun derecesi, azami-asgari dereceler, dereceler t�plesi �rne�i.

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

print ("\n�zole yumrular listesi:")
print (grafik.izoleYumrular() )

print ("\nAsgari ve azami dereceler:")
print (grafik.asgariDerece(), grafik.azamiDerece() )

print ("\nDerecelerin (t�ple) silsilesi:")
silsileT�plesi = grafik.dereceSilsilesi()
print (silsileT�plesi)

print ("\nErd�s-Galay'�n sav� do�rulan�yor mu?: ", end="")
print (grafik.erdoes_gallai (silsileT�plesi) )



"""��kt�:
>python p_20704.py
Verili yumru dereceleri:
c: 5
g: 1
h: 0

�zole yumrular listesi:
['h']

Asgari ve azami dereceler:
0 5

Derecelerin (t�ple) silsilesi:
(5, 2, 2, 2, 1, 1, 1, 0)

Erd�s-Galay'�n sav� do�rulan�yor mu?: True
"""