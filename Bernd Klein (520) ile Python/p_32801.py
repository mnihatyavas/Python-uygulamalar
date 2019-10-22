#coding:iso-8859-9 T�rk�e
# p_32801.py: Pandas ve datetime ile zaman serileri t�retme �rne�i.

import pandas as pd
from datetime import datetime, timedelta
from random import random

g�nSay�s� = 15
ilk = datetime (2019, 8, 13)
tarihler = [ilk - timedelta (days=i) for i in range (g�nSay�s�)]
de�erler = [int (random() * 100) for _ in range (g�nSay�s�)]
zamanSerisi = pd.Series (de�erler, index=tarihler)

print ("Pandas zaman serisi:\n", zamanSerisi, sep="")
print ("\nZaman serisinin tipi:", type (zamanSerisi))
print ("\nZaman serisinin endeksi:\n", zamanSerisi.index, sep="")
print ("\nZaman serisinin de�erleri:", zamanSerisi.values)
#---------------------------------------------------------------------------------------------------

de�erler2 = [int (random() * 100) for _ in range (g�nSay�s�)]
zs2 = pd.Series (de�erler2, index=tarihler)

print ("\n2.zaman serisi:\n", zs2, sep="")
#---------------------------------------------------------------------------------------------------

print ("\nHer iki zaman serisinin toplam�:\n", (zamanSerisi + zs2), sep="")
print ("\nHer iki zaman serisinin ortalamas�:\n", (zamanSerisi + zs2) / 2, sep="")
print ("-"*30)
#---------------------------------------------------------------------------------------------------

g�nSay�s� = 10
ilk = datetime (2019, 8, 13)
tarihler = [ilk - timedelta (days=i) for i in range (g�nSay�s�)]
tarihler2 = [ilk - timedelta (days=i) for i in range (5, g�nSay�s� + 5)]
de�erler = [int (random() * 100) for _ in range (g�nSay�s�)]
de�erler2 = [int (random() * 100) for _ in range (g�nSay�s�)]
zs = pd.Series (de�erler, index=tarihler)
zs2 = pd.Series (de�erler2, index=tarihler2)
print ("\n�lk zaman serisi:\n", zs,
    "\n\n�kinci zaman serisi:\n", zs2,
    "\n\nHeriki zaman serisinin kesi�en toplam�:\n", (zs + zs2), sep="")



"""��kt�:
>python p_32801.py
Pandas zaman serisi:
2019-08-13    14
2019-08-12    15
2019-08-11    28
2019-08-10    25
2019-08-09    21
2019-08-08    74
2019-08-07    38
2019-08-06    62
2019-08-05    29
2019-08-04    66
2019-08-03    12
2019-08-02    55
2019-08-01    22
2019-07-31    78
2019-07-30    29
dtype: int64

Zaman serisinin tipi: <class 'pandas.core.series.Series'>

Zaman serisinin endeksi:
DatetimeIndex(['2019-08-13', '2019-08-12', '2019-08-11', '2019-08-10',
               '2019-08-09', '2019-08-08', '2019-08-07', '2019-08-06',
               '2019-08-05', '2019-08-04', '2019-08-03', '2019-08-02',
               '2019-08-01', '2019-07-31', '2019-07-30'],
              dtype='datetime64[ns]', freq=None)

Zaman serisinin de�erleri: [14 15 28 25 21 74 38 62 29 66 12 55 22 78 29]

2.zaman serisi:
2019-08-13    87
2019-08-12    23
2019-08-11    21
2019-08-10    42
2019-08-09    42
2019-08-08    69
2019-08-07    49
2019-08-06    80
2019-08-05    81
2019-08-04    38
2019-08-03    38
2019-08-02    73
2019-08-01    17
2019-07-31    97
2019-07-30    54
dtype: int64

Her iki zaman serisinin toplam�:
2019-08-13    101
2019-08-12     38
2019-08-11     49
2019-08-10     67
2019-08-09     63
2019-08-08    143
2019-08-07     87
2019-08-06    142
2019-08-05    110
2019-08-04    104
2019-08-03     50
2019-08-02    128
2019-08-01     39
2019-07-31    175
2019-07-30     83
dtype: int64

Her iki zaman serisinin ortalamas�:
2019-08-13    50.5
2019-08-12    19.0
2019-08-11    24.5
2019-08-10    33.5
2019-08-09    31.5
2019-08-08    71.5
2019-08-07    43.5
2019-08-06    71.0
2019-08-05    55.0
2019-08-04    52.0
2019-08-03    25.0
2019-08-02    64.0
2019-08-01    19.5
2019-07-31    87.5
2019-07-30    41.5
dtype: float64
------------------------------

�lk zaman serisi:
2019-08-13    35
2019-08-12    83
2019-08-11    63
2019-08-10    17
2019-08-09    90
2019-08-08    93
2019-08-07    68
2019-08-06    67
2019-08-05    73
2019-08-04    30
dtype: int64

�kinci zaman serisi:
2019-08-08    22
2019-08-07    51
2019-08-06    69
2019-08-05    31
2019-08-04    78
2019-08-03    95
2019-08-02    64
2019-08-01    11
2019-07-31    45
2019-07-30     3
dtype: int64

Heriki zaman serisinin kesi�en toplam�:
2019-07-30      NaN
2019-07-31      NaN
2019-08-01      NaN
2019-08-02      NaN
2019-08-03      NaN
2019-08-04    108.0
2019-08-05    104.0
2019-08-06    136.0
2019-08-07    119.0
2019-08-08    115.0
2019-08-09      NaN
2019-08-10      NaN
2019-08-11      NaN
2019-08-12      NaN
2019-08-13      NaN
dtype: float64
"""