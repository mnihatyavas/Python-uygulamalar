# coding:iso-8859-9 Türkçe
import sys

def fibonacci_serisi (n): # yield üreteç fonksiyonu...
    a, b, sayaç = 0, 1, 0
    while True:
        if (sayaç > n): return
        yield a # a üretir ve seriyi hafızasında saklar...
        a, b = b, a + b
        sayaç += 1

sayı = int (input ("Fibonacci sayısı girin: "))
tara = fibonacci_serisi (sayı) # tara bir Iterator nesnesidir...
print (sayı, "sayısının Fibonacci seri açılımı==>")
while True:
    try:print (next (tara), end=" ")
    except StopIteration: sys.exit()
