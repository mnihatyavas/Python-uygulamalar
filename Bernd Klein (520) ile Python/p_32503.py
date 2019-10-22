#coding:iso-8859-9 T�rk�e
# p_32503.py: Y�llara yayg�n python kurs ziyaret�ilerinin grafiklenmesi �rne�i.

import matplotlib.pyplot as mp
import pandas as pd

#v�_path = "https://www.python-course.eu/data1/python_course_monthly_history.txt"
v� = pd.read_csv ("p_32503x.txt", delimiter=",", encoding="iso-8859-9")

print ("Python kurslar�na ayl�k kat�l�m veri �er�evesi (son-10):\n", v�.tail (10), sep="")
print ("\nVeri �er�evesi kolon adlar�:\n", v�.columns, sep="")

#v�.to_csv ("p_32503.txt")
#---------------------------------------------------------------------------------------------------------

def birim�evirici (x):
    de�er, birim = x
    if birim == "MB": de�er *= 1024
    elif birim == "GB": de�er *= 1048576 # yani: 1024 **2
    return de�er # Bant geni�li�i de�eriyle MB veya GB �arp�m�...

bantBirim= v�[["Bant geni�li�i", "Birim"]]
bantGeni�li�i = bantBirim.apply (birim�evirici, axis=1)
del v�["Birim"]
v�["Bant geni�li�i"] = bantGeni�li�i
del v�["Bant geni�li�i"] # Birs�r� �evrim hesaplar� yap�p neden siliyorsun?..

ayY�l =  v�[["Ay", "Y�l"]]
ayY�l = ayY�l.apply (lambda x: x[0] + " " + str (x [1]), axis=1)
v�["Ay"] = ayY�l
del v�["Y�l"]
v�.set_index ("Ay", inplace=True)

del v� ["Sayfalar"]
del v� ["Zirve"]

print ("\nGrafi�e sunulan veri �er�evesi (ilk-10):\n", v�.head (10), sep="")

mp.style.use ("dark_background")
v�[["Tikel ziyaret�iler", "Ziyaret say�s�"]].plot (
    use_index=True,
    rot=90,
    xticks=range (1, len (v�.index), 4) ) # 4 ayl�k aral�klarla grafikle...
mp.show()
#---------------------------------------------------------------------------------------------------------

oran = pd.Series (v� ["Ziyaret say�s�"] / v� ["Tikel ziyaret�iler"], index=v�.index)
oran.plot (
    use_index=True,
    xticks=range (1, len (oran.index), 4),
    rot=90)
print ("\nZiyaret s�kl���n�n ziyaret�ilere oran� serisi (son-10):\n", oran [-10:], sep="")
mp.show()



"""��kt�:
>python p_32503.py
Python kurslar�na ayl�k kat�l�m veri �er�evesi (son-10):
      Ay   Y�l  Tikel ziyaret�iler  ...     Zirve  Bant geni�li�i  Birim
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

Veri �er�evesi kolon adlar�:
Index(['Ay', 'Y�l', 'Tikel ziyaret�iler', 'Ziyaret say�s�', 'Sayfalar',
       'Zirve', 'Bant geni�li�i', 'Birim'],
      dtype='object')

Grafi�e sunulan veri �er�evesi (ilk-10):
          Tikel ziyaret�iler  Ziyaret say�s�
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

Ziyaret s�kl���n�n ziyaret�ilere oran� serisi (son-10):
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