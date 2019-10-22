# coding:iso-8859-9 T�rk�e
# p_12602.py: Bellemeli dekorat�r s�n�fl� ve @ direktifli fibonaki serisi �rne�i.

class Bellekle:
    def __init__ (self, f):
        self.f = f
        self.bellek = {}
    def __call__ (self, *a):
        if a not in self.bellek: self.bellek [a] = self.f (*a)
        return self.bellek[a]

def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

from random import randint
adet = randint (0, 30)
S�n�f = Bellekle (fib)

print (adet, "adet fibonaki seri a��l�m�: ")
for i in range (adet): print (S�n�f (i), end=", ")
#-----------------------------------------------------------------------------------------------------

@Bellekle
def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

print ("\n\n@Bellekle dekorat�r s�n�f nesnesi tan�t�ml� fib serisi:")
for i in range (adet): print (fib (i), end=", ")


"""��kt�:
>python p_12602.py
12 adet fibonaki seri a��l�m�:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

@Bellekle dekorat�r s�n�f nesnesi tan�t�ml� fib serisi:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
"""