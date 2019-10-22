# coding:iso-8859-9 Türkçe
# p_12601.py: Olağan, bellemeli dekoratör ve @ direktifli fibonaki fonksiyonu örneği.

def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

from random import randint

a = randint (0, 30)
print ("Olağan fibonaki fonksiyonuyla", a, "adet seri açılımı:")
for i in range (a): print (fib (i), end=", ")
#-------------------------------------------------------------------------------------------------------

def bellekle (f):
    bellek = {}
    def yardımcı (x):
        if x not in bellek: bellek[x] = f (x)
        return bellek[x]
    return yardımcı

print ("\n\nFibonaki serisinde birsonrakini hesaplamak için hep tekrar tekrar 0'dan başlamak yerine önceki değerler bellekte saklanabilir. Bu da işlem süratini çok çok artırır. Aynı açılımı belleklemeli dekoratör fibonakiyle tekrarlayalım:")
for i in range (a): print (bellekle (fib) (i), end=", ")
#-------------------------------------------------------------------------------------------------------

@bellekle
def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

print ("\n\nÇağırmayı 'bellekle (fib) (i)' yerine @ yöntemiyle pratikleştirelim:")
for i in range (a): print (fib (i), end=", ")


"""Çıktı:
>python p_12601.py
Olağan fibonaki fonksiyonuyla 18 adet seri açılımı:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,

Fibonaki serisinde birsonrakini hesaplamak için hep tekrar tekrar 0'dan başlamak
 yerine önceki değerler bellekte saklanabilir. Bu da işlem süratini çok çok artı
rır. Aynı açılımı belleklemeli dekoratör fibonakiyle tekrarlayalım:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,

Çağırmayı 'bellekle (fib) (i)' yerine @ yöntemiyle pratikleştirelim:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
"""