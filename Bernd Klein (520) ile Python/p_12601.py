# coding:iso-8859-9 T�rk�e
# p_12601.py: Ola�an, bellemeli dekorat�r ve @ direktifli fibonaki fonksiyonu �rne�i.

def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

from random import randint

a = randint (0, 30)
print ("Ola�an fibonaki fonksiyonuyla", a, "adet seri a��l�m�:")
for i in range (a): print (fib (i), end=", ")
#-------------------------------------------------------------------------------------------------------

def bellekle (f):
    bellek = {}
    def yard�mc� (x):
        if x not in bellek: bellek[x] = f (x)
        return bellek[x]
    return yard�mc�

print ("\n\nFibonaki serisinde birsonrakini hesaplamak i�in hep tekrar tekrar 0'dan ba�lamak yerine �nceki de�erler bellekte saklanabilir. Bu da i�lem s�ratini �ok �ok art�r�r. Ayn� a��l�m� belleklemeli dekorat�r fibonakiyle tekrarlayal�m:")
for i in range (a): print (bellekle (fib) (i), end=", ")
#-------------------------------------------------------------------------------------------------------

@bellekle
def fib (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib (n-1) + fib (n-2)

print ("\n\n�a��rmay� 'bellekle (fib) (i)' yerine @ y�ntemiyle pratikle�tirelim:")
for i in range (a): print (fib (i), end=", ")


"""��kt�:
>python p_12601.py
Ola�an fibonaki fonksiyonuyla 18 adet seri a��l�m�:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,

Fibonaki serisinde birsonrakini hesaplamak i�in hep tekrar tekrar 0'dan ba�lamak
 yerine �nceki de�erler bellekte saklanabilir. Bu da i�lem s�ratini �ok �ok art�
r�r. Ayn� a��l�m� belleklemeli dekorat�r fibonakiyle tekrarlayal�m:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,

�a��rmay� 'bellekle (fib) (i)' yerine @ y�ntemiyle pratikle�tirelim:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
"""