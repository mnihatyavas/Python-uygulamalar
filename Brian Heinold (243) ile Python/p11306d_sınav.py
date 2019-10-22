# coding:iso-8859-9 Türkçe

def taban20 (n):
    L1 = []
    if n == 0: return "A"
    while n > 0:
        L1 = L1 + [n % 20]
        n = n//20
    tt = çevir (L1)
    return tt

def çevir (L1):
    dizge = "ABCDEFGHIJKLMNOPQRST"
    t = ""
    for i in range (len (L1)): t = dizge[L1[i]] + t
    return t

def taban10 (d):
    dizge = "ABCDEFGHIJKLMNOPQRST"
    n = 0
    for i in range (len (d)): n += dizge.index (str (d[i])) * (20 ** (len (d) - i -1))
    return n

from random import randint
try: sayı10 = abs (int (eval (input ("Bir pozitif tamsayı gir: "))))
except Exception: sayı10 = randint (0, 10**14)

sayı20 = taban20 (sayı10)
print ("\n10 tabanlı: (", sayı10, ") sayısı = 20 tabanlı: (", sayı20, ") A-T sembolüdür.", sep="")

sayı_10 = taban10 (sayı20)
print ("20 tabanlı: (", sayı20, ") sembolü = 10 tabanlı: (", sayı_10, ") sayısıdır.", sep="")
