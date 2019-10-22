# coding:iso-8859-9 T�rk�e
# p_32105.py: Geli�ig�zel (12x11) say�l� veri �er�evesinin endeks-kolon-yenidenEndeks �rne�i.

import pandas as pd
import numpy as np

adlar = ['Bekir', 'Fadime', 'Memet', 'Han�m', 'Hatice', "S�heyla", "Zeliha", "Nihat", "Song�l", "Nedim", "Sevim"]
ayEndeksi = ["Ocak", "�ubat", "Mart", "Nisan", "May�s", "Haziran", "Temmuz", "A�ustos", "Eyl�l", "Ekim", "Kas�m", "Aral�k"]
v� = pd.DataFrame ( (np.random.randn (12, 11) * 2000 + 3000).round (0),
    columns=adlar, index=ayEndeksi)

print ("Aylara endeksli 2019 y�l� bor�-alacak tablosu:\n", v�, sep="")
print ("\nAdlara endeksli 2019 y�l� ayl�k bor�-alacak tablosu:\n", v�.T, sep="")
print ("\nAdlara endeksli 2019 y�l� 3 ayl�k bor�-alacak tablosu:\n", v�.T.reindex (columns=["Haziran", "Eyl�l", "Aral�k"]), sep="")
print ("\n3 ki�inin aylara endeksli 2019 y�l� ayl�k bor�-alacak tablosu:\n", v�.reindex (columns=["Hatice", "Nihat", "Sevim"]), sep="")
print ("\n3 aya endeksli 2019 y�l� ayl�k bor�-alacak tablosu:\n", v�.reindex (index=["Haziran", "Eyl�l", "Aral�k"]), sep="")
print ("\n3 ki�inin 3 aya endeksli 2019 y�l� ayl�k bor�-alacak tablosu:\n", v�.reindex (index=["Haziran", "Eyl�l", "Aral�k"], columns=["Hatice", "Nihat", "Sevim"]), sep="")



"""��kt�:
>python p_32105.py
Aylara endeksli 2019 y�l� bor�-alacak tablosu:
          Bekir  Fadime   Memet   Han�m  ...   Nihat  Song�l   Nedim   Sevim
Ocak     4807.0  1236.0  2912.0  3638.0  ...  4522.0   428.0  4304.0  5299.0
�ubat    5565.0  3320.0  -520.0  2154.0  ...  5592.0  1444.0  5313.0  5368.0
Mart     2136.0  2690.0  2126.0  3371.0  ...  5158.0   340.0  1729.0   196.0
Nisan    4600.0  2161.0  4524.0  2953.0  ...  5211.0  1088.0  -236.0  1061.0
May�s    2512.0  4720.0  4656.0  3951.0  ...  4692.0  2162.0   344.0  2328.0
Haziran  4202.0  -445.0  1686.0  4077.0  ...  4843.0  4196.0   805.0  1908.0
Temmuz    989.0  4719.0  1029.0  2142.0  ...   356.0  3055.0  4468.0  7985.0
A�ustos  2645.0  2640.0  2518.0  2361.0  ...  2289.0  4251.0   721.0  3086.0
Eyl�l    5670.0   995.0  2156.0  2814.0  ...  7201.0  1743.0  3915.0  2711.0
Ekim     -328.0  2367.0  3241.0  1238.0  ...  2992.0  3296.0  1956.0  3544.0
Kas�m     792.0  2886.0 -1596.0  2690.0  ...  2396.0  6568.0  5190.0  3360.0
Aral�k   1266.0  -943.0  1775.0  4938.0  ...  4876.0  1170.0  1634.0  2344.0

[12 rows x 11 columns]

Adlara endeksli 2019 y�l� ayl�k bor�-alacak tablosu:
           Ocak   �ubat    Mart   Nisan  ...   Eyl�l    Ekim   Kas�m  Aral�k
Bekir    4807.0  5565.0  2136.0  4600.0  ...  5670.0  -328.0   792.0  1266.0
Fadime   1236.0  3320.0  2690.0  2161.0  ...   995.0  2367.0  2886.0  -943.0
Memet    2912.0  -520.0  2126.0  4524.0  ...  2156.0  3241.0 -1596.0  1775.0
Han�m    3638.0  2154.0  3371.0  2953.0  ...  2814.0  1238.0  2690.0  4938.0
Hatice    465.0  3139.0  4746.0  1769.0  ...  4875.0 -1045.0  1052.0  2669.0
S�heyla  1437.0  3295.0  2034.0  1250.0  ...  4333.0  2764.0  4587.0  -996.0
Zeliha   3307.0  2491.0  5806.0  2385.0  ...  5122.0  3789.0  2133.0  2505.0
Nihat    4522.0  5592.0  5158.0  5211.0  ...  7201.0  2992.0  2396.0  4876.0
Song�l    428.0  1444.0   340.0  1088.0  ...  1743.0  3296.0  6568.0  1170.0
Nedim    4304.0  5313.0  1729.0  -236.0  ...  3915.0  1956.0  5190.0  1634.0
Sevim    5299.0  5368.0   196.0  1061.0  ...  2711.0  3544.0  3360.0  2344.0

[11 rows x 12 columns]

Adlara endeksli 2019 y�l� 3 ayl�k bor�-alacak tablosu:
         Haziran   Eyl�l  Aral�k
Bekir     4202.0  5670.0  1266.0
Fadime    -445.0   995.0  -943.0
Memet     1686.0  2156.0  1775.0
Han�m     4077.0  2814.0  4938.0
Hatice    5059.0  4875.0  2669.0
S�heyla   6098.0  4333.0  -996.0
Zeliha    4592.0  5122.0  2505.0
Nihat     4843.0  7201.0  4876.0
Song�l    4196.0  1743.0  1170.0
Nedim      805.0  3915.0  1634.0
Sevim     1908.0  2711.0  2344.0

3 ki�inin aylara endeksli 2019 y�l� ayl�k bor�-alacak tablosu:
         Hatice   Nihat   Sevim
Ocak      465.0  4522.0  5299.0
�ubat    3139.0  5592.0  5368.0
Mart     4746.0  5158.0   196.0
Nisan    1769.0  5211.0  1061.0
May�s    2238.0  4692.0  2328.0
Haziran  5059.0  4843.0  1908.0
Temmuz   -200.0   356.0  7985.0
A�ustos  4659.0  2289.0  3086.0
Eyl�l    4875.0  7201.0  2711.0
Ekim    -1045.0  2992.0  3544.0
Kas�m    1052.0  2396.0  3360.0
Aral�k   2669.0  4876.0  2344.0

3 aya endeksli 2019 y�l� ayl�k bor�-alacak tablosu:
          Bekir  Fadime   Memet   Han�m  ...   Nihat  Song�l   Nedim   Sevim
Haziran  4202.0  -445.0  1686.0  4077.0  ...  4843.0  4196.0   805.0  1908.0
Eyl�l    5670.0   995.0  2156.0  2814.0  ...  7201.0  1743.0  3915.0  2711.0
Aral�k   1266.0  -943.0  1775.0  4938.0  ...  4876.0  1170.0  1634.0  2344.0

[3 rows x 11 columns]

3 ki�inin 3 aya endeksli 2019 y�l� ayl�k bor�-alacak tablosu:
         Hatice   Nihat   Sevim
Haziran  5059.0  4843.0  1908.0
Eyl�l    4875.0  7201.0  2711.0
Aral�k   2669.0  4876.0  2344.0
"""