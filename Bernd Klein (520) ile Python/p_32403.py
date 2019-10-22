#coding:iso-8859-9 Türkçe
# p_32403.py: Pandas kategorik nesnesinin detayları örneği.

from random import random
import pandas as pd

insanKiloları = [int ((random() * 63 + 51) * 10) / 10.0 for _ in range (30)]
print ("30 adet gelişigüzel insan ağırlıkları:\n", insanKiloları, sep="")

kategorikNesne = pd.cut (insanKiloları, 18)
# Verili kiloların: (enbüyük - enküçük) / 18 = (110.7-52.6)/18=3.228; (52.6, 55.828],..,(107.472, 110.7]
print ("\nVerili 30 adet insan kiloları ve varsayılı sağ-kapalı 18 adet sınıflandırmasının Pandas kategorik nesnesi:", kategorikNesne, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

seri = [_ for _ in range (50, 115, 4)]
print ("\n50->114 arası 4'er artan insan kiloları serisi:\n", seri, sep="")
kategorikNesne = pd.cut (insanKiloları, seri)
print ("\nVerili 30 adet insan kiloları ve 17 adet kilo serisinin Pandas kategorik nesnesi:\n", kategorikNesne, sep="")
print ("-"*79)
#--------------------------------------------------------------------------------------------------------

print ("\nToplam 30 ağırlığın, herbir kategoriye düşen ağırlık dağılımları:\n", pd.value_counts (kategorikNesne), sep="")

endeksler = kategorikNesne.codes
print ("\nHerbir ağırlığın kategori endeksi:\n", endeksler)

kategoriler = kategorikNesne.categories
print ("\n17 adet Pandas kategorik kilo sınıflandırması varsayılı sağ-kapalı aralıkları:\n", kategoriler, sep="")

print ("\n30 adet kilo, endeksi ve kategorik sınıfı dökümü:\n", "-"*49, sep="")
for i in range (len (insanKiloları)):
    endeks = endeksler [i]
    print ((i+1), insanKiloları [i], endeks, kategoriler [endeks])



"""Çıktı:
>python p_32403.py
30 adet gelişigüzel insan ağırlıkları:
[79.1, 56.0, 65.6, 107.6, 77.8, 73.8, 96.4, 91.7, 85.3, 54.4, 102.9, 70.4, 75.5,
 90.0, 63.8, 92.0, 61.9, 85.4, 75.6, 85.5, 90.3, 93.5, 106.5, 52.1, 82.5, 71.1,
59.3, 87.7, 62.9, 90.8]

Verili 30 adet insan kiloları ve varsayılı sağ-kapalı 18 adet sınıflandırmasının
 Pandas kategorik nesnesi:[(76.767, 79.85], (55.183, 58.267], (64.433, 67.517],
(104.517, 107.6], (76.767, 79.85], ..., (70.6, 73.683], (58.267, 61.35], (86.017, 89.1],
 (61.35, 64.433], (89.1, 92.183]]
Length: 30
Categories (18, interval[float64]): [(52.044, 55.183] < (55.183, 58.267] < (58.267, 61.35] < (61.35, 64.433]
 ... (95.267, 98.35] < (98.35, 101.433] < (101.433, 104.517] < (104.517, 107.6]]
-------------------------------------------------------------------------------

50->114 arası 4'er artan insan kiloları serisi:
[50, 54, 58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106, 110, 114]

Verili 30 adet insan kiloları ve 17 adet kilo serisinin Pandas kategorik nesnesi:
[(78, 82], (54, 58], (62, 66], (106, 110], (74, 78], ..., (70, 74], (58, 62], (86, 90], (62, 66], (90, 94]]
Length: 30
Categories (16, interval[int64]): [(50, 54] < (54, 58] < (58, 62] < (62, 66]
 ... (98, 102] < (102, 106] < (106, 110] < (110, 114]]
-------------------------------------------------------------------------------

Toplam 30 ağırlığın, herbir kategoriye düşen ağırlık dağılımları:
(90, 94]      5
(82, 86]      4
(74, 78]      3
(70, 74]      3
(62, 66]      3
(106, 110]    2
(86, 90]      2
(58, 62]      2
(54, 58]      2
(102, 106]    1
(94, 98]      1
(78, 82]      1
(50, 54]      1
(110, 114]    0
(98, 102]     0
(66, 70]      0
dtype: int64

Herbir ağırlığın kategori endeksi:
[ 7  1  3 14  6  5 11 10  8  1 13  5  6  9  3 10  2  8  6  8 10 10 14  0
  8  5  2  9  3 10]

17 adet Pandas kategorik kilo sınıflandırması varsayılı sağ-kapalı aralıkları:
IntervalIndex([(50, 54], (54, 58], (58, 62], (62, 66], (66, 70] ... (94, 98], (98, 102], (102, 106], (106, 110], (110, 114]],
              closed='right',
              dtype='interval[int64]')

30 adet kilo, endeksi ve kategorik sınıfı dökümü:
-------------------------------------------------
1 79.1 7 (78, 82]
2 56.0 1 (54, 58]
3 65.6 3 (62, 66]
4 107.6 14 (106, 110]
5 77.8 6 (74, 78]
6 73.8 5 (70, 74]
7 96.4 11 (94, 98]
8 91.7 10 (90, 94]
9 85.3 8 (82, 86]
10 54.4 1 (54, 58]
11 102.9 13 (102, 106]
12 70.4 5 (70, 74]
13 75.5 6 (74, 78]
14 90.0 9 (86, 90]
15 63.8 3 (62, 66]
16 92.0 10 (90, 94]
17 61.9 2 (58, 62]
18 85.4 8 (82, 86]
19 75.6 6 (74, 78]
20 85.5 8 (82, 86]
21 90.3 10 (90, 94]
22 93.5 10 (90, 94]
23 106.5 14 (106, 110]
24 52.1 0 (50, 54]
25 82.5 8 (82, 86]
26 71.1 5 (70, 74]
27 59.3 2 (58, 62]
28 87.7 9 (86, 90]
29 62.9 3 (62, 66]
30 90.8 10 (90, 94]
"""