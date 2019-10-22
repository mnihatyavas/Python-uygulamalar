# coding:iso-8859-9 Türkçe
# p_32001.py: Basit bir pandas serisiyle numpy dizisinin karşılaştırılması örneği.

#pip install pandas
#Successfully installed pandas-0.24.2 pytz-2019.1

import pandas as pd

seri = pd.Series ([11, 28, 72, 3, 5, 8])
print ("Panda serisinin endeks, değer ve tipi:\n", seri, sep="")
print ("\nSerinin değerleri:", seri.values)
print ("Serinin endeks kapsamı:", seri.index)
print ("-"*60)
#------------------------------------------------------------------------------------------------------

import numpy as np

seri2 = np.array ([11, 28, 72, 3, 5, 8])
print ("\nNumpy dizisi:", seri2)
print ("Pandas seri değerleri:", seri.values)
print ("Pandas seri tipi = Numpy dizi tipi:\n",
    type (seri.values), " = ", type (seri2), sep="")
print ("Serinin ilk ve son değerleri:", seri [0], seri [len (seri) - 1])



"""Çıktı:
>python p_32001.py
Panda serisinin endeks, değer ve tipi:
0    11
1    28
2    72
3     3
4     5
5     8
dtype: int64

Serinin değerleri: [11 28 72  3  5  8]
Serinin endeks kapsamı: RangeIndex(start=0, stop=6, step=1)
------------------------------------------------------------

Numpy dizisi: [11 28 72  3  5  8]
Pandas seri değerleri: [11 28 72  3  5  8]
Pandas seri tipi = Numpy dizi tipi:
<class 'numpy.ndarray'> = <class 'numpy.ndarray'>
Serinin ilk ve son değerleri: 11 8
"""