# coding:iso-8859-9 T�rk�e

from random import randint

def fakt�riyel (n):
    if n==0: return 1
    else: return n * fakt�riyel (n - 1)

def fakt�r (n, L=[]):
    for i in range (2, n//2+1):
        if n % i == 0:
            return L+[i]+fakt�r (n//i)
    return L+[n]

try: say� = abs (int (eval (input ("Fakt�riyeli hesaplanacak say�y� girin: "))))
except Exception: say� = randint (0,100)

print (say�, " say�s�n�n fakt�riyeli:", fakt�riyel (say�) )

print()
# Asal fakt�rlerin �arp�m� say�'y� verir, yoksa asal olan say�n�n kendisi d�ner...
print (say�, " say�s�n�n asal fakt�rleri:", fakt�r (say�) )