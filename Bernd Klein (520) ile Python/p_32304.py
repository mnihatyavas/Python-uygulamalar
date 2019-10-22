#coding:iso-8859-9 T�rk�e
# p_32304.py: S�cakl�k veri �er�evesinde NaN'lar�n d���r�lmesi ve ortalama �rne�i.

import pandas as pd

v�Bozuk = pd.read_csv ("p_32303x.txt", sep=",", decimal=".", encoding="iso:8859-9", index_col=0)
print ("Zaman ve 6 sens�rl� bozuk=NaN veri �er�evesi (ilk 10):\n", v�Bozuk.head (10), sep="")

v�Bozuk2 = v�Bozuk.dropna() # Varsay�l� axis=0
print ("\nZaman ve 6 sens�rl� bozuk=NaN SATIRLARI d��en v� (ilk 10):\n", v�Bozuk2.head (10), sep="")

print ("\nZaman ve 6 sens�rl� bozuk=NaN S�TUNLARI d��en v�:\n", v�Bozuk.dropna (axis=1), sep="")

v�Temiz = v�Bozuk.dropna (thresh=5, axis=0)
print ("\nEnaz 5 sens�r �al��an (di�er SATIRLAR d���k) v� (ilk 10):\n", v�Temiz.head (10), sep="")

ortalamaSerisi = v�Temiz.mean (axis=1) # Yatay X eksendeki sens�r verileri ortalamas�...
sens�rlerListesi = v�Temiz.columns.values
v�1 = v�Temiz.drop (sens�rlerListesi, axis=1) # Sadece zaman kolonu kal�r...
v�1 = v�1.assign (s�cakl�k=ortalamaSerisi)  # inplace=True kullan�lm�yor...
print ("\nZaman ve �al��an sens�r ortalamal� v� (ilk 10):\n", v�1.head (10), sep="")



"""��kt�:
>python p_32304.py
Zaman ve 6 sens�rl� bozuk=NaN veri �er�evesi (ilk 10):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00     14.3     13.7      NaN     14.3     13.5     13.6
06:15:00     14.5      NaN     14.0      NaN     14.5     14.7
06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
06:45:00      NaN     14.5     15.6      NaN     14.7     14.6
07:00:00     15.0     14.9     15.7     15.6      NaN     15.3
07:15:00     15.2      NaN     14.6     15.3      NaN     14.9
07:30:00     15.4     15.3     15.6     15.6      NaN     15.1
07:45:00     15.5     14.8     15.4     15.5     14.6     14.9
08:00:00     15.7      NaN     15.9      NaN     15.4     15.4
08:15:00     15.9     15.8     15.9     16.9     16.0     16.2

Zaman ve 6 sens�rl� bozuk=NaN SATIRLARI d��en v� (ilk 10):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
07:45:00     15.5     14.8     15.4     15.5     14.6     14.9
08:15:00     15.9     15.8     15.9     16.9     16.0     16.2
08:30:00     16.1     15.7     16.1     15.9     14.9     15.2
08:45:00     16.5     16.6     17.3     16.2     16.4     16.0
09:30:00     17.7     18.2     18.2     18.6     16.9     17.4
10:15:00     19.7     19.4     19.2     19.2     19.7     19.6
11:45:00     24.2     23.1     25.3     23.7     24.5     24.8
12:30:00     23.6     24.2     23.6     24.1     22.1     22.5
13:00:00     23.2     24.1     24.0     23.3     23.5     23.1

Zaman ve 6 sens�rl� bozuk=NaN S�TUNLARI d��en v�:
Empty DataFrame
Columns: []
Index: [06:00:00, 06:15:00, 06:30:00, 06:45:00, 07:00:00, 07:15:00, 07:30:00, 07
:45:00, 08:00:00, 08:15:00, 08:30:00, 08:45:00, 09:00:00, 09:15:00, 09:30:00, 09
:45:00, 10:00:00, 10:15:00, 10:30:00, 10:45:00, 11:00:00, 11:15:00, 11:30:00, 11
:45:00, 12:00:00, 12:15:00, 12:30:00, 12:45:00, 13:00:00, 13:15:00, 13:30:00, 13
:45:00, 14:00:00, 14:15:00, 14:30:00, 14:45:00, 15:00:00, 15:15:00, 15:30:00, 15
:45:00, 16:00:00, 16:15:00, 16:30:00, 16:45:00, 17:00:00, 17:15:00, 17:30:00, 17
:45:00, 18:00:00, 18:15:00, 18:30:00, 18:45:00, 19:00:00, 19:15:00]

Enaz 5 sens�r �al��an (di�er SATIRLAR d���k) v� (ilk 10):
          sens�r1  sens�r2  sens�r3  sens�r4  sens�r5  sens�r6
zaman
06:00:00     14.3     13.7      NaN     14.3     13.5     13.6
06:30:00     14.6     15.1     14.8     15.3     14.0     14.2
07:00:00     15.0     14.9     15.7     15.6      NaN     15.3
07:30:00     15.4     15.3     15.6     15.6      NaN     15.1
07:45:00     15.5     14.8     15.4     15.5     14.6     14.9
08:15:00     15.9     15.8     15.9     16.9     16.0     16.2
08:30:00     16.1     15.7     16.1     15.9     14.9     15.2
08:45:00     16.5     16.6     17.3     16.2     16.4     16.0
09:30:00     17.7     18.2     18.2     18.6     16.9     17.4
09:45:00     18.4     19.0      NaN     19.4     18.4     18.3

Zaman ve �al��an sens�r ortalamal� v� (ilk 10):
           s�cakl�k
zaman
06:00:00  13.880000
06:30:00  14.666667
07:00:00  15.300000
07:30:00  15.400000
07:45:00  15.116667
08:15:00  16.116667
08:30:00  15.650000
08:45:00  16.500000
09:30:00  17.833333
09:45:00  18.700000
"""