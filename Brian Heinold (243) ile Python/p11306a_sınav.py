# coding:iso-8859-9 T�rk�e

def dikd�rtgen (a, b):
    for i in range (a): print ("*" * b)

def de�i�tirme (L1):
    for k in L1:
        k = k + "!.."
        print (k)

def de�i�tir (L1):
    for i in range (len (L1)): L1[i] = L1[i] + "!.."
    return L1

def topla (k):
    toplam = 0
    for i in range (len (k)): toplam += int (k[i])
    return toplam

def k�k (k):
    while len (k) > 1: k = str (topla (k))
    return k

def fakt�riyel (m):
    �arp�m = 1
    for i in range (1, m+1): �arp�m *=i
    return �arp�m

try: x, y = eval (input ("Dikd�rtgenin [sat�r, kolon] adetlerini gir: "))
except Exception: x = 10; y = 50

yy = 41
if y > yy: yy = y
print (x, " sat�r ve ", y, " kolonlu y�ld�zl� dikd�rtgen:\n", "-"*yy, sep="")
dikd�rtgen (x, y)

print()
L = [sat�r.strip() for sat�r in open ("sorular.txt")]
from pprint import pprint
print ("Orijinal liste:\n", "-"*45, sep="")
pprint (L)

print()
print ("Sonlar� !.. ekli liste:\n", "-"*45, sep="")
de�i�tirme (L)
print ("\nDe�i�meyen liste:\n", "-"*45, sep="")
pprint (L)

print()
L = de�i�tir (L)
print ("De�i�en liste:\n", "-"*45, sep="")
pprint (L)

print()
try: b = abs (int (eval (input ("Ka� basamakl� say� olsun: "))))
except Exception: b = 20
print()
if b == 0: b = 1
from random import randint
say� = str (randint (10**(b-1), 10**b-1 ))
print ("[", 10**(b-1), ", ", 10**b-1, "] aras� tesad�fi tamsay�: ", say�, sep="")
print ("Say� basamaklar�n�n toplam�:", topla (say�))
print ("Say� basamaklar�n�n toplam k�k� (2 y�ntemle):", int (say�) % 9, "=", k�k (say�))

print()
# Binomiyal (n, k) = n! / (k! (n-k)!)
k = randint (0, 100)
n = randint (k, 100)
print ("Binomial ({:d},{:d}) katsay�s� = {:d}" .format (n, k, int (fakt�riyel (n) / (fakt�riyel (k) * fakt�riyel (n - k)))) )
