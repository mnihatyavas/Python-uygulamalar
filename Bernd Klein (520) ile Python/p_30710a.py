# coding:iso-8859-9 Türkçe
# p_30710a.py: Ağırlık nisbetinde tesadüfi sıfır ve bir üretme örneği.

import random

def tesadüfiBirSıfır (ağırlık):
    gelişigüzelSayı = random.random()
    return 1 if (gelişigüzelSayı < ağırlık) else 0

try: n = abs (int (input ("Kaç adet ağırlıklı 1/0 üretsin [1 000 000]? ")))
except: n = 1000000

print ("%80 birli:", sum (tesadüfiBirSıfır (0.8) for i in range (n)) / n)
print ("%20 birli:", sum (tesadüfiBirSıfır (0.2) for i in range (n)) / n)
print ("%50 birli:", sum (tesadüfiBirSıfır (0.5) for i in range (n)) / n)



"""Çıktı:
>python p_30710a.py
Kaç adet ağırlıklı 1/0 üretsin [1 000 000]? 100
%80 birli: 0.79
%20 birli: 0.22
%50 birli: 0.61

>python p_30710a.py  ** TEKRAR **
Kaç adet ağırlıklı 1/0 üretsin [1 000 000]? 10000
%80 birli: 0.7984
%20 birli: 0.1981
%50 birli: 0.5009

>python p_30710a.py  ** TEKRAR **
Kaç adet ağırlıklı 1/0 üretsin [1 000 000]?
%80 birli: 0.80008
%20 birli: 0.199658
%50 birli: 0.50013
"""