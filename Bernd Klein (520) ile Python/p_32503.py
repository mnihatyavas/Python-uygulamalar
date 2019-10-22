#coding:iso-8859-9 Türkçe
# p_32503.py: Yıllara yaygın python kurs ziyaretçilerinin grafiklenmesi örneği.

import matplotlib.pyplot as mp
import pandas as pd

#vÇ_path = "https://www.python-course.eu/data1/python_course_monthly_history.txt"
vÇ = pd.read_csv ("p_32503x.txt", delimiter=",", encoding="iso-8859-9")

print ("Python kurslarına aylık katılım veri çerçevesi (son-10):\n", vÇ.tail (10), sep="")
print ("\nVeri çerçevesi kolon adları:\n", vÇ.columns, sep="")

#vÇ.to_csv ("p_32503.txt")
#---------------------------------------------------------------------------------------------------------

def birimÇevirici (x):
    değer, birim = x
    if birim == "MB": değer *= 1024
    elif birim == "GB": değer *= 1048576 # yani: 1024 **2
    return değer # Bant genişliği değeriyle MB veya GB çarpımı...

bantBirim= vÇ[["Bant genişliği", "Birim"]]
bantGenişliği = bantBirim.apply (birimÇevirici, axis=1)
del vÇ["Birim"]
vÇ["Bant genişliği"] = bantGenişliği
del vÇ["Bant genişliği"] # Birsürü çevrim hesapları yapıp neden siliyorsun?..

ayYıl =  vÇ[["Ay", "Yıl"]]
ayYıl = ayYıl.apply (lambda x: x[0] + " " + str (x [1]), axis=1)
vÇ["Ay"] = ayYıl
del vÇ["Yıl"]
vÇ.set_index ("Ay", inplace=True)

del vÇ ["Sayfalar"]
del vÇ ["Zirve"]

print ("\nGrafiğe sunulan veri çerçevesi (ilk-10):\n", vÇ.head (10), sep="")

mp.style.use ("dark_background")
vÇ[["Tikel ziyaretçiler", "Ziyaret sayısı"]].plot (
    use_index=True,
    rot=90,
    xticks=range (1, len (vÇ.index), 4) ) # 4 aylık aralıklarla grafikle...
mp.show()
#---------------------------------------------------------------------------------------------------------

oran = pd.Series (vÇ ["Ziyaret sayısı"] / vÇ ["Tikel ziyaretçiler"], index=vÇ.index)
oran.plot (
    use_index=True,
    xticks=range (1, len (oran.index), 4),
    rot=90)
print ("\nZiyaret sıklığının ziyaretçilere oranı serisi (son-10):\n", oran [-10:], sep="")
mp.show()



"""Çıktı:
>python p_32503.py
Python kurslarına aylık katılım veri çerçevesi (son-10):
      Ay   Yıl  Tikel ziyaretçiler  ...     Zirve  Bant genişliği  Birim
92   Feb  2018              457861  ...   8110373          382.76     GB
93   Mar  2018              476179  ...   8684025          423.81     GB
94   Apr  2018              434346  ...   7723268          377.56     GB
95   May  2018              402390  ...   7307779          394.72     GB
96   Jun  2018              369739  ...   6773820          386.60     GB
97   Jul  2018              352670  ...   6551347          375.86     GB
98   Aug  2018              407512  ...   7829987          472.37     GB
99   Sep  2018              463937  ...   8468723          514.46     GB
100  Oct  2018              537343  ...  10013025          620.55     GB
101  Nov  2018              514072  ...   9487834          642.16     GB

[10 rows x 8 columns]

Veri çerçevesi kolon adları:
Index(['Ay', 'Yıl', 'Tikel ziyaretçiler', 'Ziyaret sayısı', 'Sayfalar',
       'Zirve', 'Bant genişliği', 'Birim'],
      dtype='object')

Grafiğe sunulan veri çerçevesi (ilk-10):
          Tikel ziyaretçiler  Ziyaret sayısı
Ay
Jun 2010                  11              13
Jul 2010                  27              39
Aug 2010                  75              87
Sep 2010                 171             221
Oct 2010                 238             301
Nov 2010                 353             455
Dec 2010                 366             423
Jan 2011                 911            1111
Feb 2011                1488            1807
Mar 2011                2128            2762

Ziyaret sıklığının ziyaretçilere oranı serisi (son-10):
Ay
Feb 2018    1.551663
Mar 2018    1.554140
Apr 2018    1.527186
May 2018    1.540776
Jun 2018    1.550018
Jul 2018    1.566674
Aug 2018    1.576744
Sep 2018    1.515997
Oct 2018    1.537733
Nov 2018    1.519894
dtype: float64
"""