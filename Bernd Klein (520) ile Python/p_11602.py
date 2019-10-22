# coding:iso-8859-9 Türkçe
# p_11602.py: for-range ile ardışık erimler taratarak toplamlar ve pisagor eşitliği örneği.

print ("range(10):", range (10) )
print ("list(range(10)):", list (range (10)) )
print ("list(range(4,10)):", list (range (4, 10)) )
print ("list(range(4,50,5)):", list (range (4, 50, 5)) )
print ("list(range(47,-12,-7)):", list (range (47, -12, -7)) )
#------------------------------------------------------------------------------------------

from random import randint
n = randint (1957, 2019)

toplam = 0
for i in range (1957, n+1): toplam = toplam + i
print ("\n1957'den {}'a kadar olan sayıların toplamı: {:,}'dır." .format (n, toplam) )
input ("Ent:")
#------------------------------------------------------------------------------------------

sayaç=0
print ("\n1'den ", n, "'e kadar olan sayılardan pisagor eşitliğini sağlayanların listesi:\n", "-"*76, sep="")
for a in range (1, n+1):
    for b in range (a, n):
        c = (a**2+b**2)**0.5
        if c ==  int (c):
            print ("{}^2 + {}^2 = {}^2" .format (a, b, int (c)) )
            sayaç +=1
            if sayaç%20==0: input ("\nDevam:Ent veya Çık:Ctrl_C ")


"""Çıktı:
>python p_11602.py
range(10): range(0, 10)
list(range(10)): [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(4,10)): [4, 5, 6, 7, 8, 9]
list(range(4,50,5)): [4, 9, 14, 19, 24, 29, 34, 39, 44, 49]
list(range(47,-12,-7)): [47, 40, 33, 26, 19, 12, 5, -2, -9]

1957'den 1973'a kadar olan sayıların toplamı: 33,405'dır.
Ent:

1'den 1973'e kadar olan sayılardan pisagor eşitliğini sağlayanların listesi:
----------------------------------------------------------------------------
3^2 + 4^2 = 5^2
5^2 + 12^2 = 13^2
6^2 + 8^2 = 10^2
7^2 + 24^2 = 25^2
8^2 + 15^2 = 17^2
9^2 + 12^2 = 15^2
9^2 + 40^2 = 41^2
10^2 + 24^2 = 26^2
11^2 + 60^2 = 61^2
12^2 + 16^2 = 20^2
12^2 + 35^2 = 37^2
13^2 + 84^2 = 85^2
14^2 + 48^2 = 50^2
15^2 + 20^2 = 25^2
15^2 + 36^2 = 39^2
15^2 + 112^2 = 113^2
16^2 + 30^2 = 34^2
16^2 + 63^2 = 65^2
17^2 + 144^2 = 145^2
18^2 + 24^2 = 30^2

Devam:Ent veya Çık:Ctrl_C Traceback (most recent call last):
"""