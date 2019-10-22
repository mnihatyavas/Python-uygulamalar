#coding:iso-8859-9 T�rk�e
# p_32404.py: Pandas'la ��renci derecelerinin etiketli kategorilendirilmesi �rne�i.

from random import random
import pandas as pd

dereceler = ["Ba�ar�s�z ��renci", "Normal ��renci", "Ba�ar�l� ��renci", "Onur ��rencisi", "Y�ksek onur ��rencisi", "S�per onur ��rencisi"]
��renciNotlar� = [int ((random() * 2.6 + 1.5) * 100) / 100 for _ in range (30)]
��renciNotKategorisi = pd.cut (��renciNotlar�, [0, 2.0, 2.75, 3.5, 3.75, 3.85, 4.0], labels=dereceler)

print ("30 adet geli�ig�zel ��renci notlar� listesi:\n", ��renciNotlar�, sep="")
print ("\nHerbir ba�ar� derecesine d��en ��renci say�s�:\n", pd.value_counts (��renciNotKategorisi), sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

endeksler = ��renciNotKategorisi.codes
print ("\nHerbir notun kategori endeksi:\n", endeksler)

kategoriler = ��renciNotKategorisi.categories
print ("\n6 adet Pandas kategorik derece s�n�fland�rmas� varsay�l� sa�-kapal� aral�klar�:\n", kategoriler, sep="")

print ("\n30 adet not, endeksi ve kategorik s�n�f� d�k�m�:\n", "-"*49, sep="")
for i in range (len (��renciNotlar�)):
    endeks = endeksler [i]
    print ((i+1), ��renciNotlar� [i], endeks, kategoriler [endeks])



"""��kt�:
>python p_32404.py
30 adet geli�ig�zel ��renci notlar� listesi:
[1.62, 1.58, 2.05, 3.95, 3.03, 3.74, 1.69, 3.45, 2.43, 1.58, 2.8, 3.79, 1.6, 2.24,
 3.81, 3.13, 2.15, 3.98, 3.84, 2.26, 2.48, 3.27, 3.87, 2.93, 3.12, 3.14, 2.55,
 2.87, 2.05, 2.87]

Herbir ba�ar� derecesine d��en ��renci say�s�:
Ba�ar�l� ��renci         10
Normal ��renci            8
Ba�ar�s�z ��renci         5
S�per onur ��rencisi      3
Y�ksek onur ��rencisi     3
Onur ��rencisi            1
dtype: int64
-------------------------------------------------------------------------------

Herbir notun kategori endeksi:
 [0 0 1 5 2 3 0 2 1 0 2 4 0 1 4 2 1 5 4 1 1 2 5 2 2 2 1 2 1 2]

6 adet Pandas kategorik derece s�n�fland�rmas� varsay�l� sa�-kapal� aral�klar�:
Index(['Ba�ar�s�z ��renci', 'Normal ��renci', 'Ba�ar�l� ��renci',
       'Onur ��rencisi', 'Y�ksek onur ��rencisi', 'S�per onur ��rencisi'],
      dtype='object')

30 adet not, endeksi ve kategorik s�n�f� d�k�m�:
-------------------------------------------------
1 1.62 0 Ba�ar�s�z ��renci
2 1.58 0 Ba�ar�s�z ��renci
3 2.05 1 Normal ��renci
4 3.95 5 S�per onur ��rencisi
5 3.03 2 Ba�ar�l� ��renci
6 3.74 3 Onur ��rencisi
7 1.69 0 Ba�ar�s�z ��renci
8 3.45 2 Ba�ar�l� ��renci
9 2.43 1 Normal ��renci
10 1.58 0 Ba�ar�s�z ��renci
11 2.8 2 Ba�ar�l� ��renci
12 3.79 4 Y�ksek onur ��rencisi
13 1.6 0 Ba�ar�s�z ��renci
14 2.24 1 Normal ��renci
15 3.81 4 Y�ksek onur ��rencisi
16 3.13 2 Ba�ar�l� ��renci
17 2.15 1 Normal ��renci
18 3.98 5 S�per onur ��rencisi
19 3.84 4 Y�ksek onur ��rencisi
20 2.26 1 Normal ��renci
21 2.48 1 Normal ��renci
22 3.27 2 Ba�ar�l� ��renci
23 3.87 5 S�per onur ��rencisi
24 2.93 2 Ba�ar�l� ��renci
25 3.12 2 Ba�ar�l� ��renci
26 3.14 2 Ba�ar�l� ��renci
27 2.55 1 Normal ��renci
28 2.87 2 Ba�ar�l� ��renci
29 2.05 1 Normal ��renci
30 2.87 2 Ba�ar�l� ��renci
"""