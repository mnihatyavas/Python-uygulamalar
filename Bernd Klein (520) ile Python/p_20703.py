# coding:iso-8859-9 Türkçe
# p_20703.py: Grafik modülüyle yumru, bağlantı ve yumrular arasındaki enkısa patika örneği.

from p_20702 import Grafik

g = {
        "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c", "f"],
        "f" : ["e", "g"],
        "g" : ["f"]
    }


grafik = Grafik (g)

print ("Grafiğin yumruları:")
print (grafik.yumrular())

print ("Grafiğin bağlantıları:")
print (grafik.bağlantılar() )

print ('Yumru "a" dan yumru "b" ye giden patika:')
patika = grafik.patikaBul ("a", "b")
print (patika)

print ('Yumru ("a", "g") arasındaki patika:')
patika = grafik.patikaBul ("a", "g")
print (patika)

print ('Yumru ("c", "c") arasındaki patika:')
patika = grafik.patikaBul ("c", "c")
print (patika)

"""Çıktı:
>python p_20703.py
Grafiğin yumruları:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Grafiğin bağlantıları:
[{'d', 'a'}, {'b', 'c'}, {'c'}, {'d', 'c'}, {'e', 'c'}, {'e', 'f'}, {'g', 'f'}]
Yumru "a" dan yumru "b" ye giden patika:
['a', 'd', 'c', 'b']
Yumru ("a", "g") arasındaki patika:
['a', 'd', 'c', 'e', 'f', 'g']
Yumru ("c", "c") arasındaki patika:
['c']
"""