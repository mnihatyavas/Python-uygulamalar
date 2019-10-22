#coding:iso-8859-9 T�rk�e
# p_32402.py: Pandas kategorik nesneyle grupland�rma �rne�i.

from random import random

def gruplar�Yarat (altS�n�r, art��, adet):
    gruplar = []
    for alt in range (altS�n�r, (altS�n�r + adet * art�� + 1), art��):
        gruplar.append ( (alt, alt + art��) )
    return gruplar

gruplar = gruplar�Yarat (altS�n�r=50, art��=4, adet=15)
insanKilolar� = [int ((random() * 60 + 51) * 10) / 10.0 for _ in range (30)]
print ("�nsan kilolar� s�n�fland�rmas�:\n", gruplar,
    "\n\n30 adet geli�ig�zel insan a��rl�klar�:\n", insanKilolar�, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

import pandas as pd

gruplar2 = pd.IntervalIndex.from_tuples (gruplar)
kategorikNesne = pd.cut (insanKilolar�, gruplar2)
print ("\nVerili insan kilolar� ve sa�-kapal� s�n�fland�rmas�n�n Pandas kategorik nesnesi:", kategorikNesne, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

gruplar3 = pd.IntervalIndex.from_tuples (gruplar, closed="left") # right/default, left, both, neither
kategorikNesne = pd.cut (insanKilolar�, gruplar3)
print ("\nVerili insan kilolar� ve sol-kapal� s�n�fland�rmas�n�n Pandas kategorik nesnesi:", kategorikNesne, sep="")



"""��kt�:
>python p_32402.py
�nsan kilolar� s�n�fland�rmas�:
[(50, 54), (54, 58), (58, 62), (62, 66), (66, 70), (70, 74), (74, 78), (78, 82),
 (82, 86), (86, 90), (90, 94), (94, 98), (98, 102), (102, 106), (106, 110), (110, 114)]

30 adet geli�ig�zel insan a��rl�klar�:
[51.8, 52.4, 87.8, 59.1, 77.9, 91.3, 59.2, 93.3, 102.6, 79.4, 107.3, 77.3, 61.4,
 83.6, 99.8, 97.8, 100.9, 92.1, 87.3, 103.5, 70.1, 93.9, 92.9, 87.5, 79.3, 75.5,
 103.2, 88.6, 110.5, 90.2]
-------------------------------------------------------------------------------

Verili insan kilolar� ve sa�-kapal� s�n�fland�rmas�n�n Pandas kategorik nesnesi:
[(50, 54], (50, 54], (86, 90], (58, 62], (74, 78], ..., (74, 78], (102, 106], (86, 90], (110, 114], (90, 94]]
Length: 30
Categories (16, interval[int64]): [(50, 54] < (54, 58] < (58, 62] < (62, 66] ... (98, 102] <
    (102, 106] < (106, 110] < (110, 114]]
-------------------------------------------------------------------------------

Verili insan kilolar� ve sol-kapal� s�n�fland�rmas�n�n Pandas kategorik nesnesi:
[[50, 54), [50, 54), [86, 90), [58, 62), [74, 78), ..., [74, 78), [102, 106), [86, 90), [110, 114), [90, 94)]
Length: 30
Categories (16, interval[int64]): [[50, 54) < [54, 58) < [58, 62) < [62, 66) ...[98, 102) <
    [102, 106) < [106, 110) < [110, 114)]
"""