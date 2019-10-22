# coding:iso-8859-9 Türkçe
# p_12106.py: Fibonaki sayıları, kareleri ve endeksleri örneği.

bellek = {0:0, 1:1}
def fibonaki (n):
    if not n in bellek: bellek [n] = fibonaki (n-1) + fibonaki (n-2)
    return bellek [n]

def endeksiBul (*x):
    if len (x) == 1: return endeksiBul (x[0], 0)
    else:
        n = fibonaki (x[1])
        m = x[0]
        if  n > m: return -1
        elif n == m: return x[1]
        else: return endeksiBul (m, x[1]+1)

print ("20'lik fibonaki serisi listesi:", [fibonaki (i) for i in range (20)])
print()
sayı = 144
konum = endeksiBul (sayı)
if konum == -1: print (konum, "==> ", sayı, " sayısı 20'lik fibonakide NAMEVCUT!", sep="")
else: print (fibonaki (konum) == sayı, "==> ", sayı, " sayısı fibonaki ", konum, ".endekste MEVCUT.", sep="")
#--------------------------------------------------------------------------------------------------------

print ("\nfibA endeks | fibA | fibB | Kare Tpl | fibA'daki Konumu")
print ("=======================================================")
for i in range (20):
    karesi = fibonaki (i)**2 + fibonaki (i+1)**2
    print (" %10d | %4d | %4d | %8d | %2d" % (i, fibonaki (i), fibonaki (i+1), karesi, endeksiBul (karesi)) )


"""Çıktı:
>python p_12106.py
20'lik fibonaki serisi listesi: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
233, 377, 610, 987, 1597, 2584, 4181]

True==> 144 sayısı fibonaki 12.endekste MEVCUT.

fibA endeks | fibA | fibB | Kare Tpl | fibA'daki Konumu
=======================================================
          0 |    0 |    1 |        1 |  1
          1 |    1 |    1 |        2 |  3
          2 |    1 |    2 |        5 |  5
          3 |    2 |    3 |       13 |  7
          4 |    3 |    5 |       34 |  9
          5 |    5 |    8 |       89 | 11
          6 |    8 |   13 |      233 | 13
          7 |   13 |   21 |      610 | 15
          8 |   21 |   34 |     1597 | 17
          9 |   34 |   55 |     4181 | 19
         10 |   55 |   89 |    10946 | 21
         11 |   89 |  144 |    28657 | 23
         12 |  144 |  233 |    75025 | 25
         13 |  233 |  377 |   196418 | 27
         14 |  377 |  610 |   514229 | 29
         15 |  610 |  987 |  1346269 | 31
         16 |  987 | 1597 |  3524578 | 33
         17 | 1597 | 2584 |  9227465 | 35
         18 | 2584 | 4181 | 24157817 | 37
         19 | 4181 | 6765 | 63245986 | 39
"""