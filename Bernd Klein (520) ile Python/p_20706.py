# coding:iso-8859-9 T�rk�e
# p_20706.py: Verili grafiklerin yumrular�, ba�lant�lar� ve izolelelerinin tespiti �rne�i.

from p_20702 import Grafik

g1 = {
    "a" : ["d"],
    "b" : ["c"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : []
}

g2 = {
    "a" : ["d","f"],
    "b" : ["c"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : ["a"]
}

g3 = {
    "a" : ["d","f"],
    "b" : ["c","b"],
    "c" : ["b", "c", "d", "e"],
    "d" : ["a", "c"],
    "e" : ["c"],
    "f" : ["a"],
    "g" : []
}

g4 = {
    "a" : ["c"],
    "b" : ["c", "e", "f"],
    "c" : ["a", "b", "d", "e"],
    "d" : ["c"],
    "e" : ["b", "c", "f"],
    "f" : ["b", "e"]
}

grafik = Grafik (g1)
print ("Grafik 'g1' i�in==>")
print (grafik) # Varsay�l� __str__ �a�r�l�r...
print ("Yumrular�n t�m� ba�lant�l� m�?:", grafik.ba�lant�l�M�() )

grafik = Grafik (g2)
print ("\nGrafik 'g2' i�in==>")
print (grafik)
print ("Yumrular�n t�m� ba�lant�l� m�?:", grafik.ba�lant�l�M�() )

grafik = Grafik (g3)
print ("\nGrafik 'g3' i�in==>")
print (grafik)
print ("Yumrular�n t�m� ba�lant�l� m�?:", grafik.ba�lant�l�M�())

grafik = Grafik (g4)
print ("\nGrafik 'g4' i�in==>")
print (grafik)
print ("Yumrular�n t�m� ba�lant�l� m�?:", grafik.ba�lant�l�M�())

"""��kt�:
>python p_20706.py
Grafik 'g1' i�in==>
Yumrular: a b c d e f
Ba�lant�lar: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumrular�n t�m� ba�lant�l� m�?: False

Grafik 'g2' i�in==>
Yumrular: a b c d e f
Ba�lant�lar: {'a', 'd'} {'a', 'f'} {'c', 'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumrular�n t�m� ba�lant�l� m�?: True

Grafik 'g3' i�in==>
Yumrular: a b c d e f g
Ba�lant�lar: {'a', 'd'} {'a', 'f'} {'c', 'b'} {'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumrular�n t�m� ba�lant�l� m�?: False

Grafik 'g4' i�in==>
Yumrular: a b c d e f
Ba�lant�lar: {'c', 'a'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'c', 'e'} {'e', 'f'}
Yumrular�n t�m� ba�lant�l� m�?: True
"""