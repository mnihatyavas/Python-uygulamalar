# coding:iso-8859-9 Türkçe

def fib (n):
    sonuç = [ ]
    a, b = 0, 1
    while b < n:
        sonuç.append (b)
        a, b = b, a + b
    return sonuç

if __name__ == "__main__":
   f = fib (100)
   print (f)
