# coding:iso-8859-9 Türkçe
# p_12602.py: Bellemeli dekoratör sınıflı ve @ direktifli fibonaki serisi örneği.

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
Sınıf = Bellekle (fib)

print (adet, "adet fibonaki seri açılımı: ")
for i in range (adet): print (Sınıf (i), end=", ")
#-----------------------------------------------------------------------------------------------------

@Bellekle
def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

print ("\n\n@Bellekle dekoratör sınıf nesnesi tanıtımlı fib serisi:")
for i in range (adet): print (fib (i), end=", ")


"""Çıktı:
>python p_12602.py
12 adet fibonaki seri açılımı:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,

@Bellekle dekoratör sınıf nesnesi tanıtımlı fib serisi:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
"""