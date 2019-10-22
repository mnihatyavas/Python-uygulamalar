# coding:iso-8859-9 Türkçe

s={}
for i in range (65, 91): s[chr (i)] = i
print (s)

print()
s1 = s
print (s1)

print()
s2 = s.copy()
print (s2)

print()
from random import randint
karakter = chr (randint (0, 256)).upper()
if karakter in s: print (karakter, "-->", s[karakter])
else: print (karakter, "sözlükte mevcut değil.")

print()
for anahtar in s: print (anahtar, ":", s[anahtar])

print()
print (s)
print()
print (list (s))
print()
print (list (s.keys()))
print()
print (list (s.values()))
print()
print (list (s.items()))

print()
L = [x[0] for x in s.items() if 75 < x[1] < 85]
print (L)
print()
print ([x[1] for x in s.items() if "L" <= x[0] <= "T"])

print()
s3 = {chr(i):i for i in range (122, 96, -1)} # Kapsamlı sözlük yaratma yöntemi...
print (s3)

print()
s4 = dict ({chr (i): i for i in range (97, 123)})
print (s4)
