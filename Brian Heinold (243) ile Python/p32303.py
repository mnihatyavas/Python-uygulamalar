# coding:iso-8859-9 Türkçe

from random import randint

def faktöriyel (n):
    if n==0: return 1
    else: return n * faktöriyel (n - 1)

def faktör (n, L=[]):
    for i in range (2, n//2+1):
        if n % i == 0:
            return L+[i]+faktör (n//i)
    return L+[n]

try: sayı = abs (int (eval (input ("Faktöriyeli hesaplanacak sayıyı girin: "))))
except Exception: sayı = randint (0,100)

print (sayı, " sayısının faktöriyeli:", faktöriyel (sayı) )

print()
# Asal faktörlerin çarpımı sayı'yı verir, yoksa asal olan sayının kendisi döner...
print (sayı, " sayısının asal faktörleri:", faktör (sayı) )