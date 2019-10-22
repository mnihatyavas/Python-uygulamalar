# coding:iso-8859-9 Türkçe

def dikdörtgen (a, b):
    for i in range (a): print ("*" * b)

def değiştirme (L1):
    for k in L1:
        k = k + "!.."
        print (k)

def değiştir (L1):
    for i in range (len (L1)): L1[i] = L1[i] + "!.."
    return L1

def topla (k):
    toplam = 0
    for i in range (len (k)): toplam += int (k[i])
    return toplam

def kök (k):
    while len (k) > 1: k = str (topla (k))
    return k

def faktöriyel (m):
    çarpım = 1
    for i in range (1, m+1): çarpım *=i
    return çarpım

try: x, y = eval (input ("Dikdörtgenin [satır, kolon] adetlerini gir: "))
except Exception: x = 10; y = 50

yy = 41
if y > yy: yy = y
print (x, " satır ve ", y, " kolonlu yıldızlı dikdörtgen:\n", "-"*yy, sep="")
dikdörtgen (x, y)

print()
L = [satır.strip() for satır in open ("sorular.txt")]
from pprint import pprint
print ("Orijinal liste:\n", "-"*45, sep="")
pprint (L)

print()
print ("Sonları !.. ekli liste:\n", "-"*45, sep="")
değiştirme (L)
print ("\nDeğişmeyen liste:\n", "-"*45, sep="")
pprint (L)

print()
L = değiştir (L)
print ("Değişen liste:\n", "-"*45, sep="")
pprint (L)

print()
try: b = abs (int (eval (input ("Kaç basamaklı sayı olsun: "))))
except Exception: b = 20
print()
if b == 0: b = 1
from random import randint
sayı = str (randint (10**(b-1), 10**b-1 ))
print ("[", 10**(b-1), ", ", 10**b-1, "] arası tesadüfi tamsayı: ", sayı, sep="")
print ("Sayı basamaklarının toplamı:", topla (sayı))
print ("Sayı basamaklarının toplam kökü (2 yöntemle):", int (sayı) % 9, "=", kök (sayı))

print()
# Binomiyal (n, k) = n! / (k! (n-k)!)
k = randint (0, 100)
n = randint (k, 100)
print ("Binomial ({:d},{:d}) katsayısı = {:d}" .format (n, k, int (faktöriyel (n) / (faktöriyel (k) * faktöriyel (n - k)))) )
