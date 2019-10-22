# coding:iso-8859-9 T�rk�e
# p_20707.py: Verili grafiklerin yumrular�, ba�lant�lar� ve �aplar� �rne�i.

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
�ap = grafik.grafi�in�ap�()
print ("Grafik 'g1' i�in==>")
print (grafik, "\nGrafi�in �ap�: ", �ap, sep="")

g = Grafik (g2)
�ap = g.grafi�in�ap�()
print ("\nGrafik 'g2' i�in==>")
print (g, "\nGrafi�in �ap�: ", �ap, sep="")

print ("\nGrafik 'g3' i�in==>")
print (Grafik (g3), "\nGrafi�in �ap�: ", Grafik (g3).grafi�in�ap�(), sep="")



"""��kt�:
>python p_20708.py
Grafik 'g1' i�in==>
Yumrular: a b c d e f
Ba�lant�lar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'}
Grafi�in �ap�: 3

Grafik 'g2' i�in==>
Yumrular: a b c d e f g
Ba�lant�lar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'} {'g', 'f'}
Grafi�in �ap�: 4

Grafik 'g3' i�in==>
Yumrular: a b c d e f g h
Ba�lant�lar: {'a', 'c'} {'c', 'b'} {'e', 'b'} {'f', 'b'} {'c', 'd'} {'e', 'c'} {'e', 'f'} {'g', 'f'} {'g', 'h'}
Grafi�in �ap�: 5
"""