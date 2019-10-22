# coding:iso-8859-9 Türkçe
# Gereken dosyalar: p_12102x1.py ve p_12102x2.py
# p_12102.py: For-döngülü ve özyinelemeli ayrıca da bellekli fibonaki kıyaslamaları örneği.

from random import randint

def fibonaki (n):
    if n > 0: print (0, 1, end=" ")
    else:
        print (0, end=" ")
        return 0
    a, b = 0, 1
    for i in range (n):
        print (a+b, end=" ")
        a, b = b, a + b
    return b

sayı = randint (0, 20)
print ("\n", sayı, " sayısının for döngülü tekrarlanabilir fibonaki sonucu: ", fibonaki (sayı), sep="")
#------------------------------------------------------------------------------------------------------

def fibonaki2 (n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        print (n, end=" ")
        return fibonaki2 (n-1) + fibonaki2 (n-2)

print()
print ("\n", sayı, " sayısının özyinelemeli fibonaki sonucu: ", fibonaki2 (sayı), sep="")
#------------------------------------------------------------------------------------------------------

from timeit import Timer

print()
for i in range (sayı+1):
    s = "fib1 (" + str(i) + ")"
    t1 = Timer (s, "from p_12102x1 import fib1")
    zaman1 = t1.timeit (10) # 10 kez çağırır ve toplam zamanını alır...
    s = "fib2 (" + str(i) + ")"
    t2 = Timer (s, "from p_12102x1 import fib2")
    zaman2 = t2.timeit (10) # 10 kez çağırır ve toplam zamanını alır...
    print ("n=%2d, fibonaki1: %8.6f, fibonaki2:  %7.6f, zaman1/zaman2: %.2f" % (i, zaman2, zaman1, zaman2 / zaman1))

print ("\nYani, sonuç olarak özyinelemeli fibonaki, for-döngülüden {:.2f} kat VERİMSİZDİR!" .format (zaman2/zaman1) )
#------------------------------------------------------------------------------------------------------

from timeit import Timer

print ("Sebebi önceki özyinelemeleri unutmasıdır!.. Şayet öncekileri belleğe saklarsak:\n")
for i in range (sayı+1):
    s = "fib1 (" + str(i) + ")"
    t1 = Timer (s, "from p_12102x2 import fib1")
    zaman1 = t1.timeit (10) # 10 kez çağırır ve toplam zamanını alır...
    s = "fib2 (" + str(i) + ")"
    t2 = Timer (s, "from p_12102x2 import fib2")
    zaman2 = t2.timeit (10) # 10 kez çağırır ve toplam zamanını alır...
    print ("n=%2d, fibonaki1: %8.6f, fibonaki2:  %7.6f, zaman1/zaman2: %.2f" % (i, zaman2, zaman1, zaman2 / zaman1))

print ("\nYani, sonuç olarak özyinelemeli fibonaki, for-döngülüden {:.2f} kat VERİMLİDİR!" .format (zaman1/zaman2) )


"""Çıktı:
>python p_12102.py
0 1 1 2 3 5 8
5 sayısının for döngülü tekrarlanabilir fibonaki sonucu: 8

0 1 1 2 3 5 8
5 sayısının özyinelemeli fibonaki sonucu: 8

n= 0, fibonaki1: 0.000030, fibonaki2:  0.000048, zaman1/zaman2: 0.63
n= 1, fibonaki1: 0.000036, fibonaki2:  0.000142, zaman1/zaman2: 0.26
n= 2, fibonaki1: 0.000103, fibonaki2:  0.000148, zaman1/zaman2: 0.70
n= 3, fibonaki1: 0.000169, fibonaki2:  0.000155, zaman1/zaman2: 1.09
n= 4, fibonaki1: 0.000286, fibonaki2:  0.000278, zaman1/zaman2: 1.03
n= 5, fibonaki1: 0.000472, fibonaki2:  0.000168, zaman1/zaman2: 2.80

Yani, sonuç olarak özyinelemeli fibonaki, for-döngülüden 2.80 kat VERİMSİZDİR!
Sebebi önceki özyinelemeleri unutmasıdır!.. Şayet öncekileri belleğe saklarsak:

n= 0, fibonaki1: 0.000045, fibonaki2:  0.000036, zaman1/zaman2: 1.23
n= 1, fibonaki1: 0.000041, fibonaki2:  0.000139, zaman1/zaman2: 0.30
n= 2, fibonaki1: 0.000056, fibonaki2:  0.000150, zaman1/zaman2: 0.37
n= 3, fibonaki1: 0.000056, fibonaki2:  0.000155, zaman1/zaman2: 0.36
n= 4, fibonaki1: 0.000055, fibonaki2:  0.000163, zaman1/zaman2: 0.34
n= 5, fibonaki1: 0.000044, fibonaki2:  0.012681, zaman1/zaman2: 0.00

Yani, sonuç olarak özyinelemeli fibonaki, for-döngülüden 285.47 kat VERİMLİDİR!
"""