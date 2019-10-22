# coding:iso-8859-9 Türkçe
# p_32105.py: Gelişigüzel (12x11) sayılı veri çerçevesinin endeks-kolon-yenidenEndeks örneği.

import pandas as pd
import numpy as np

adlar = ['Bekir', 'Fadime', 'Memet', 'Hanım', 'Hatice', "Süheyla", "Zeliha", "Nihat", "Songül", "Nedim", "Sevim"]
ayEndeksi = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
vç = pd.DataFrame ( (np.random.randn (12, 11) * 2000 + 3000).round (0),
    columns=adlar, index=ayEndeksi)

print ("Aylara endeksli 2019 yılı borç-alacak tablosu:\n", vç, sep="")
print ("\nAdlara endeksli 2019 yılı aylık borç-alacak tablosu:\n", vç.T, sep="")
print ("\nAdlara endeksli 2019 yılı 3 aylık borç-alacak tablosu:\n", vç.T.reindex (columns=["Haziran", "Eylül", "Aralık"]), sep="")
print ("\n3 kişinin aylara endeksli 2019 yılı aylık borç-alacak tablosu:\n", vç.reindex (columns=["Hatice", "Nihat", "Sevim"]), sep="")
print ("\n3 aya endeksli 2019 yılı aylık borç-alacak tablosu:\n", vç.reindex (index=["Haziran", "Eylül", "Aralık"]), sep="")
print ("\n3 kişinin 3 aya endeksli 2019 yılı aylık borç-alacak tablosu:\n", vç.reindex (index=["Haziran", "Eylül", "Aralık"], columns=["Hatice", "Nihat", "Sevim"]), sep="")



"""Çıktı:
>python p_32105.py
Aylara endeksli 2019 yılı borç-alacak tablosu:
          Bekir  Fadime   Memet   Hanım  ...   Nihat  Songül   Nedim   Sevim
Ocak     4807.0  1236.0  2912.0  3638.0  ...  4522.0   428.0  4304.0  5299.0
Şubat    5565.0  3320.0  -520.0  2154.0  ...  5592.0  1444.0  5313.0  5368.0
Mart     2136.0  2690.0  2126.0  3371.0  ...  5158.0   340.0  1729.0   196.0
Nisan    4600.0  2161.0  4524.0  2953.0  ...  5211.0  1088.0  -236.0  1061.0
Mayıs    2512.0  4720.0  4656.0  3951.0  ...  4692.0  2162.0   344.0  2328.0
Haziran  4202.0  -445.0  1686.0  4077.0  ...  4843.0  4196.0   805.0  1908.0
Temmuz    989.0  4719.0  1029.0  2142.0  ...   356.0  3055.0  4468.0  7985.0
Ağustos  2645.0  2640.0  2518.0  2361.0  ...  2289.0  4251.0   721.0  3086.0
Eylül    5670.0   995.0  2156.0  2814.0  ...  7201.0  1743.0  3915.0  2711.0
Ekim     -328.0  2367.0  3241.0  1238.0  ...  2992.0  3296.0  1956.0  3544.0
Kasım     792.0  2886.0 -1596.0  2690.0  ...  2396.0  6568.0  5190.0  3360.0
Aralık   1266.0  -943.0  1775.0  4938.0  ...  4876.0  1170.0  1634.0  2344.0

[12 rows x 11 columns]

Adlara endeksli 2019 yılı aylık borç-alacak tablosu:
           Ocak   Şubat    Mart   Nisan  ...   Eylül    Ekim   Kasım  Aralık
Bekir    4807.0  5565.0  2136.0  4600.0  ...  5670.0  -328.0   792.0  1266.0
Fadime   1236.0  3320.0  2690.0  2161.0  ...   995.0  2367.0  2886.0  -943.0
Memet    2912.0  -520.0  2126.0  4524.0  ...  2156.0  3241.0 -1596.0  1775.0
Hanım    3638.0  2154.0  3371.0  2953.0  ...  2814.0  1238.0  2690.0  4938.0
Hatice    465.0  3139.0  4746.0  1769.0  ...  4875.0 -1045.0  1052.0  2669.0
Süheyla  1437.0  3295.0  2034.0  1250.0  ...  4333.0  2764.0  4587.0  -996.0
Zeliha   3307.0  2491.0  5806.0  2385.0  ...  5122.0  3789.0  2133.0  2505.0
Nihat    4522.0  5592.0  5158.0  5211.0  ...  7201.0  2992.0  2396.0  4876.0
Songül    428.0  1444.0   340.0  1088.0  ...  1743.0  3296.0  6568.0  1170.0
Nedim    4304.0  5313.0  1729.0  -236.0  ...  3915.0  1956.0  5190.0  1634.0
Sevim    5299.0  5368.0   196.0  1061.0  ...  2711.0  3544.0  3360.0  2344.0

[11 rows x 12 columns]

Adlara endeksli 2019 yılı 3 aylık borç-alacak tablosu:
         Haziran   Eylül  Aralık
Bekir     4202.0  5670.0  1266.0
Fadime    -445.0   995.0  -943.0
Memet     1686.0  2156.0  1775.0
Hanım     4077.0  2814.0  4938.0
Hatice    5059.0  4875.0  2669.0
Süheyla   6098.0  4333.0  -996.0
Zeliha    4592.0  5122.0  2505.0
Nihat     4843.0  7201.0  4876.0
Songül    4196.0  1743.0  1170.0
Nedim      805.0  3915.0  1634.0
Sevim     1908.0  2711.0  2344.0

3 kişinin aylara endeksli 2019 yılı aylık borç-alacak tablosu:
         Hatice   Nihat   Sevim
Ocak      465.0  4522.0  5299.0
Şubat    3139.0  5592.0  5368.0
Mart     4746.0  5158.0   196.0
Nisan    1769.0  5211.0  1061.0
Mayıs    2238.0  4692.0  2328.0
Haziran  5059.0  4843.0  1908.0
Temmuz   -200.0   356.0  7985.0
Ağustos  4659.0  2289.0  3086.0
Eylül    4875.0  7201.0  2711.0
Ekim    -1045.0  2992.0  3544.0
Kasım    1052.0  2396.0  3360.0
Aralık   2669.0  4876.0  2344.0

3 aya endeksli 2019 yılı aylık borç-alacak tablosu:
          Bekir  Fadime   Memet   Hanım  ...   Nihat  Songül   Nedim   Sevim
Haziran  4202.0  -445.0  1686.0  4077.0  ...  4843.0  4196.0   805.0  1908.0
Eylül    5670.0   995.0  2156.0  2814.0  ...  7201.0  1743.0  3915.0  2711.0
Aralık   1266.0  -943.0  1775.0  4938.0  ...  4876.0  1170.0  1634.0  2344.0

[3 rows x 11 columns]

3 kişinin 3 aya endeksli 2019 yılı aylık borç-alacak tablosu:
         Hatice   Nihat   Sevim
Haziran  5059.0  4843.0  1908.0
Eylül    4875.0  7201.0  2711.0
Aralık   2669.0  4876.0  2344.0
"""