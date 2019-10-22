# coding:iso-8859-9 T�rk�e
# Gereken dosyalar: p_12102x1.py ve p_12102x2.py
# p_12102.py: For-d�ng�l� ve �zyinelemeli ayr�ca da bellekli fibonaki k�yaslamalar� �rne�i.

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

say� = randint (0, 20)
print ("\n", say�, " say�s�n�n for d�ng�l� tekrarlanabilir fibonaki sonucu: ", fibonaki (say�), sep="")
#------------------------------------------------------------------------------------------------------

def fibonaki2 (n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        print (n, end=" ")
        return fibonaki2 (n-1) + fibonaki2 (n-2)

print()
print ("\n", say�, " say�s�n�n �zyinelemeli fibonaki sonucu: ", fibonaki2 (say�), sep="")
#------------------------------------------------------------------------------------------------------

from timeit import Timer

print()
for i in range (say�+1):
    s = "fib1 (" + str(i) + ")"
    t1 = Timer (s, "from p_12102x1 import fib1")
    zaman1 = t1.timeit (10) # 10 kez �a��r�r ve toplam zaman�n� al�r...
    s = "fib2 (" + str(i) + ")"
    t2 = Timer (s, "from p_12102x1 import fib2")
    zaman2 = t2.timeit (10) # 10 kez �a��r�r ve toplam zaman�n� al�r...
    print ("n=%2d, fibonaki1: %8.6f, fibonaki2:  %7.6f, zaman1/zaman2: %.2f" % (i, zaman2, zaman1, zaman2 / zaman1))

print ("\nYani, sonu� olarak �zyinelemeli fibonaki, for-d�ng�l�den {:.2f} kat VER�MS�ZD�R!" .format (zaman2/zaman1) )
#------------------------------------------------------------------------------------------------------

from timeit import Timer

print ("Sebebi �nceki �zyinelemeleri unutmas�d�r!.. �ayet �ncekileri belle�e saklarsak:\n")
for i in range (say�+1):
    s = "fib1 (" + str(i) + ")"
    t1 = Timer (s, "from p_12102x2 import fib1")
    zaman1 = t1.timeit (10) # 10 kez �a��r�r ve toplam zaman�n� al�r...
    s = "fib2 (" + str(i) + ")"
    t2 = Timer (s, "from p_12102x2 import fib2")
    zaman2 = t2.timeit (10) # 10 kez �a��r�r ve toplam zaman�n� al�r...
    print ("n=%2d, fibonaki1: %8.6f, fibonaki2:  %7.6f, zaman1/zaman2: %.2f" % (i, zaman2, zaman1, zaman2 / zaman1))

print ("\nYani, sonu� olarak �zyinelemeli fibonaki, for-d�ng�l�den {:.2f} kat VER�ML�D�R!" .format (zaman1/zaman2) )


"""��kt�:
>python p_12102.py
0 1 1 2 3 5 8
5 say�s�n�n for d�ng�l� tekrarlanabilir fibonaki sonucu: 8

0 1 1 2 3 5 8
5 say�s�n�n �zyinelemeli fibonaki sonucu: 8

n= 0, fibonaki1: 0.000030, fibonaki2:  0.000048, zaman1/zaman2: 0.63
n= 1, fibonaki1: 0.000036, fibonaki2:  0.000142, zaman1/zaman2: 0.26
n= 2, fibonaki1: 0.000103, fibonaki2:  0.000148, zaman1/zaman2: 0.70
n= 3, fibonaki1: 0.000169, fibonaki2:  0.000155, zaman1/zaman2: 1.09
n= 4, fibonaki1: 0.000286, fibonaki2:  0.000278, zaman1/zaman2: 1.03
n= 5, fibonaki1: 0.000472, fibonaki2:  0.000168, zaman1/zaman2: 2.80

Yani, sonu� olarak �zyinelemeli fibonaki, for-d�ng�l�den 2.80 kat VER�MS�ZD�R!
Sebebi �nceki �zyinelemeleri unutmas�d�r!.. �ayet �ncekileri belle�e saklarsak:

n= 0, fibonaki1: 0.000045, fibonaki2:  0.000036, zaman1/zaman2: 1.23
n= 1, fibonaki1: 0.000041, fibonaki2:  0.000139, zaman1/zaman2: 0.30
n= 2, fibonaki1: 0.000056, fibonaki2:  0.000150, zaman1/zaman2: 0.37
n= 3, fibonaki1: 0.000056, fibonaki2:  0.000155, zaman1/zaman2: 0.36
n= 4, fibonaki1: 0.000055, fibonaki2:  0.000163, zaman1/zaman2: 0.34
n= 5, fibonaki1: 0.000044, fibonaki2:  0.012681, zaman1/zaman2: 0.00

Yani, sonu� olarak �zyinelemeli fibonaki, for-d�ng�l�den 285.47 kat VER�ML�D�R!
"""