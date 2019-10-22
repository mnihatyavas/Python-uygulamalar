# coding:iso-8859-9 "T�rk�e"

x = lambda a : a + 10 # Lambda haz�r fonksiyonu tan�m�...
print ("Lambda (5 + 10) =", x (5))

x = lambda a, b : a * b
print ("Lambda (5 * 6) =", x (5, 6))

x = lambda a, b, c : a + b + c
print ("Lambda (5 + 6 + 2) =", x (5, 6, 2))

def fonksiyonum (n): return lambda a : a * n

ikiKat = fonksiyonum (2)
print ("�ki katl� lambdal� 11 =", ikiKat (11))

be�Kat = fonksiyonum (5)
print ("Be� katl� lambdal� 11 =", be�Kat (11))
