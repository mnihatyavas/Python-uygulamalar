# coding:iso-8859-9 Türkçe
# p_32104.py: İç-içe sözlükten veri çerçevesinin satır ve sütunlarını yerdeğiştirme örneği.

import pandas as pd

yıllıkBüyüme = {# İç-içe sözlük...
    "İsviçre": {"2010": 3.0, "2011": 1.8, "2012": 1.1, "2013": 1.9},
    "Almanya": {"2010": 4.1, "2011": 3.6, "2012": 0.4, "2013": 0.1},
    "Fransa": {"2010":2.0,  "2011":2.1, "2012": 0.3, "2013": 0.3},
    "Yunanistan": {"2010":-5.4, "2011":-8.9, "2012":-6.6, "2013":	-3.3},
    "İtalya": {"2010":1.7, "2011":	0.6, "2012":-2.3, "2013":-1.9},
    "Türkiye": {"2010": 3.2, "2011": 4.1, "2012": 3.8, "2013":6.5} }

bç = pd.DataFrame (yıllıkBüyüme) # Büyüme Çerçevesi...
print ("Yıla endeksli ülkelerin büyüme oranları yüzdesi:\n", bç, sep="")

bç1 = bç.T
print ("\nÜlkeye endeksli yıllık büyüme oranları yüzdesi:\n", bç, sep="") # T:transpose

print ("\n3 ülkeye endeksli yıllık büyüme oranları yüzdesi:\n", bç1.reindex (["Türkiye", "İtalya", "Yunanistan"]), sep="")



"""Çıktı:
>python p_32104.py
Yıla endeksli ülkelerin büyüme oranları yüzdesi:
      İsviçre  Almanya  Fransa  Yunanistan  İtalya  Türkiye
2010      3.0      4.1     2.0        -5.4     1.7      3.2
2011      1.8      3.6     2.1        -8.9     0.6      4.1
2012      1.1      0.4     0.3        -6.6    -2.3      3.8
2013      1.9      0.1     0.3        -3.3    -1.9      6.5

Ülkeye endeksli yıllık büyüme oranları yüzdesi:
      İsviçre  Almanya  Fransa  Yunanistan  İtalya  Türkiye
2010      3.0      4.1     2.0        -5.4     1.7      3.2
2011      1.8      3.6     2.1        -8.9     0.6      4.1
2012      1.1      0.4     0.3        -6.6    -2.3      3.8
2013      1.9      0.1     0.3        -3.3    -1.9      6.5

3 ülkeye endeksli yıllık büyüme oranları yüzdesi:
            2010  2011  2012  2013
Türkiye      3.2   4.1   3.8   6.5
İtalya       1.7   0.6  -2.3  -1.9
Yunanistan  -5.4  -8.9  -6.6  -3.3
"""