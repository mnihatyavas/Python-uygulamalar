# coding:iso-8859-9 T�rk�e
# p_32005.py: Pandas serisinde None-null de�erlerin idaresi �rne�i.

import pandas as pd

s�zl�k = {"a":23, "b":45, "c":None, "d":0, "e":None}
seri = pd.Series (s�zl�k)

print ("None de�erli float seri:\n", seri, sep="")
print ("\nSeri de�erleri null mu?:\n", pd.isnull (seri), sep="")
print ("\nSeri de�erleri null de�il mi?:\n", pd.notnull (seri), sep="")
print ("\nNone de�erlileri seriden ele:\n", seri.dropna(), sep="")
print ("\nNone de�erlileri s�f�rla:\n", seri.fillna (0), sep="")
print ("\nNone de�erlilere de�er ata ve tamsay�la:\n", seri.fillna ({"c":15, "e":29}).astype (int), sep="")



"""��kt�:
>python p_32005.py
None de�erli float seri:
a    23.0
b    45.0
c     NaN
d     0.0
e     NaN
dtype: float64

Seri de�erleri null mu?:
a    False
b    False
c     True
d    False
e     True
dtype: bool

Seri de�erleri null de�il mi?:
a     True
b     True
c    False
d     True
e    False
dtype: bool

None de�erlileri seriden ele:
a    23.0
b    45.0
d     0.0
dtype: float64

None de�erlileri s�f�rla:
a    23.0
b    45.0
c     0.0
d     0.0
e     0.0
dtype: float64

None de�erlilere de�er ata ve tamsay�la:
a    23
b    45
c    15
d     0
e    29
dtype: int32
"""