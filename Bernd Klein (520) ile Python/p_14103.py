# coding:iso-8859-9 T�rk�e
# p_14103.py: Pyyhon fonksiyonlar�n�n �okbi�imli arg�man tiplemesi �rne�i.

def f (x, y): print ("Fonksiyona ge�irilen arg�manlar: ", x, ":", type (x), "; ", y, ":", type (y), sep="")

f (42, 43) # (int, int)
f (42, 43.7) # (int, float)
f (42.3, 43) # (float, int)
f (42.0, 43.9) # (float, float)

""" Python polimorfik/�okbi�imli'dir.
Java ve C++ her farkl� veri �e�idi i�in ayr�
fonksiyonlar tan�mlar ve overload/a��r�y�klenme
yaparken, python i�in tek bir fonksiyon yeterlidir...
"""

print()
f ([3,5,6], (3,5) ) # (liste, t�ple)
f ("Bir dizge", ("Dizgeli", "bir t�ple") ) # (dizge, t�ple)
f ({2, 3, 9}, {"a":3.4, "b":7.8, "c":9.04} ) # (k�me, s�zl�k)



"""��kt�:
>python p_14103.py
Fonksiyona ge�irilen arg�manlar: 42:<class 'int'>; 43:<class 'int'>
Fonksiyona ge�irilen arg�manlar: 42:<class 'int'>; 43.7:<class 'float'>
Fonksiyona ge�irilen arg�manlar: 42.3:<class 'float'>; 43:<class 'int'>
Fonksiyona ge�irilen arg�manlar: 42.0:<class 'float'>; 43.9:<class 'float'>

Fonksiyona ge�irilen arg�manlar: [3, 5, 6]:<class 'list'>; (3, 5):<class 'tuple'>
Fonksiyona ge�irilen arg�manlar: Bir dizge:<class 'str'>; ('Dizgeli', 'bir t�ple'):<class 'tuple'>
Fonksiyona ge�irilen arg�manlar: {9, 2, 3}:<class 'set'>; {'a': 3.4, 'b': 7.8, 'c': 9.04}:<class 'dict'>
"""