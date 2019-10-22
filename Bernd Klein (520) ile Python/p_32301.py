#coding:iso-8859-9 T�rk�e
# p_32301.py: Farkl� sens�rlerin g�nl�k s�cakl�k veri �er�evesi �rne�i.

import pandas as pd

v� = pd.read_csv ("p_32301x.txt", sep=";", decimal=",", encoding="iso:8859-9")
print ("\nHer 15 dk.da bir al�nan 6 farkl� sens�rl� hava s�cakl��� (ilk 4) verisi:\n", v�.loc [:3], sep="")

v�2 = v�.mean() # Varsay�l� axis=0: dikey y verileri ortalamas�...
print ("\nDikey Y ekseni boyunca 6 sens�r�n herbirinin g�nboyu ortalamas�:\n", v�2, sep="")

v�3 = v�.mean (axis=1) # axis=1: yatay x verileri ortalamas�...
print ("\nYatay X ekseni enince 6 farkl� sens�r�n g�nl�k [6->19 aras�] ortalamas�:\n",
    v�3.head (3), "\n", v�3.tail (3), sep="")

sens�rler = v�.columns.values [1:]
v�4 = v�.drop (sens�rler, axis=1) # T�m sens�r kolonlar� d���r�l�yor...
print ("\nSens�r kolonlar� d���r�len tablonun ilk 5 sat�r�:\n", v�4.head(), sep="")

v�4 = v�4.assign (s�cakl�k=v�3)
# Alternatifi: v�4.loc [:,"s�cakl�k"] = v�3
print ("\nOrtalama s�cakl�k kolonu eklenen tablonun ilk 5 sat�r�:\n", v�4.head(), sep="")

v�5 = v�.assign (s�cakl�k=v�3)
print ("\nOrtalama s�cakl�k kolonu eklenen tablo:\n", v�5, sep="")



