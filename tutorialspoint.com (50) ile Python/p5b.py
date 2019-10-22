# coding:iso-8859-9 T�rk�e
import sys

def fibonacci_serisi (n): # yield �rete� fonksiyonu...
    a, b, saya� = 0, 1, 0
    while True:
        if (saya� > n): return
        yield a # a �retir ve seriyi haf�zas�nda saklar...
        a, b = b, a + b
        saya� += 1

say� = int (input ("Fibonacci say�s� girin: "))
tara = fibonacci_serisi (say�) # tara bir Iterator nesnesidir...
print (say�, "say�s�n�n Fibonacci seri a��l�m�==>")
while True:
    try:print (next (tara), end=" ")
    except StopIteration: sys.exit()
