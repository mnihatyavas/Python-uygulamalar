# coding:iso-8859-9 T�rk�e
# p_20705.py: Grafik mod�l�yle verili grafiklerin ba�lant�lar listesi ve yo�unluklar� �rne�i.

from p_20702 import Grafik

g1 = {
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c", "f"],
        "f" : ["e", "g"],
        "g" : ["f"],
        "h" : []
    }

g2 = {
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
}

g3 = {"a" : [], "b" : [], "c" : []}

grafik = Grafik (g1)
print ("Grafik ba�lant�lar� listesi ve yo�unluk derecesi:")
print ("Grafik g1:", "\n==>", grafik.ba�lant�lar(), "\n==>", grafik.yo�unluk() )

grafik = Grafik (g2)
print ("\nGrafik g2:", "\n==>", grafik.ba�lant�lar(), "\n==>", grafik.yo�unluk() )

print ("\nGrafik g3:", "\n==>", Grafik (g3).ba�lant�lar(), "\n==>", Grafik (g3).yo�unluk() )

"""��kt�:
>python p_20705.py
Grafik ba�lant�lar� listesi ve yo�unluk derecesi:
Grafik g1:
==> [{'d', 'a'}, {'b', 'c'}, {'c'}, {'d', 'c'}, {'c', 'e'}, {'f', 'e'}, {'f', 'g'}]
==> 0.25

Grafik g2:
==> [{'a', 'b'}, {'a', 'c'}, {'b', 'c'}]
==> 1.0

Grafik g3:
==> []
==> 0.0
"""