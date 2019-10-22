# coding:iso-8859-9 Türkçe
# p_20705.py: Grafik modülüyle verili grafiklerin bağlantılar listesi ve yoğunlukları örneği.

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
print ("Grafik bağlantıları listesi ve yoğunluk derecesi:")
print ("Grafik g1:", "\n==>", grafik.bağlantılar(), "\n==>", grafik.yoğunluk() )

grafik = Grafik (g2)
print ("\nGrafik g2:", "\n==>", grafik.bağlantılar(), "\n==>", grafik.yoğunluk() )

print ("\nGrafik g3:", "\n==>", Grafik (g3).bağlantılar(), "\n==>", Grafik (g3).yoğunluk() )

"""Çıktı:
>python p_20705.py
Grafik bağlantıları listesi ve yoğunluk derecesi:
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