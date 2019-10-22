# coding:iso-8859-9 T�rk�e
# p_20703.py: Grafik mod�l�yle yumru, ba�lant� ve yumrular aras�ndaki enk�sa patika �rne�i.

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

print ("Grafi�in yumrular�:")
print (grafik.yumrular())

print ("Grafi�in ba�lant�lar�:")
print (grafik.ba�lant�lar() )

print ('Yumru "a" dan yumru "b" ye giden patika:')
patika = grafik.patikaBul ("a", "b")
print (patika)

print ('Yumru ("a", "g") aras�ndaki patika:')
patika = grafik.patikaBul ("a", "g")
print (patika)

print ('Yumru ("c", "c") aras�ndaki patika:')
patika = grafik.patikaBul ("c", "c")
print (patika)

"""��kt�:
>python p_20703.py
Grafi�in yumrular�:
['a', 'b', 'c', 'd', 'e', 'f', 'g']
Grafi�in ba�lant�lar�:
[{'d', 'a'}, {'b', 'c'}, {'c'}, {'d', 'c'}, {'e', 'c'}, {'e', 'f'}, {'g', 'f'}]
Yumru "a" dan yumru "b" ye giden patika:
['a', 'd', 'c', 'b']
Yumru ("a", "g") aras�ndaki patika:
['a', 'd', 'c', 'e', 'f', 'g']
Yumru ("c", "c") aras�ndaki patika:
['c']
"""