# coding:iso-8859-9 T�rk�e
# p_30710a.py: A��rl�k nisbetinde tesad�fi s�f�r ve bir �retme �rne�i.

import random

def tesad�fiBirS�f�r (a��rl�k):
    geli�ig�zelSay� = random.random()
    return 1 if (geli�ig�zelSay� < a��rl�k) else 0

try: n = abs (int (input ("Ka� adet a��rl�kl� 1/0 �retsin [1 000 000]? ")))
except: n = 1000000

print ("%80 birli:", sum (tesad�fiBirS�f�r (0.8) for i in range (n)) / n)
print ("%20 birli:", sum (tesad�fiBirS�f�r (0.2) for i in range (n)) / n)
print ("%50 birli:", sum (tesad�fiBirS�f�r (0.5) for i in range (n)) / n)



"""��kt�:
>python p_30710a.py
Ka� adet a��rl�kl� 1/0 �retsin [1 000 000]? 100
%80 birli: 0.79
%20 birli: 0.22
%50 birli: 0.61

>python p_30710a.py  ** TEKRAR **
Ka� adet a��rl�kl� 1/0 �retsin [1 000 000]? 10000
%80 birli: 0.7984
%20 birli: 0.1981
%50 birli: 0.5009

>python p_30710a.py  ** TEKRAR **
Ka� adet a��rl�kl� 1/0 �retsin [1 000 000]?
%80 birli: 0.80008
%20 birli: 0.199658
%50 birli: 0.50013
"""