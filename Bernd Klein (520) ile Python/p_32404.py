#coding:iso-8859-9 Türkçe
# p_32404.py: Pandas'la öğrenci derecelerinin etiketli kategorilendirilmesi örneği.

from random import random
import pandas as pd

dereceler = ["Başarısız öğrenci", "Normal öğrenci", "Başarılı öğrenci", "Onur öğrencisi", "Yüksek onur öğrencisi", "Süper onur öğrencisi"]
öğrenciNotları = [int ((random() * 2.6 + 1.5) * 100) / 100 for _ in range (30)]
öğrenciNotKategorisi = pd.cut (öğrenciNotları, [0, 2.0, 2.75, 3.5, 3.75, 3.85, 4.0], labels=dereceler)

print ("30 adet gelişigüzel öğrenci notları listesi:\n", öğrenciNotları, sep="")
print ("\nHerbir başarı derecesine düşen öğrenci sayısı:\n", pd.value_counts (öğrenciNotKategorisi), sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

endeksler = öğrenciNotKategorisi.codes
print ("\nHerbir notun kategori endeksi:\n", endeksler)

kategoriler = öğrenciNotKategorisi.categories
print ("\n6 adet Pandas kategorik derece sınıflandırması varsayılı sağ-kapalı aralıkları:\n", kategoriler, sep="")

print ("\n30 adet not, endeksi ve kategorik sınıfı dökümü:\n", "-"*49, sep="")
for i in range (len (öğrenciNotları)):
    endeks = endeksler [i]
    print ((i+1), öğrenciNotları [i], endeks, kategoriler [endeks])



"""Çıktı:
>python p_32404.py
30 adet gelişigüzel öğrenci notları listesi:
[1.62, 1.58, 2.05, 3.95, 3.03, 3.74, 1.69, 3.45, 2.43, 1.58, 2.8, 3.79, 1.6, 2.24,
 3.81, 3.13, 2.15, 3.98, 3.84, 2.26, 2.48, 3.27, 3.87, 2.93, 3.12, 3.14, 2.55,
 2.87, 2.05, 2.87]

Herbir başarı derecesine düşen öğrenci sayısı:
Başarılı öğrenci         10
Normal öğrenci            8
Başarısız öğrenci         5
Süper onur öğrencisi      3
Yüksek onur öğrencisi     3
Onur öğrencisi            1
dtype: int64
-------------------------------------------------------------------------------

Herbir notun kategori endeksi:
 [0 0 1 5 2 3 0 2 1 0 2 4 0 1 4 2 1 5 4 1 1 2 5 2 2 2 1 2 1 2]

6 adet Pandas kategorik derece sınıflandırması varsayılı sağ-kapalı aralıkları:
Index(['Başarısız öğrenci', 'Normal öğrenci', 'Başarılı öğrenci',
       'Onur öğrencisi', 'Yüksek onur öğrencisi', 'Süper onur öğrencisi'],
      dtype='object')

30 adet not, endeksi ve kategorik sınıfı dökümü:
-------------------------------------------------
1 1.62 0 Başarısız öğrenci
2 1.58 0 Başarısız öğrenci
3 2.05 1 Normal öğrenci
4 3.95 5 Süper onur öğrencisi
5 3.03 2 Başarılı öğrenci
6 3.74 3 Onur öğrencisi
7 1.69 0 Başarısız öğrenci
8 3.45 2 Başarılı öğrenci
9 2.43 1 Normal öğrenci
10 1.58 0 Başarısız öğrenci
11 2.8 2 Başarılı öğrenci
12 3.79 4 Yüksek onur öğrencisi
13 1.6 0 Başarısız öğrenci
14 2.24 1 Normal öğrenci
15 3.81 4 Yüksek onur öğrencisi
16 3.13 2 Başarılı öğrenci
17 2.15 1 Normal öğrenci
18 3.98 5 Süper onur öğrencisi
19 3.84 4 Yüksek onur öğrencisi
20 2.26 1 Normal öğrenci
21 2.48 1 Normal öğrenci
22 3.27 2 Başarılı öğrenci
23 3.87 5 Süper onur öğrencisi
24 2.93 2 Başarılı öğrenci
25 3.12 2 Başarılı öğrenci
26 3.14 2 Başarılı öğrenci
27 2.55 1 Normal öğrenci
28 2.87 2 Başarılı öğrenci
29 2.05 1 Normal öğrenci
30 2.87 2 Başarılı öğrenci
"""