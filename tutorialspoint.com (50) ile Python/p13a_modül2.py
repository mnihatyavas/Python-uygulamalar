# coding:iso-8859-9 T�rk�e

def fib (n):
    sonu� = [ ]
    a, b = 0, 1
    while b < n:
        sonu�.append (b)
        a, b = b, a + b
    return sonu�

if __name__ == "__main__":
   f = fib (100)
   print (f)
