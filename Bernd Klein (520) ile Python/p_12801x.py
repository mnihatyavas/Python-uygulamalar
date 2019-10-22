# coding:iso-8859-9 T�rk�e
# p_12801x.py: �zyineleme ve for d�ng�l� fibonaki fonksiyonlar� alt-�rne�i.

print ("==>p_12801x fibonaki mod�l� �uanda import/ithal edilmi�tir.")

def fib1 (n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib1 (n-1) + fib1 (n-2)

def fib2 (n):
    a, b = 0, 1
    for i in range (n): a, b = b, a + b
    return a

if __name__ == "__main__":
    import sys
    adet = int (sys.argv[1])
    for i in range (adet): print (fib1 (i), end=" ")
