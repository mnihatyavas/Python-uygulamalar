# coding:iso-8859-9 T�rk�e

def taban20 (n):
    L1 = []
    if n == 0: return "A"
    while n > 0:
        L1 = L1 + [n % 20]
        n = n//20
    tt = �evir (L1)
    return tt

def �evir (L1):
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
try: say�10 = abs (int (eval (input ("Bir pozitif tamsay� gir: "))))
except Exception: say�10 = randint (0, 10**14)

say�20 = taban20 (say�10)
print ("\n10 tabanl�: (", say�10, ") say�s� = 20 tabanl�: (", say�20, ") A-T sembol�d�r.", sep="")

say�_10 = taban10 (say�20)
print ("20 tabanl�: (", say�20, ") sembol� = 10 tabanl�: (", say�_10, ") say�s�d�r.", sep="")
