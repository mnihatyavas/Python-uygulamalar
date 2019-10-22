# coding:iso-8859-9 Türkçe
# p_12004.py: Fibonaki fonksiyonunun serideki son iki değeri döndürmesi örneği.

from random import randint

def fib (x):
    (a, b, c) = (0, 1, 0)
    print (x, "sayısı için fibonaki serisi:", 0, end=", ")
    while True:
        if b <= x:
            c = b
            (a, b) = (b, a + b)
            print (a, end=", ")
        else:
            print (b)
            return (c, b)

sayı = randint (0, 100)
(küçük, büyük) = fib (sayı)
print (sayı, "'ten küçük, enbüyük fibonaki sayısı: ", küçük, sep="")
print (sayı, "'ten büyük, enküçük fibonaki sayısı: ", büyük, sep="")


"""Çıktı:
>python p_12004.py
49 sayısı için fibonaki serisi: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
49'ten küçük, enbüyük fibonaki sayısı: 34
49'ten büyük, enküçük fibonaki sayısı: 55
"""