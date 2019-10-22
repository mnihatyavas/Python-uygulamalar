# coding:iso-8859-9 Türkçe
# p_20706.py: Verili grafiklerin yumruları, bağlantıları ve izolelelerinin tespiti örneği.

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
print ("Grafik 'g1' için==>")
print (grafik) # Varsayılı __str__ çağrılır...
print ("Yumruların tümü bağlantılı mı?:", grafik.bağlantılıMı() )

grafik = Grafik (g2)
print ("\nGrafik 'g2' için==>")
print (grafik)
print ("Yumruların tümü bağlantılı mı?:", grafik.bağlantılıMı() )

grafik = Grafik (g3)
print ("\nGrafik 'g3' için==>")
print (grafik)
print ("Yumruların tümü bağlantılı mı?:", grafik.bağlantılıMı())

grafik = Grafik (g4)
print ("\nGrafik 'g4' için==>")
print (grafik)
print ("Yumruların tümü bağlantılı mı?:", grafik.bağlantılıMı())

"""Çıktı:
>python p_20706.py
Grafik 'g1' için==>
Yumrular: a b c d e f
Bağlantılar: {'a', 'd'} {'c', 'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumruların tümü bağlantılı mı?: False

Grafik 'g2' için==>
Yumrular: a b c d e f
Bağlantılar: {'a', 'd'} {'a', 'f'} {'c', 'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumruların tümü bağlantılı mı?: True

Grafik 'g3' için==>
Yumrular: a b c d e f g
Bağlantılar: {'a', 'd'} {'a', 'f'} {'c', 'b'} {'b'} {'c'} {'c', 'd'} {'c', 'e'}
Yumruların tümü bağlantılı mı?: False

Grafik 'g4' için==>
Yumrular: a b c d e f
Bağlantılar: {'c', 'a'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'c', 'e'} {'e', 'f'}
Yumruların tümü bağlantılı mı?: True
"""