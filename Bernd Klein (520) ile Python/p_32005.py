# coding:iso-8859-9 Türkçe
# p_32005.py: Pandas serisinde None-null değerlerin idaresi örneği.

import pandas as pd

sözlük = {"a":23, "b":45, "c":None, "d":0, "e":None}
seri = pd.Series (sözlük)

print ("None değerli float seri:\n", seri, sep="")
print ("\nSeri değerleri null mu?:\n", pd.isnull (seri), sep="")
print ("\nSeri değerleri null değil mi?:\n", pd.notnull (seri), sep="")
print ("\nNone değerlileri seriden ele:\n", seri.dropna(), sep="")
print ("\nNone değerlileri sıfırla:\n", seri.fillna (0), sep="")
print ("\nNone değerlilere değer ata ve tamsayıla:\n", seri.fillna ({"c":15, "e":29}).astype (int), sep="")



"""Çıktı:
>python p_32005.py
None değerli float seri:
a    23.0
b    45.0
c     NaN
d     0.0
e     NaN
dtype: float64

Seri değerleri null mu?:
a    False
b    False
c     True
d    False
e     True
dtype: bool

Seri değerleri null değil mi?:
a     True
b     True
c    False
d     True
e    False
dtype: bool

None değerlileri seriden ele:
a    23.0
b    45.0
d     0.0
dtype: float64

None değerlileri sıfırla:
a    23.0
b    45.0
c     0.0
d     0.0
e     0.0
dtype: float64

None değerlilere değer ata ve tamsayıla:
a    23
b    45
c    15
d     0
e    29
dtype: int32
"""