"""��kt�:
>python p_32301a.py

Her 15 dk.da bir al�nan 6 farkl� sens�rl� hava s�cakl��� (ilk 4) verisi:
      zaman  sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
0  06:00:00     14.3     13.7     14.2     14.3     13.5     13.6
1  06:15:00     14.5     14.5     14.0     15.0     14.5     14.7
2  06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
3  06:45:00     14.8     14.5     15.6     15.2     14.7     14.6

Dikey Y ekseni boyunca 6 sens�r�n herbirinin g�nboyu ortalamas�:
sens�r1    19.775926
sens�r2    19.757407
sens�r3    19.840741
sens�r4    20.187037
sens�r5    19.181481
sens�r6    19.437037
dtype: float64

Yatay X ekseni enince 6 farkl� sens�r�n g�nl�k [6->19 aras�] ortalamas�:
0    13.933333
1    14.533333
2    14.666667
dtype: float64
51    19.050000
52    19.250000
53    19.116667
dtype: float64

Sens�r kolonlar� d���r�len tablonun ilk 5 sat�r�:
      zaman
0  06:00:00
1  06:15:00
2  06:30:00
3  06:45:00
4  07:00:00

Ortalama s�cakl�k kolonu eklenen tablonun ilk 5 sat�r�:
      zaman   s�cakl�k
0  06:00:00  13.933333
1  06:15:00  14.533333
2  06:30:00  14.666667
3  06:45:00  14.900000
4  07:00:00  15.083333

Ortalama s�cakl�k kolonu eklenen tablo:
       zaman  sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6   s�cakl�k
0   06:00:00     14.3     13.7     14.2     14.3     13.5     13.6  13.933333
1   06:15:00     14.5     14.5     14.0     15.0     14.5     14.7  14.533333
2   06:30:00     14.6     15.1     14.8     15.3     14.0     14.2  14.666667
3   06:45:00     14.8     14.5     15.6     15.2     14.7     14.6  14.900000
4   07:00:00     15.0     14.9     15.7     15.6     14.0     15.3  15.083333
5   07:15:00     15.2     15.2     14.6     15.3     15.5     14.9  15.116667
6   07:30:00     15.4     15.3     15.6     15.6     14.7     15.1  15.283333
7   07:45:00     15.5     14.8     15.4     15.5     14.6     14.9  15.116667
8   08:00:00     15.7     15.6     15.9     16.2     15.4     15.4  15.700000
9   08:15:00     15.9     15.8     15.9     16.9     16.0     16.2  16.116667
10  08:30:00     16.1     15.7     16.1     15.9     14.9     15.2  15.650000
11  08:45:00     16.5     16.6     17.3     16.2     16.4     16.0  16.500000
12  09:00:00     16.8     17.3     17.7     17.8     15.9     16.1  16.933333
13  09:15:00     17.1     17.5     17.5     17.3     16.6     16.8  17.133333
14  09:30:00     17.7     18.2     18.2     18.6     16.9     17.4  17.833333
15  09:45:00     18.4     19.0     19.0     19.4     18.4     18.3  18.750000
16  10:00:00     19.0     19.7     18.8     18.9     17.5     18.9  18.800000
17  10:15:00     19.7     19.4     19.2     19.2     19.7     19.6  19.466667
18  10:30:00     20.4     19.4     20.0     21.0     20.2     19.8  20.133333
19  10:45:00     21.1     20.9     22.2     21.9     19.7     20.5  21.050000
20  11:00:00     21.8     21.3     20.9     23.2     21.1     20.5  21.466667
21  11:15:00     22.6     22.7     23.7     22.8     22.9     22.1  22.800000
22  11:30:00     23.4     22.7     23.0     24.5     22.3     22.9  23.133333
23  11:45:00     24.2     23.1     25.3     23.7     24.5     24.8  24.266667
24  12:00:00     24.0     23.1     23.1     24.8     22.5     22.7  23.366667
25  12:15:00     23.8     23.7     24.8     25.1     22.2     22.4  23.666667
26  12:30:00     23.6     24.2     23.6     24.1     22.1     22.5  23.350000
27  12:45:00     23.4     22.6     23.7     24.4     21.8     23.8  23.283333
28  13:00:00     23.2     24.1     24.0     23.3     23.5     23.1  23.533333
29  13:15:00     23.1     22.8     23.2     22.5     23.2     22.2  22.833333
30  13:30:00     22.9     21.9     22.9     24.3     22.9     23.0  22.983333
31  13:45:00     22.7     23.3     22.2     22.2     21.0     23.0  22.400000
32  14:00:00     22.5     23.0     22.1     24.1     22.5     22.7  22.816667
33  14:15:00     22.3     22.9     21.9     22.3     22.5     21.1  22.166667
34  14:30:00     22.1     21.9     22.3     22.2     21.2     22.1  21.966667
35  14:45:00     22.0     21.9     21.5     22.3     20.2     21.3  21.533333
36  15:00:00     21.8     22.9     22.2     22.8     21.0     21.9  22.100000
37  15:15:00     21.6     21.3     21.7     21.7     21.9     21.1  21.550000
38  15:30:00     21.4     21.3     21.7     21.9     21.0     21.7  21.500000
39  15:45:00     21.3     21.6     21.6     22.6     20.5     21.0  21.433333
40  16:00:00     21.1     21.6     20.7     20.6     19.9     21.4  20.883333
41  16:15:00     20.9     20.6     20.8     20.5     20.3     21.6  20.783333
42  16:30:00     20.8     20.7     20.7     20.4     20.2     19.6  20.400000
43  16:45:00     20.6     21.4     20.3     21.4     19.1     21.2  20.666667
44  17:00:00     20.4     19.5     20.3     21.8     19.9     19.2  20.183333
45  17:15:00     20.3     20.7     19.6     21.3     19.8     19.0  20.116667
46  17:30:00     20.1     20.5     19.7     19.7     18.7     19.7  19.733333
47  17:45:00     19.9     20.4     19.4     21.1     20.0     20.5  20.216667
48  18:00:00     19.8     20.0     19.1     19.7     20.1     20.2  19.816667
49  18:15:00     19.6     19.9     19.2     19.9     20.0     18.6  19.533333
50  18:30:00     19.5     19.1     19.2     19.7     18.3     18.3  19.016667
51  18:45:00     19.3     18.7     20.3     19.0     18.8     18.2  19.050000
52  19:00:00     19.2     18.7     20.1     19.9     18.3     19.3  19.250000
53  19:15:00     19.0     19.7     18.9     19.2     18.5     19.4  19.116667
"""