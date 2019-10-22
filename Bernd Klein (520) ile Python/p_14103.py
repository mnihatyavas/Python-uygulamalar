# coding:iso-8859-9 Türkçe
# p_14103.py: Pyyhon fonksiyonlarının çokbiçimli argüman tiplemesi örneği.

def f (x, y): print ("Fonksiyona geçirilen argümanlar: ", x, ":", type (x), "; ", y, ":", type (y), sep="")

f (42, 43) # (int, int)
f (42, 43.7) # (int, float)
f (42.3, 43) # (float, int)
f (42.0, 43.9) # (float, float)

""" Python polimorfik/çokbiçimli'dir.
Java ve C++ her farklı veri çeşidi için ayrı
fonksiyonlar tanımlar ve overload/aşırıyüklenme
yaparken, python için tek bir fonksiyon yeterlidir...
"""

print()
f ([3,5,6], (3,5) ) # (liste, tüple)
f ("Bir dizge", ("Dizgeli", "bir tüple") ) # (dizge, tüple)
f ({2, 3, 9}, {"a":3.4, "b":7.8, "c":9.04} ) # (küme, sözlük)



"""Çıktı:
>python p_14103.py
Fonksiyona geçirilen argümanlar: 42:<class 'int'>; 43:<class 'int'>
Fonksiyona geçirilen argümanlar: 42:<class 'int'>; 43.7:<class 'float'>
Fonksiyona geçirilen argümanlar: 42.3:<class 'float'>; 43:<class 'int'>
Fonksiyona geçirilen argümanlar: 42.0:<class 'float'>; 43.9:<class 'float'>

Fonksiyona geçirilen argümanlar: [3, 5, 6]:<class 'list'>; (3, 5):<class 'tuple'>
Fonksiyona geçirilen argümanlar: Bir dizge:<class 'str'>; ('Dizgeli', 'bir tüple'):<class 'tuple'>
Fonksiyona geçirilen argümanlar: {9, 2, 3}:<class 'set'>; {'a': 3.4, 'b': 7.8, 'c': 9.04}:<class 'dict'>
"""