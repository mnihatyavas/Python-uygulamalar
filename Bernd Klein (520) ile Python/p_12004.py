# coding:iso-8859-9 T�rk�e
# p_12004.py: Fibonaki fonksiyonunun serideki son iki de�eri d�nd�rmesi �rne�i.

from random import randint

def fib (x):
    (a, b, c) = (0, 1, 0)
    print (x, "say�s� i�in fibonaki serisi:", 0, end=", ")
    while True:
        if b <= x:
            c = b
            (a, b) = (b, a + b)
            print (a, end=", ")
        else:
            print (b)
            return (c, b)

say� = randint (0, 100)
(k���k, b�y�k) = fib (say�)
print (say�, "'ten k���k, enb�y�k fibonaki say�s�: ", k���k, sep="")
print (say�, "'ten b�y�k, enk���k fibonaki say�s�: ", b�y�k, sep="")


"""��kt�:
>python p_12004.py
49 say�s� i�in fibonaki serisi: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
49'ten k���k, enb�y�k fibonaki say�s�: 34
49'ten b�y�k, enk���k fibonaki say�s�: 55
"""