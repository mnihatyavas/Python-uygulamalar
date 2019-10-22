# coding:iso-8859-9 Türkçe
# p_20707.py: Verili grafiklerin yumruları, bağlantıları ve çapları örneği.

from p_20702 import Grafik

g1 = {
    "a" : ["c"],
    "b" : ["c","e","f"],
    "c" : ["a","b","d","e"],
    "d" : ["c"],
    "e" : ["b","c","f"],
    "f" : ["b","e"]
}

g2 = {
    "a" : ["c"],
    "b" : ["c","e","f"],
    "c" : ["a","b","d","e"],
    "d" : ["c"],
    "e" : ["b","c","f"],
    "f" : ["b","e", "g"],
    "g" : ["f"]
}

g3 = {
    "a" : ["c"],
    "b" : ["c", "e", "f"],
    "c" : ["a", "b", "d", "e"],
    "d" : ["c"],
    "e" : ["b", "c", "f"],
    "f" : ["b", "e", "g"],
    "g" : ["f", "h"],
    "h" : ["g"]
}

grafik = Grafik (g1)
çap = grafik.grafiğinÇapı()
print ("Grafik 'g1' için==>")
print (grafik, "\nGrafiğin çapı: ", çap, sep="")

g = Grafik (g2)
çap = g.grafiğinÇapı()
print ("\nGrafik 'g2' için==>")
print (g, "\nGrafiğin çapı: ", çap, sep="")

print ("\nGrafik 'g3' için==>")
print (Grafik (g3), "\nGrafiğin çapı: ", Grafik (g3).grafiğinÇapı(), sep="")



"""Çıktı:
>python p_20708.py
Grafik 'g1' için==>
Yumrular: a b c d e f
Bağlantılar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'}
Grafiğin çapı: 3

Grafik 'g2' için==>
Yumrular: a b c d e f g
Bağlantılar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'} {'g', 'f'}
Grafiğin çapı: 4

Grafik 'g3' için==>
Yumrular: a b c d e f g h
Bağlantılar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'} {'g', 'f'} {'g', 'h'}
Grafiğin çapı: 5
"""